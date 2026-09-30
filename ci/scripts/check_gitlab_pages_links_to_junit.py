#!/usr/bin/env python3
"""
Convert RST links pointing to GitLab Pages into a JUnit XML report.

Usage:
  python3 scripts/check_gitlab_pages_links_to_junit.py [source_dir] [output.xml]

Defaults:
  source_dir: source
  output.xml: gitlab-links-junit.xml
"""
import os
import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from urllib.parse import urlparse

def clean_text(s):
    if s is None:
        return ''
    s = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', s)
    s = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', s)
    return s

def find_rst_files(root):
    for dirpath, dirs, files in os.walk(root):
        for fn in files:
            if fn.lower().endswith('.rst'):
                yield os.path.join(dirpath, fn)

def url_host_is_gitlab(host):
    if not host:
        return False
    host = host.lower()
    # NIST internal domains
    if 'ipages.nist.gov' in host:
        return True
    # MITRE internal domains
    if 'pages.mitre.org' in host:
        return True
    return False

def parse_file_for_gitlab_links(path):
    """
    Return list of dicts {file, line, url, msg} for absolute URLs in RST files that point to GitLab domains/pages.
    """
    issues = []
    url_re = re.compile(r'https?://[^\s\)\]\>]+')
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            for idx, line in enumerate(fh, start=1):
                for m in url_re.finditer(line):
                    url = m.group(0)
                    try:
                        p = urlparse(url)
                        host = p.netloc
                    except Exception:
                        host = ''
                    if url_host_is_gitlab(host):
                        issues.append({
                            'file': clean_text(path),
                            'line': str(idx),
                            'url': clean_text(url),
                            'msg': clean_text(f"Found absolute internal GitLab URL '{url}' in {path}:{idx}")
                        })
    except FileNotFoundError:
        return issues
    return issues

def collect_issues(root='source'):
    all_issues = []
    for rst in find_rst_files(root):
        all_issues.extend(parse_file_for_gitlab_links(rst))
    return all_issues

def build_junit(issues):
    testsuite = ET.Element('testsuite', name='gitlab-links-check', tests="1", failures="1" if issues else "0")
    tc = ET.SubElement(testsuite, 'testcase', classname='Sphinx', name="GitLab Links Check")
    msg = []
    if issues:
        failure = ET.SubElement(tc, 'failure', message=f"GitLab links found")
        for it in issues:
            msg.append(it['msg'])
        failure.text = "\n".join(msg)
    return testsuite

def pretty_xml(elem):
    rough = ET.tostring(elem, encoding='unicode')
    reparsed = minidom.parseString(rough)
    return reparsed.toprettyxml(indent='  ')

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else 'source'
    out = sys.argv[2] if len(sys.argv) > 2 else 'gitlab-links-junit.xml'
    issues = collect_issues(src)
    testsuite = build_junit(issues)
    xml_str = pretty_xml(testsuite)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(xml_str)
    print(f'Wrote {out} with {len(issues)} issue(s).')

if __name__ == '__main__':
    main()
