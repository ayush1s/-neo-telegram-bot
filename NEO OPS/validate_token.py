import re
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def validate_token_format(token):
    if not token:
        print("❌ Error: No token provided for validation.")
        return False

    print(f"🔍 Validating token format: {token}")

    # Check if token matches expected format
    pattern = r'^\d+:[A-Za-z0-9_-]+$'

    if re.match(pattern, token):
        print("✅ Token format looks correct!")
        print(f"📏 Length: {len(token)} characters")

        # Split token
        parts = token.split(':')
        print(f"🔢 Bot ID: {parts[0]}")
        print(f"🔑 Token part: {parts[1]}")

        return True
    else:
        print("❌ Token format is incorrect!")
        print("Expected format: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
        return False

# Test the current token from environment
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("❌ TELEGRAM_BOT_TOKEN environment variable not set.")
    print("💡 Please create a .env file with TELEGRAM_BOT_TOKEN=your_token_here")
else:
    validate_token_format(TOKEN)

print("\n💡 If the format is correct but still unauthorized:")
print("1. Make sure you got the token from @BotFather")
print("2. Try copying the token again")
print("3. Check for any extra spaces")
print("4. Make sure the bot is not deleted")
