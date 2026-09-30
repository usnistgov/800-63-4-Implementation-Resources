#!/usr/bin/env python3
"""
Convert Sphinx RST image usage into a JUnit XML report that fails when images are missing alt text.

Usage:
  python3 scripts/check_images_alttext_to_junit.py [source_dir] [output.xml]

Defaults:
  source_dir: source
  output.xml: images-alttext-junit.xml
"""
import os
import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def clean_text(s):
    if s is None:
        return ''
    # Remove ANSI escapes and low control chars
    s = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', s)
    s = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', s)
    return s

def find_rst_files(root):
    for dirpath, dirs, files in os.walk(root):
        for fn in files:
            if fn.lower().endswith('.rst'):
                yield os.path.join(dirpath, fn)

def parse_file_for_images(path):
    """
    Return list of dicts {file, line, msg} for images/figures missing :alt:.
    Heuristic improvements:
     - Handle substitution-style directives like ".. |name| image:: path"
     - Detect :alt: on the same line as the directive
     - Scan following indented option lines for :alt:
    """
    issues = []
    # Allow optional substitution text between the leading ".." and the "image|figure::"
    directive_re = re.compile(r'^\s*\.\.\s+(?:\|[^|]+\|\s+)?(?:image|figure)::\s+(?P<src>\S+)', re.IGNORECASE)
    alt_re = re.compile(r'^\s*:[aA]lt\s*:', re.IGNORECASE)
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            lines = fh.readlines()
    except FileNotFoundError:
        return issues

    for idx, line in enumerate(lines):
        m = directive_re.match(line)
        if not m:
            continue

        # If the same line contains an :alt: option, treat it as having alt text.
        if ':alt:' in line.lower():
            continue

        # look ahead up to N lines for an :alt: option that is indented (typical RST option block)
        found_alt = False
        max_look = 10
        directive_indent = len(line) - len(line.lstrip(' '))
        for j in range(idx + 1, min(idx + 1 + max_look, len(lines))):
            nxt = lines[j]
            # If we encounter another directive (starts with "..") at same or lesser indentation, stop scanning.
            if re.match(r'^\s*\.\.', nxt) and (len(nxt) - len(nxt.lstrip(' '))) <= directive_indent:
                break
            if alt_re.match(nxt):
                found_alt = True
                break
            # continue scanning even through blank/option lines

        if not found_alt:
            src = m.group('src')
            issues.append({
                'file': clean_text(path),
                'line': str(idx + 1),
                'msg': clean_text(f"Image/figure '{src}' missing :alt: text in {path}:{idx+1}")
            })
    return issues

def collect_issues(root='source'):
    all_issues = []
    for rst in find_rst_files(root):
        all_issues.extend(parse_file_for_images(rst))
    return all_issues

def build_junit(issues):
    testsuite = ET.Element('testsuite', name='images-alttext-check', tests="1", failures="1" if issues else "0")
    tc = ET.SubElement(testsuite, 'testcase', classname='Sphinx', name="Images Alt Text Check")
    msg = []
    if issues:
        failure = ET.SubElement(tc, 'failure', message=f"Images missing alt text found")
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
    out = sys.argv[2] if len(sys.argv) > 2 else 'images-alttext-junit.xml'
    issues = collect_issues(src)
    testsuite = build_junit(issues)
    xml_str = pretty_xml(testsuite)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(xml_str)
    print(f'Wrote {out} with {len(issues)} issue(s).')

if __name__ == '__main__':
    main()
