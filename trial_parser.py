import os
import sys

# ======================================================================
#         SPATIALGUARD SECURITY PIPELINE - TRIAL ENFORCEMENT ENGINE
# ======================================================================
TRIAL_BYTE_LIMIT = 35  # Strict evaluation constraint for freemium model

def check_license_or_enforce(file_path):
    """
    Automated Gatekeeper: Verifies file constraints locally. 
    Prevents enterprise clients from bypassing paid commercial tiers.
    """
    if not os.path.exists(file_path):
        print(f"[ERROR]: Target file '{file_path}' not found.")
        sys.exit(1)
        
    file_size = os.path.getsize(file_path)
    
    # If the file size exceeds the freemium allowance, trigger the automated funnel block
    if file_size > TRIAL_BYTE_LIMIT:
        print("=" * 70)
        print("[AUTOMATED PIPELINE ALERT]: PREVENTED UNAUTHORIZED ENTERPRISE USE")
        print("=" * 70)
        print(f"Detected File Size: {file_size} bytes.")
        print(f"Freemium Evaluation Capacity: Unlimited files up to {TRIAL_BYTE_LIMIT} bytes each.")
        print("-" * 70)
        print("CRITICAL: Your dataset exceeds the standalone trial limits.")
        print("To process large production files and unlock our multi-threaded C server engine,")
        print("your corporate infrastructure requires a valid Commercial License Key.")
        print("\n🔒 Secure your production environment instantly at your storefront:")
        print("👉 https://github.com")
        print("=" * 70)
        sys.exit(1)

    print(f"[SUCCESS]: File size ({file_size} bytes) verified within standalone trial bounds.")
    print("Initiating sliding-key matrix cyclic mathematical transformation execution...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 trial_parser.py <path_to_log_file>")
        sys.exit(1)
    
    # Run the automated gatekeeper evaluation check using the first argument file path
    check_license_or_enforce(sys.argv[1])
