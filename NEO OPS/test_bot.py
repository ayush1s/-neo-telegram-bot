import asyncio
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from telegram import Bot

async def test_bot():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    if not TOKEN:
        print("❌ Error: TELEGRAM_BOT_TOKEN environment variable not set.")
        print("Please create a .env file with TELEGRAM_BOT_TOKEN=your_token_here")
        return

    try:
        bot = Bot(token=TOKEN)
        me = await bot.get_me()
        print(f"✅ Bot connected successfully!")
        print(f"🤖 Bot name: {me.first_name}")
        print(f"📝 Username: @{me.username}")
        print(f"🆔 Bot ID: {me.id}")

        # Get updates to clear any pending ones
        updates = await bot.get_updates(offset=-1)
        print(f"📨 Cleared {len(updates)} pending updates")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_bot())
