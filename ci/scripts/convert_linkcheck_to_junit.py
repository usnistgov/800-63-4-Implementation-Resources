#!/usr/bin/env python3
"""Convert Sphinx linkcheck output to a JUnit XML file consumable by GitLab.

Usage:
  python scripts/convert_linkcheck_to_junit.py [linkcheck.log] [output.xml]
"""
import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def clean_text(s):
    """Remove ANSI escape sequences and control characters that are invalid in XML."""
    if s is None:
        return ''
    # Strip common ANSI CSI sequences like "\x1b[31m"
    s = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', s)
    # Remove C0 control chars except TAB (0x09), LF (0x0A), CR (0x0D)
    s = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', s)
    return s

def parse_linkcheck(path):
    """Parse linkcheck output and return a list of issues with url and msg."""
    issues = []
    # Match http/https URLs (stop at whitespace or common trailing punctuation)
    url_re = re.compile(r'https?://[^\s\)\]\,;]+')
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            for line in fh:
                line = line.rstrip()
                lower = line.lower()
                # Heuristic: lines that mention "broken", "broken link", "failed", or contain a WARNING plus a URL
                if 'broken' in lower or 'broken link' in lower or 'failed' in lower or 'dead' in lower:
                    m = url_re.search(line)
                    url = m.group(0) if m else 'unknown'
                    issues.append({'url': clean_text(url), 'msg': clean_text(line)})
                else:
                    if 'warning' in lower and ('http://' in line or 'https://' in line):
                        m = url_re.search(line)
                        url = m.group(0) if m else 'unknown'
                        issues.append({'url': clean_text(url), 'msg': clean_text(line)})
    except FileNotFoundError:
        return []
    return issues

def build_junit(issues):
    testsuite = ET.Element('testsuite', name='sphinx-linkcheck', tests="1", failures="1" if issues else "0")
    tc = ET.SubElement(testsuite, 'testcase', classname='Sphinx', name="Link Check")
    msg = []
    if issues:
        failure = ET.SubElement(tc, 'failure', message=f"Broken links found")
        for it in issues:
            msg.append(it['msg'])
        failure.text = "\n".join(msg)
    return testsuite

def pretty_xml(elem):
    # Produce a Unicode string for minidom.parseString and avoid passing raw bytes.
    rough = ET.tostring(elem, encoding='unicode')
    reparsed = minidom.parseString(rough)
    return reparsed.toprettyxml(indent='  ')

def main():
    inp = sys.argv[1] if len(sys.argv) > 1 else 'linkcheck.log'
    out = sys.argv[2] if len(sys.argv) > 2 else 'linkcheck-junit.xml'
    issues = parse_linkcheck(inp)
    testsuite = build_junit(issues)
    xml_str = pretty_xml(testsuite)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(xml_str)
    print(f'Wrote {out} with {len(issues)} issue(s).')

if __name__ == '__main__':
    main()
