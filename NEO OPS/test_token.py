import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot

# Load environment variables
load_dotenv()

async def test_token():
    TOKEN = os.getenv('TOKEN')

    if not TOKEN:
        print("❌ Error: TOKEN environment variable is not set.")
        return

    try:
        print("🔍 Testing bot token...")
        bot = Bot(token=TOKEN)
        me = await bot.get_me()

        print("✅ SUCCESS! Bot is working!")
        print(f"🤖 Bot Name: {me.first_name}")
        print(f"📝 Username: @{me.username}")
        print(f"🔗 Link: https://t.me/{me.username}")

        print("\n🎯 Your bot is ready!")
        print("1. Click the link above to open your bot")
        print("2. Click 'Start' to begin chatting")
        print("3. Send: 'Neo Mode' to test")

    except Exception as e:
        print(f"❌ Error: {e}")
        if "Unauthorized" in str(e):
            print("🔑 Token is invalid. Please check:")
            print("   - Did you copy the token correctly?")
            print("   - Did you get it from @BotFather?")
            print("   - Is there any extra space in the token?")

if __name__ == "__main__":
    asyncio.run(test_token())
