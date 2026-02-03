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
        tests = int(root.attrib.get("tests", 0))
        failures = int(root.attrib.get("failures", 0))
        errors = int(root.attrib.get("errors", 0))
        skipped = int(root.attrib.get("skipped", 0))
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
