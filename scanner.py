import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

class VulnerabilityScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.vulnerabilities = []

    def scan_for_sql_injection(self):
        # Common SQL injection payloads
        payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*"]

        for payload in payloads:
            url = f"{self.target_url}?q={payload}"
            response = requests.get(url)
            if "error" in response.text.lower() or "sql" in response.text.lower():
                self.vulnerabilities.append(f"SQL Injection vulnerability found with payload: {payload}")

    def scan(self):
        self.scan_for_sql_injection()
        return self.vulnerabilities

@app.route("/scan", methods=['POST'])
def scan():
    data = request.json
    target_url = data.get('target_url')
    if not target_url:
        return jsonify({"error": "target_url is required"}), 400

    scanner = VulnerabilityScanner(target_url)
    vulnerabilities = scanner.scan()

    return jsonify({"vulnerabilities": vulnerabilities})

if __name__ == "__main__":
    app.run(debug=True)
