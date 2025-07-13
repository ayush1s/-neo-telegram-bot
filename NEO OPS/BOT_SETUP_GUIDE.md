# 🤖 How to Create Your Telegram Bot

## Step 1: Create a Bot Token

1. **Open Telegram** and search for `@BotFather`
2. **Start a conversation** with BotFather
3. **Send the command**: `/newbot`
4. **Enter a name** for your bot (e.g., "NEO Bot")
5. **Enter a username** for your bot (e.g., "neo_evolution_bot") - must end with "bot"
6. **Copy the token** that BotFather gives you

## Step 2: Update Your Code

Replace the TOKEN in `NEO_OPS.py` with your new token:

```python
TOKEN = "YOUR_NEW_TOKEN_HERE"  # Replace with the token from BotFather
```

## Step 3: Test Your Bot

1. **Run the test script:**
   ```bash
   python test_new_token.py
   ```

2. **If successful, run the main bot:**
   ```bash
   python NEO_OPS.py
   ```

## Step 4: Use Your Bot

1. **Find your bot** on Telegram using the username you created
2. **Start a conversation** with your bot
3. **Send commands** like:
   - "Neo Mode"
   - "Override Reality"
   - "Command Protocol Activate"
   - "This is a dream?"
   - "Offence"
   - "Defence"

## 🔧 Troubleshooting

### If you get "Unauthorized" error:
- Make sure you copied the token correctly
- Check that there are no extra spaces
- Verify the token starts with numbers and contains a colon

### If you get "Conflict" error:
- Stop any running Python processes: `taskkill /f /im python.exe`
- Wait a few minutes and try again

### If the bot doesn't respond:
- Make sure the bot is running (`python NEO_OPS.py`)
- Check that you sent one of the trigger phrases
- Try sending "Neo Mode" first

## 📱 Example BotFather Conversation

```
You: /newbot
BotFather: Alright, a new bot. How are we going to call it? Please choose a name for your bot.

You: NEO Evolution Bot
BotFather: Good. Now let's choose a username for your bot. It must end in `bot`. Like this: TetrisBot or tetris_bot.

You: neo_evolution_bot
BotFather: Done! Congratulations on your new bot. You will find it at t.me/neo_evolution_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

Keep your token secure and store it safely, it can be used by anyone to control your bot.
``` 