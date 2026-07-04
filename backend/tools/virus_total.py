def check_ip(ip: str) -> dict:
    """
    Mock VirusTotal lookup.
    Replace with real API later.
    """

    suspicious_ips = {
        "192.168.1.10": {
            "reputation": "Suspicious",
            "country": "India",
            "malicious_score": 82,
            "provider": "VirusTotal (Mock)"
        },

        "8.8.8.8": {
            "reputation": "Safe",
            "country": "USA",
            "malicious_score": 0,
            "provider": "VirusTotal (Mock)"
        }
    }

    return suspicious_ips.get(
        ip,
        {
            "reputation": "Unknown",
            "country": "Unknown",
            "malicious_score": 0,
            "provider": "VirusTotal (Mock)"
        }
    )