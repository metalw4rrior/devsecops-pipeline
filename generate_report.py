import json
import xml.etree.ElementTree as ET
from jinja2 import Template

# Function to load JSON files
def load_json(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to load XML files
def load_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return ET.tostring(root, encoding='unicode')
    except FileNotFoundError:
        return ''

# Function to run scans and generate reports
def run_scans():
    safety_report = load_json('safety_report.json')
    # Run Bandit scan and save report to 'bandit_report.txt'
    bandit_report = run_bandit_scan()
    test_results = load_xml('test_results.xml')
    return safety_report, bandit_report, test_results

# Function to run Bandit scan and save report to 'bandit_report.txt'
def run_bandit_scan():
    import subprocess
    subprocess.run(['bandit', '-r', 'app/', '-o', 'bandit_report.txt'], check=True)
    with open('bandit_report.txt', 'r') as f:
        return f.read()

# Load reports
safety_report, bandit_report, test_results = run_scans()

# HTML template with CSS styles
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CI/CD Scan Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        pre { background-color: #f9f9f9; padding: 10px; overflow-x: auto; }
        h1, h2 { color: #333; }
    </style>
</head>
<body>
    <h1>CI/CD Scan Report</h1>
    <h2>Safety Report</h2>
    <pre>{{ safety_report | tojson(indent=2) }}</pre>
    <h2>Bandit Report</h2>
    <pre>{{ bandit_report }}</pre>
    <h2>Test Results</h2>
    <pre>{{ test_results }}</pre>
</body>
</html>
"""

# Generate HTML report
template = Template(html_template)
html_content = template.render(
    safety_report=safety_report,
    bandit_report=bandit_report,
    test_results=test_results
)

# Save HTML report
with open('report.html', 'w') as f:
    f.write(html_content)
