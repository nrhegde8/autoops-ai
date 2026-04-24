TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "create_order",
            "description": "Create a new logistics order",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"},
                    "weight": {"type": "string"},
                    "city": {"type": "string"}
                },
                "required": ["product_name", "weight", "city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["to", "subject", "body"]
            }
        }
    }
]