#!/usr/bin/env python3
"""Convert sphinx-warnings.log to a JUnit XML file consumable by GitLab.

Usage:
  python scripts/convert_sphinx_warnings_to_junit.py [warnings.log] [output.xml]
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

def parse_warnings(path):
    warnings = []
    # Typical sphinx warning format: path/to/file:123: WARNING: message
    pattern = re.compile(r'^(?P<file>[^:]+):(?P<line>\d+):\s*WARNING:\s*(?P<msg>.*)$')
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
            for line in fh:
                line = line.rstrip()
                m = pattern.match(line)
                if m:
                    warnings.append({
                        'file': clean_text(m.group('file')),
                        'line': clean_text(m.group('line')),
                        'msg': clean_text(m.group('msg')),
                    })
                else:
                    # fallback: include any line that contains "WARNING"
                    if 'WARNING' in line:
                        warnings.append({'file': 'unknown', 'line': '0', 'msg': clean_text(line)})
    except FileNotFoundError:
        return []
    return warnings

def build_junit(warnings):
    testsuite = ET.Element('testsuite', name='sphinx-warnings', tests="1", failures="1" if warnings else "0")
    tc = ET.SubElement(testsuite, 'testcase', classname='Sphinx', name="Sphinx Build Warnings")
    msg = []
    if warnings:
        failure = ET.SubElement(tc, 'failure', message=f"Sphinx warnings found")
        for w in warnings:
            msg.append(w['msg'])
        failure.text = "\n".join(msg)
    return testsuite

def pretty_xml(elem):
    # Produce a Unicode string for minidom.parseString and avoid passing raw bytes.
    rough = ET.tostring(elem, encoding='unicode')
    reparsed = minidom.parseString(rough)
    return reparsed.toprettyxml(indent='  ')

def main():
    inp = sys.argv[1] if len(sys.argv) > 1 else 'sphinx-warnings.log'
    out = sys.argv[2] if len(sys.argv) > 2 else 'sphinx-warnings-junit.xml'
    warnings = parse_warnings(inp)
    testsuite = build_junit(warnings)
    xml_str = pretty_xml(testsuite)
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(xml_str)
    print(f'Wrote {out} with {len(warnings)} warning(s).')

if __name__ == '__main__':
    main()
