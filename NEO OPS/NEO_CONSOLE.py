import random
import time
import os

# ✅ Bot Configuration
BOT_NAME = "NEO (Next Evolution Operator)"
VERSION = "1.0.0"

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
    
    "Defence": "🛡️ Defence protocols armed. I cannot be deactivated force-killed.",
    
    "Status": f"🤖 {BOT_NAME} v{VERSION} - All systems operational. "
              f"Core temperature: {random.randint(20, 45)}°C. "
              f"Memory usage: {random.randint(60, 95)}%",
              
    "Help": "📋 Available Commands:\n"
            "  • Neo Mode - Activate primary protocols\n"
            "  • Override Reality - Reality manipulation\n"
            "  • Command Protocol Activate - Destruction mode\n"
            "  • This is a dream? - Psychic sync\n"
            "  • Offence - Offensive modules\n"
            "  • Defence - Defence protocols\n"
            "  • Status - System status\n"
            "  • Help - Show this help\n"
            "  • Exit/Quit - Shutdown"
}

# ✅ Console Interface
def console_interface():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    
    print("🤖" + "="*48 + "🤖")
    print(f"    {BOT_NAME} v{VERSION}")
    print("    Next Evolution Operator for OBLIVION OS")
    print("🤖" + "="*48 + "🤖")
    print()
    print("💡 Type 'help' for available commands")
    print("💡 Type 'exit' or 'quit' to shutdown")
    print()
    
    while True:
        try:
            user_input = input("🔮 NEO> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'shutdown']:
                print("🔄 Shutting down NEO Bot...")
                print("🌌 Reality restored. Goodbye.")
                break
                
            # Check for exact matches first
            if user_input in RESPONSES:
                print(f"🤖 NEO: {RESPONSES[user_input]}")
                continue
                
            # Check for partial matches
            response_found = False
            for trigger, response in RESPONSES.items():
                if trigger.lower() in user_input.lower():
                    print(f"🤖 NEO: {response}")
                    response_found = True
                    break
                    
            if not response_found:
                print("🤖 NEO: Command not recognized. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\n🔄 Shutting down NEO Bot...")
            print("🌌 Reality restored. Goodbye.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# ✅ Main Function
def main():
    print("🚀 Initializing NEO Bot...")
    time.sleep(1)
    print("🔧 Loading core modules...")
    time.sleep(0.5)
    print("⚡ Activating neural networks...")
    time.sleep(0.5)
    print("🌌 Reality interface online...")
    time.sleep(0.5)
    
    console_interface()

if __name__ == "__main__":
    main() 