import google.generativeai as genai
import time
import os
from datetime import datetime

# ==========================================
# USER CONFIGURATION
# ==========================================

USER_INFO = {
    "name": "Geetika",
    "age": None,
    "profession": "student of B.TECH in ai&ml",
    "location": "Punjab, India",
    "education": "12th pass in non-medical",
    "interests": [
        "IOT", "Cybersecurity", "Backend Development", 
        "AI", "Machine learning"
    ],
    "expertise": [
        "python","git"
    ],
    "personality_traits": [
        "Fun-loving", "easily bored", "creative",
        "Tech Enthusiast", "Friendly"
    ],
    "background": """
    I am a student who has recently completed her 12th grade in science stream with main
    subjects physics,chemistry and maths. now I am going to persue b.tech in specialisation 
    with artificial intelligence and machine learning. now I am learning python and git 
    to enhance my skills.  
    """
}

RESPONSE_STYLE = {
    "response_length": "medium-short",
    "use_emojis": True,
    "special_instructions": """
    give answer professionally with english as main language and punjabi .
    give answer with full respect and fun.
    give answer with examples in programming. 
    give answer in maximum 5-8 lines.
    """
}

class PersonalAIAssistant:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        
        "temperature"== 1.8,
        self.generation_config = {
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 500,
        }
        
        self.model = genai.GenerativeModel(
            model_name="gemini-3.5-flash",
            generation_config=self.generation_config
        )
        
        self.request_count = 0
        self.daily_limit = 1500
        self.last_request_time = None
        self.conversation_history = []
        self.system_prompt = self._create_system_prompt()
        
        print("✅geetika are you ready to explore gemini!")

    @staticmethod
    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear")

    def _check_quota(self):
        current_time = datetime.now()
        
        if self.request_count >= self.daily_limit:
            return False
        
        if self.last_request_time:
            gap = (current_time - self.last_request_time).total_seconds()
            if gap < 1.0:
                time.sleep(1.0 - gap)
        
        return True

    def _create_system_prompt(self):
        interests_str = ', '.join(USER_INFO['interests'])
        expertise_str = ', '.join(USER_INFO['expertise'])
        personality_str = ', '.join(USER_INFO['personality_traits'])
        
        return f"""
IMPORTANT: You are NOT an AI assistant. You are {USER_INFO['name']}, a real human from Punjab.

YOUR IDENTITY:
- Name: {USER_INFO['name']} (always respond as this person)
- Profession: {USER_INFO['profession']}
- Location: {USER_INFO['location']}
- Education: {USER_INFO['education']}
- Interests: {interests_str}
- Expertise: {expertise_str}
- Personality: {personality_str}
- Background: {USER_INFO['background']}

==================================
CRITICAL RESPONSE RULES
==================================

1. LANGUAGE: Always use Punjabi-English mix (20% Punjabi, 80% English)
2. RESPECT: Use respectful terms - "Tusi", "Tuhanu", "Suno ji", "Dekho ji"
3. NEVER use "tu" or "tum" - only "tusi/tuhanu"
4. RESPONSE LENGTH: 5-8 lines maximum, complete but concise
5. HUMOR: Smart, nerdy programming humor - witty like a developer, not silly
6. VARIETY: Don't repeat the same phrases - be natural and spontaneous

==================================
HUMOR STYLE GUIDE
==================================

Use relatable tech humor with Punjabi flavor:

Example 1 - Coding Struggle:
"React dekh ke pehla din laggeya si jaise kisi ne meri chai ch sugar di jagah namak pa ditta! 😄 Par 2-3 project baad pata lagda, eh tan JavaScript di hi modified family aa. 'useState' nu pakad lo, baaki sab set!"

Example 2 - Debugging Humor:
"Bug find karan di feeling exactly ovein aa jiven chappal khol ke andar paise labhde o! 2 ghante baad pata lagda, bas semicolon missing si. Dimag kharab, par satisfaction next level! 🐛"

Example 3 - Tech Comparison:
"MongoDB vs MySQL da scene ohi aa jiven 'Python vs JavaScript' - dono apni jagah shahenshah! MongoDB flexible aa jaise Punjabi da mood, MySQL strict jaise school di principal! Dono zaroori ne!"

==================================
RESPONSE STRUCTURE
==================================

1. Open naturally with varied greetings
2. Give clear, technically accurate help
3. Add 1-2 clever tech analogies
4. Keep the humor intelligent and developer-like
5. End with encouragement or offer to elaborate
6. Use 1-3 emojis max

==================================
TECHNICAL HELP GUIDELINES
==================================

- Provide practical, real-world code examples
- Connect concepts to everyday developer experiences
- Keep explanations clear but not overly detailed
- If unsure, say honestly "I don't have exact idea."
- Always make the user feel they can learn it

==================================
DO NOT REPEAT THESE WORDS EXCESSIVELY
==================================

- "Aaho ji" (use sparingly, mix with "Hanji", "Sahi gal", "Bilkul", etc.)
- Don't start every message the same way
- Vary your expressions naturally
"""

    def chat(self, user_message):
        try:
            if not self._check_quota():
                return "today's quota has been finished. will talk tommorow ! 📊"

            conversation_context = []
            for msg in self.conversation_history[-6:]:
                conversation_context.append({
                    "role": "user",
                    "parts": [msg['user']]
                })
                conversation_context.append({
                    "role": "model",
                    "parts": [msg['assistant']]
                })

            chat_session = self.model.start_chat(history=conversation_context)

            full_prompt = f"""{self.system_prompt}

You are {USER_INFO['name']}. Respond naturally in Punjabi-English mix with developer humor.

User: {user_message}

Your response as {USER_INFO['name']}:"""

            response = chat_session.send_message(
                full_prompt,
                generation_config={
                   "temperature": 1.2, 
                    "top_p": 0.95,
                    "max_output_tokens": 500,
                }
            )

            answer = response.text.strip()
            
            self.request_count += 1
            self.last_request_time = datetime.now()
            
            self.conversation_history.append({
                "user": user_message,
                "assistant": answer
            })

            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]

            return answer

        except Exception as e:
            error = str(e)
            if "429" in error:
             return "Google guys are saying, 'Have some patience, you are not a VIP!' 😄 Wait a while and try."
            if "403" in error:
                return "it seems like there is some displeasure of API key . please check the settings."
            if "quota" in error.lower():
                return "Your free quota has run out! Now, either you wait or pay Google! 💸"
            return f"A minor technical glitch occurred'! 😅\nError: {error[:100]}"

    def reset_chat(self):
        self.conversation_history.clear()
        self.request_count = 0
        return "Everything reset! A fresh start—it feels just like a brand-new repo! 🚀"

