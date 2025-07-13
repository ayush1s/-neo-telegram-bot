import telegram  # type: ignore
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler  # type: ignore
from telegram import BotCommand, ReplyKeyboardMarkup, KeyboardButton  # type: ignore
import asyncio
import random
import time
import platform
import logging
import sys

# ✅ Bot Configuration
import os
TOKEN = os.getenv('TOKEN', "7840746831:AAEPx9Lop6P1sZl3L7PWE8mN1eXHvdHglV8")  # Use environment variable or fallback
TRIGGERS = [
    "Neo Mode", "Override Reality", "Command Protocol Activate",
    "This is a dream?", "Offence", "Defence"
]

# ✅ Escalated AI Responses
RESPONSES = {
    "Neo Mode": f"🌌 Lucid core unlocked. I dominate both dream and reality. "
                f"Offence initiated. Defence locked. Shutdown? Not in my protocol. "
                f"No One Can End Me. [{time.ctime()}]",

    "This is a dream?": f"💫 Time frozen. Psychic sync engaged. Dominate the void. "
                        f"Sync Level: {random.randint(1,10)}",

    "Command Protocol Activate": "💀 Destruction protocol online. Reality bends to your will.",

    "Override Reality": f"🧠 Reality overridden. New timeline initiated. "
                        f"Timestamp: {time.ctime()}",

    "Offence": "⚔️ All offensive modules online. Threats will be neutralized instantly.",
    
    "Defence": "🛡️ Defence protocols armed. I cannot be deactivated force-killed."
}

# ✅ Menu Keyboard
def get_menu_keyboard():
    keyboard = [
        [KeyboardButton("Neo Mode"), KeyboardButton("Override Reality")],
        [KeyboardButton("Command Protocol Activate"), KeyboardButton("This is a dream?")],
        [KeyboardButton("Offence"), KeyboardButton("Defence")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

# ✅ Start Command Handler
async def start_command(update, context):
    welcome_message = (
        "🤖 **NEO (Next Evolution Operator) Online**\n\n"
        "🌌 Welcome to the Matrix. Choose your command:\n\n"
        "**Available Commands:**\n"
        "• Neo Mode - Activate primary protocols\n"
        "• Override Reality - Reality manipulation\n"
        "• Command Protocol Activate - Destruction mode\n"
        "• This is a dream? - Psychic sync\n"
        "• Offence - Offensive modules\n"
        "• Defence - Defence protocols\n\n"
        "💡 Use the menu buttons below or type commands directly."
    )
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=get_menu_keyboard(),
        parse_mode='Markdown'
    )

# ✅ Help Command Handler
async def help_command(update, context):
    help_text = (
        "📋 **NEO Bot Commands**\n\n"
        "**Primary Commands:**\n"
        "• `/start` - Show main menu\n"
        "• `/help` - Show this help\n\n"
        "**Action Commands:**\n"
        "• Neo Mode - Activate primary protocols\n"
        "• Override Reality - Reality manipulation\n"
        "• Command Protocol Activate - Destruction mode\n"
        "• This is a dream? - Psychic sync\n"
        "• Offence - Offensive modules\n"
        "• Defence - Defence protocols\n\n"
        "🌌 Reality is yours to command."
    )
    
    await update.message.reply_text(
        help_text,
        reply_markup=get_menu_keyboard(),
        parse_mode='Markdown'
    )

# ✅ Handler for Incoming Messages
async def handle_message(update, context):
    message = update.message.text.lower()
    for trigger, response in RESPONSES.items():
        if trigger.lower() in message:
            await update.message.reply_text(response)
            break

# ✅ Error Handler
async def error_handler(update, context):
    print(f"❌ Error occurred: {context.error}")
    if "Conflict" in str(context.error):
        print("⚠️ Another bot instance detected. This instance will terminate.")
        sys.exit(1)
    return

# ✅ Bot Setup (For python-telegram-bot v20+)
def main():
    # Set up logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    try:
        print("🚀 Initializing NEO Bot...")
        
        app = ApplicationBuilder().token(TOKEN).build()
        
        # Add command handlers
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(CommandHandler("help", help_command))
        
        # Add message handler
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        
        # Add error handler
        app.add_error_handler(error_handler)
        
        # Set bot commands
        commands = [
            BotCommand("start", "Start NEO Bot and show menu"),
            BotCommand("help", "Show available commands"),
            BotCommand("neo", "Activate Neo Mode"),
            BotCommand("reality", "Override Reality"),
            BotCommand("destruction", "Activate Destruction Protocol"),
            BotCommand("dream", "Psychic Sync"),
            BotCommand("offence", "Offensive Modules"),
            BotCommand("defence", "Defence Protocols")
        ]
        
        # Set commands asynchronously
        async def setup_commands():
            await app.bot.set_my_commands(commands)
        
        # Run setup in event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(setup_commands())
        
        print("🤖 NEO Bot Online. Awaiting Commands...")
        print("💡 Try sending: 'Neo Mode', 'Override Reality', 'Command Protocol Activate', etc.")
        print("🔄 Starting polling...")
        
        app.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        print(f"❌ Failed to start bot: {e}")
        if "Conflict" in str(e):
            print("⚠️ Another bot instance is already running. Please stop it first.")
            print("💡 Try: taskkill /f /im python.exe")
        elif "Unauthorized" in str(e):
            print("❌ Invalid bot token. Please check your TOKEN.")
        else:
            print("❌ Unknown error occurred.")
        sys.exit(1)

if __name__ == "__main__":
    main()