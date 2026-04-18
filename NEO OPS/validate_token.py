import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def validate_token_format(token):
    if not token:
        print("❌ No token provided!")
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

# Test the current token
TOKEN = os.getenv('TOKEN')
if TOKEN:
    validate_token_format(TOKEN)
else:
    print("❌ TOKEN environment variable not set.")

print("\n💡 If the format is correct but still unauthorized:")
print("1. Make sure you got the token from @BotFather")
print("2. Try copying the token again")
print("3. Check for any extra spaces")
print("4. Make sure the bot is not deleted")