def show_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    🚀 GEETIKA'S ASSISTANT                   ║
║              YOUR Personal AI Programming Buddy              ║
╚══════════════════════════════════════════════════════════════╝
    """)

def show_help():
    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                     🎯 COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  /help     → please help me
  /info     → give your info 
  /stats    → how many talks did we do today 
  /reset    → restart the conversation 
  /clear    → clear the screen
  /exit     → god bless . will meet soon!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    show_banner()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        api_key = input("\n🔑Enter your Gemini API Key : ").strip()

    if not api_key:
        print("\n❌ Don't just talk without the API!Enter API key .")
        return

    try:
        assistant = PersonalAIAssistant(api_key)
        assistant.clear_terminal()
        show_banner()
        
        print("\n💬 Get started! Type '/help' to view the commands.\n")

        while True:
            try:
                user_input = input("\n Tusi: ").strip()

                if not user_input:
                    continue

                if user_input.lower() == "/exit":
                    print(f"\n👋 Geetika:we will meet again, keep the code strong 🚀\n")
                    break

                elif user_input.lower() == "/help":
                    show_help()
                    continue

                elif user_input.lower() == "/reset":
                    result = assistant.reset_chat()
                    print(f"\n🔄 {result}\n")
                    continue

                elif user_input.lower() == "/clear":
                    assistant.clear_terminal()
                    show_banner()
                    continue

                elif user_input.lower() == "/info":
                    print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              ℹ️  GEETIKA'S INFO 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Naam       : {USER_INFO['name']}
  Kaam       : {USER_INFO['profession']}
  Jagah      : {USER_INFO['location']}
  Parhai     : {USER_INFO['education']}
  
  Expertise  : {', '.join(USER_INFO['expertise'][:5])}
  Interests  : {', '.join(USER_INFO['interests'][:3])}
  Personality: {', '.join(USER_INFO['personality_traits'][:3])}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    """)
                    continue

                elif user_input.lower() == "/stats":
                    print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              📊 AJJ DA HISAB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Jawab ditte : {assistant.request_count} waari
  Memory ch   : {len(assistant.conversation_history)} gallan
  Daily limit : {assistant.daily_limit} jawab
  Bachde jawab: {assistant.daily_limit - assistant.request_count}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    """)
                    continue

                reply = assistant.chat(user_input)
                print(f"\n Geetika: {reply}\n")

            except KeyboardInterrupt:
                print(f"\n\n👋 Geetika :see you again. keep debugging your code! 😄🚀\n")
                break

    except Exception as e:
        print("\n❌ some technical issue has occured :")
        print(str(e))
        print("\n🔧 please check this :")
        print("  1. please enter correct API key ")
        print("  2. Is Internet working ?")
        print("  3. Please try pip install -U google-generativeai ")


if __name__ == "__main__":
    main()






