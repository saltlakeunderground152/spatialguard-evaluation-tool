import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/stripe-webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    print("[CLOUD SERVER] Webhook received from payment gateway!")
    
    try:
        event = json.loads(payload)
        if event.get("type") == "checkout.session.completed":
            customer_email = event["data"]["object"]["customer_details"]["email"]
            print(f"[FULFILLMENT] Success! Packaging premium binary for {customer_email}")
    except Exception as e:
        print(f"[ERROR] Webhook processing failed: {str(e)}")

    return jsonify(status="success"), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
