TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "create_order",
            "description": "Create a logistics order",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "Product name like shoes, phone"
                    },
                    "weight": {
                        "type": "string",
                        "description": "Weight in kg"
                    },
                    "city": {
                        "type": "string",
                        "description": "Delivery city"
                    }
                },
                "required": ["product_name", "weight", "city"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email to a user",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {
                        "type": "string",
                        "description": "Recipient email address"
                    },
                    "subject": {
                        "type": "string",
                        "description": "Email subject"
                    },
                    "body": {
                        "type": "string",
                        "description": "Email body content"
                    }
                },
                "required": ["to", "subject", "body"]
            }
        }
    }
]