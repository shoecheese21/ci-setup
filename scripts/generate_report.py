import xml.etree.ElementTree as ET

tree = ET.parse("report.xml")
root = tree.getroot()

tests = int(root.attrib["tests"])
failures = int(root.attrib["failures"])
errors = int(root.attrib["errors"])
passed = tests - failures - errors

with open("report.md", "w") as f:
    f.write("# 🧪 Test Execution Report\n\n")
    f.write(f"- Total Tests: **{tests}**\n")
    f.write(f"- Passed: **{passed}** ✅\n")
    f.write(f"- Failed: **{failures}** ❌\n")
    f.write(f"- Errors: **{errors}** ⚠️\n")
