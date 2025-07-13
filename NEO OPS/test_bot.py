import asyncio
from telegram import Bot

async def test_bot():
    TOKEN = "7840746831:AAHQl59TUHb_YcMprHLIV0V3kaptQfd2tdM"
    
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