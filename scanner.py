import requests

class VulnerabilityScanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def scan(self):
        # Example scan logic
        response = requests.get(self.target_url)
        if "vulnerable" in response.text:
            return "Vulnerability found!"
        return "No vulnerabilities found."

if __name__ == "__main__":
    scanner = VulnerabilityScanner("http://example.com")
    result = scanner.scan()
    print(result)
