import requests

def execute_tool(tool_name, args):

    if tool_name == "create_order":
        try:
            print("🔥 CALLING DJANGO WITH:", args)

            res = requests.post(
                "http://127.0.0.1:8000/api/orders/create/",
                json={
                    "product_name": args.get("product_name"),
                    "weight": args.get("weight"),
                    "city": args.get("city")
                },
                timeout=5
            )

            print("🔥 DJANGO STATUS:", res.status_code)
            print("🔥 DJANGO RESPONSE:", res.text)

            return res.json()

        except Exception as e:
            print("❌ ERROR:", str(e))
            return {
                "status": "error",
                "message": "Connection error."
            }

    elif tool_name == "send_email":
        return {
            "status": "success",
            "tool_used": "send_email"
        }

    return {"error": "Unknown tool"}