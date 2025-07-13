import asyncio
# This script quickly tests your Telegram bot token and connection.
# Usage: python quick_test.py
# Make sure to replace TOKEN below with your actual bot token from @BotFather.

try:
    from telegram import Bot
except ImportError:
    print("❌ The 'python-telegram-bot' package is not installed. Please install it with 'pip install python-telegram-bot' and try again.")
    print("💡 If you are using a virtual environment, make sure it is activated. For example:")
    print("   NEO OPS/.venv/Scripts/python.exe -m pip install python-telegram-bot")
    import sys
    sys.exit(1)


# 🔧 REPLACE THIS WITH YOUR BOT TOKEN FROM BOTFATHER
TOKEN = "7840746831:AAF569DMKNhQzEg60DWTW9jz7tRBxO_uZ0U"

async def quick_test():
    if TOKEN == "7840746831:AAF569DMKNhQzEg60DWTW9jz7tRBxO_uZ0U":
        print("❌ Please replace TOKEN with your actual bot token from @BotFather")
        print("📱 Go to Telegram, find @BotFather, and create a new bot with /newbot")
        return
    
    try:
        print("🔍 Testing bot connection...")
        bot = Bot(token=TOKEN)
        me = await bot.get_me()
        
        print("✅ SUCCESS! Bot is working!")
        print(f"🤖 Bot Name: {me.first_name}")
        print(f"📝 Username: @{me.username}")
        print(f"🔗 Link: https://t.me/{me.username}")
        
        print("\n🎯 Next steps:")
        print("1. Click the link above to open your bot")
        print("2. Click 'Start' to begin chatting")
        print("3. Send: 'Neo Mode' to test")
        print("4. Run: python NEO_OPS.py to start the full bot")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if "Unauthorized" in str(e):
            print("🔑 Invalid token. Please check your bot token from @BotFather")

if __name__ == "__main__":
    asyncio.run(quick_test()) 