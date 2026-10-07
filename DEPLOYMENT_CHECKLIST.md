# SpatialGuard Commercial Launch Checklist

## Phase 1: Payment Gateways
- [ ] Create a merchant profile on Stripe (https://stripe.com)
- [ ] Generate a Payment Link for the Developer Tier (\$499.00 USD)
- [ ] Generate a Payment Link for the Enterprise Tier (\$1,999.00 USD)
- [ ] Swap out placeholder links in public `README.md` with active checkout URLs

## Phase 2: Webhook Fulfillment Configuration
- [ ] Configure Stripe Webhooks to ping your automated `fulfill_order.py` script upon payment completion
- [ ] Set up secure cloud variables to house cryptographic distribution binaries
