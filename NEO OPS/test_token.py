import asyncio
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from telegram import Bot

async def test_token():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    if not TOKEN:
        print("❌ Error: TELEGRAM_BOT_TOKEN environment variable not set.")
        print("Please create a .env file with TELEGRAM_BOT_TOKEN=your_token_here")
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
