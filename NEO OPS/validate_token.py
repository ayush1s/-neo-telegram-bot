import re

def validate_token_format(token):
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
TOKEN = "8150634144:AAG5SNj7AWMhRdiGuyb19A48ERQTK4MpKTE"
validate_token_format(TOKEN)

print("\n💡 If the format is correct but still unauthorized:")
print("1. Make sure you got the token from @BotFather")
print("2. Try copying the token again")
print("3. Check for any extra spaces")
print("4. Make sure the bot is not deleted") 