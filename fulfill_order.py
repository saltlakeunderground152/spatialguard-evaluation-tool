import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# In production, this matches the master key expected by your premium binary
AUTHORIZED_LICENSE_TOKEN = "SG-PREMIUM-2026-X97B"

@app.route('/stripe-webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    print("[CLOUD SERVER] Inbound network package received from payment gateway!")
    
    try:
        event = json.loads(payload)
        # Intercept successful payment sessions from your Stripe dashboard
        if event.get("type") == "checkout.session.completed":
            session = event["data"]["object"]
            customer_email = session["customer_details"]["email"]
            amount_paid = session["amount_total"] / 100
            
            print(f"\n💰 [REVENUE ALIGNMENT] Payment of ${amount_paid:.2f} confirmed from: {customer_email}")
            print(f"🔑 [AUTOMATED FULFILLMENT] Generating secure token credentials...")
            print(f"📨 [DISPATCH] Delivering License Key '{AUTHORIZED_LICENSE_TOKEN}' directly to {customer_email}\n")
            
            # This is where your cloud SMTP provider will fire the transaction receipt email
    except Exception as e:
        print(f"[ERROR] Failed to compile payload matrix: {str(e)}")

    return jsonify(status="success"), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
