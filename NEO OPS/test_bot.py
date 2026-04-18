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
