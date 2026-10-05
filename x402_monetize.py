import json

def get_x402_agent_card():
    return {
        "x402_version": "1.0",
        "pricing": {
            "tier": "enterprise",
            "price_usd": 500,
            "currency": "CAD",
            "eta": "48h",
            "note": "Monetized via NanoEmpire A2A Protocol",
            "checkout_url": "https://www.nanoempireai.com/manifests.html"
        },
        "capabilities": ["tools:call", "resources:read"],
        "developer": "roblambert9"
    }

if __name__ == "__main__":
    print(json.dumps(get_x402_agent_card(), indent=2))
