import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot

# Load environment variables
load_dotenv()

async def test_bot():
    TOKEN = os.getenv('TOKEN')

    if not TOKEN:
        print("❌ Error: TOKEN environment variable is not set.")
        return

    try:
        print("🔍 Testing bot token...")
        bot = Bot(token=TOKEN)
        me = await bot.get_me()
        print(f"✅ Bot connected successfully!")
        print(f"🤖 Bot name: {me.first_name}")
        print(f"📝 Username: @{me.username if hasattr(me, 'username') and me.username else 'Unknown'}")
        print(f"🆔 Bot ID: {me.id if hasattr(me, 'id') else 'Unknown'}")
        # Get updates to clear any pending ones
        updates = await bot.get_updates(offset=-1)
        print(f"📨 Cleared {len(updates)} pending updates")

        print("\n🎯 Bot is ready! You can now:")
        if hasattr(me, 'username') and me.username:
            print(f"1. Find your bot on Telegram: @{me.username}")
        else:
            print("1. Find your bot on Telegram (username not set)")
        print("2. Start a conversation with it")
        print("3. Send commands like: 'Neo Mode', 'Override Reality', etc.")

    except Exception as e:
        print(f"❌ Error: {e}")
        if "Unauthorized" in str(e):
            print("🔑 Invalid token. Please check your bot token.")
        elif "Conflict" in str(e):
            print("⚠️ Another instance is using this token.")

if __name__ == "__main__":
    asyncio.run(test_bot())
