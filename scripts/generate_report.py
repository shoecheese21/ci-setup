import os
import xml.etree.ElementTree as ET

report_path = os.path.join(os.getcwd(), "report.xml")
summary_lines = ["# 🧪 Test Execution Report\n"]

if not os.path.exists(report_path):
    summary_lines.append("⚠️ No test report (report.xml) found. Tests may have failed to run.")
else:
    try:
        tree = ET.parse(report_path)
        root = tree.getroot()

        # Prefer aggregating counts from all <testsuite> elements (covers pytest's format)
        suites = []
        if root.tag == 'testsuite':
            suites = [root]
        else:
            suites = root.findall('.//testsuite')

        tests = failures = errors = skipped = 0
        if suites:
            for s in suites:
                tests += int(s.attrib.get('tests', 0))
                failures += int(s.attrib.get('failures', 0))
                errors += int(s.attrib.get('errors', 0))
                skipped += int(s.attrib.get('skipped', 0))
        else:
            # Fallback to attributes on the root
            tests = int(root.attrib.get('tests', 0))
            failures = int(root.attrib.get('failures', 0))
            errors = int(root.attrib.get('errors', 0))
            skipped = int(root.attrib.get('skipped', 0))
            if tests == 0:
                # As a last resort, count <testcase> elements
                tests = len(list(root.iter('testcase')))

        passed = tests - failures - errors - skipped
        summary_lines.append(f"- Total Tests: **{tests}**")
        summary_lines.append(f"- Passed: **{passed}** ✅")
        summary_lines.append(f"- Failed: **{failures}** ❌")
        summary_lines.append(f"- Errors: **{errors}** ⚠️")
        summary_lines.append(f"- Skipped: **{skipped}** 🔁")
    except Exception as e:
        summary_lines.append(f"⚠️ Failed to parse report.xml: {e}")

with open("report.md", "w") as f:
    f.write("\n".join(summary_lines) + "\n")
