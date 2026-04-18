# 🔧 How to Get a Working Bot Token

## 📱 Step-by-Step Solution

### Step 1: Open Telegram
1. Open Telegram on your phone or computer
2. Make sure you're logged in

### Step 2: Find BotFather
1. In the search bar, type: `@BotFather`
2. Click on the official BotFather (blue checkmark)
3. Click "Start" or send `/start`

### Step 3: Create a New Bot
1. Send: `/newbot`
2. BotFather will ask for a name
3. Type: `NEO Evolution Bot`
4. BotFather will ask for a username
5. Type: `your_neo_bot_2024` (must end with "bot" and be unique)

### Step 4: Get Your Token
BotFather will respond with something like:
```
Done! Congratulations on your new bot. You will find it at t.me/your_neo_bot_2024

Use this token to access the HTTP API:
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

Keep your token secure and store it safely, it can be used by anyone to control your bot.
```

### Step 5: Copy the Token
Copy ONLY the token part: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Step 6: Update Your Environment
Create a file named `.env` in the `NEO OPS` directory and add your token:
```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### Step 7: Test
Run: `python NEO_OPS.py`

## 🔍 Token Format Check
A valid token should:
- Start with numbers (like: 1234567890)
- Have a colon (:)
- End with letters/numbers (like: ABCdefGHIjklMNOpqrsTUVwxyz)
- Be about 45-50 characters total

## ❌ Common Mistakes
- Copying extra spaces
- Not copying the full token
- Using an old/revoked token
- Getting token from wrong source

## ✅ Success Indicators
When you run `python NEO_OPS.py`, you should see:
```
🚀 Initializing NEO Bot...
🤖 NEO Bot Online. Awaiting Commands...
💡 Try sending: 'Neo Mode', 'Override Reality', 'Command Protocol Activate', etc.
🔄 Starting polling...
```

## 🆘 If Still Not Working
1. Try creating a completely new bot
2. Make sure you're using the official @BotFather
3. Check that the bot wasn't deleted
4. Try the token in a different script first
