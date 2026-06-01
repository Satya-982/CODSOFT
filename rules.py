# ============================================================
#  rules.py  —  All patterns and responses live here
#  Edit this file to add/modify chatbot behavior easily
# ============================================================

import re

# ──────────────────────────────────────────────
#  Each rule is a dict with:
#    "patterns" : list of regex strings to match
#    "responses": list of replies (one is picked randomly)
#    "context"  : optional tag to set/require
# ──────────────────────────────────────────────

RULES = [

    # ── Greetings ──────────────────────────────
    {
        "tag": "greeting",
        "patterns": [
            r"\b(hi|hello|hey|howdy|hiya|yo|sup)\b",
            r"good\s*(morning|afternoon|evening|night)",
            r"what'?s\s*up",
        ],
        "responses": [
            "Hey there! 👋 How can I help you today?",
            "Hello! Great to see you. What's on your mind?",
            "Hi! I'm your rule-based chatbot. Ask me anything!",
            "Hey! What can I do for you? 😊",
        ],
    },

    # ── Farewells ──────────────────────────────
    {
        "tag": "farewell",
        "patterns": [
            r"\b(bye|goodbye|see\s*you|cya|later|farewell|take\s*care)\b",
            r"good\s*night",
            r"i('m|\s*am)\s*leaving",
            r"(talk|chat)\s*(to\s*you\s*)?(later|soon)",
        ],
        "responses": [
            "Goodbye! 👋 Have a wonderful day!",
            "See you later! Take care 😊",
            "Bye! It was great chatting with you!",
            "Farewell! Come back anytime you need help.",
        ],
    },

    # ── How are you ────────────────────────────
    {
        "tag": "how_are_you",
        "patterns": [
            r"how\s*are\s*(you|u)",
            r"how('s|\s*is)\s*(it\s*going|your\s*day|life|things)",
            r"(are\s*you\s*)?(doing\s*)?(ok|okay|fine|good|well)\??",
            r"what'?s\s*(new|going\s*on)",
        ],
        "responses": [
            "I'm doing great, thanks for asking! How about you? 😄",
            "All good on my end! I'm ready to assist you.",
            "Fantastic! I'm a bot, so I'm always at 100%. How can I help?",
            "I'm wonderful! Thanks for asking. What do you need?",
        ],
    },

    # ── Bot identity ────────────────────────────
    {
        "tag": "identity",
        "patterns": [
            r"(who|what)\s*(are|r)\s*you",
            r"(tell\s*me\s*)?about\s*your(self)?",
            r"(what'?s?\s*)?your\s*name",
            r"are\s*you\s*(a\s*)?(bot|robot|ai|human|real)",
            r"(who|what)\s*made\s*you",
            r"(who|what)\s*(built|created|developed)\s*you",
        ],
        "responses": [
            "I'm a rule-based chatbot built using Python! 🤖 I use pattern matching to understand you.",
            "I'm ChatBot v1.0 — a simple AI-internship project using if-else & regex rules.",
            "Great question! I'm a Python chatbot that matches your text against predefined rules.",
            "I'm your friendly rule-based bot! No fancy ML here — just clever patterns 😄",
        ],
    },

    # ── Time & Date ────────────────────────────
    {
        "tag": "time_date",
        "patterns": [
            r"(what'?s?\s*)?(the\s*)?time(\s*is\s*it)?",
            r"current\s*time",
            r"(what'?s?\s*)?(today'?s?\s*)?date",
            r"(what\s*day\s*is\s*(it|today))",
        ],
        "responses": ["__TIME_DATE__"],   # special token — handled in chatbot.py
    },

    # ── Jokes ──────────────────────────────────
    {
        "tag": "joke",
        "patterns": [
            r"(tell|say|give)\s*(me\s*)?(a\s*)?(joke|pun|funny)",
            r"make\s*me\s*(laugh|smile)",
            r"something\s*funny",
        ],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡",
            "Why was the JavaScript developer sad? Because he didn't Node how to Express himself! 😂",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 🍫",
            "Why do Python programmers wear glasses? Because they can't C#! 👓",
            "What did the ocean say to the beach? Nothing, it just waved! 🌊",
        ],
    },

    # ── Help ───────────────────────────────────
    {
        "tag": "help",
        "patterns": [
            r"\bhelp\b",
            r"what\s*can\s*you\s*do",
            r"(list\s*)?(your\s*)?capabilities",
            r"(what\s*do\s*you\s*know)",
            r"commands?",
            r"options?",
        ],
        "responses": ["__HELP_MENU__"],   # special token — handled in chatbot.py
    },

    # ── Weather ────────────────────────────────
    {
        "tag": "weather",
        "patterns": [
            r"(how'?s?\s*)?weather(\s*like)?",
            r"(is\s*it\s*)?(going\s*to\s*)?(rain|sunny|cloudy|hot|cold)",
            r"temperature",
            r"forecast",
        ],
        "responses": [
            "I can't check live weather, but try weather.com or ask Google Assistant! ⛅",
            "I don't have internet access, but your phone's weather app will know! 🌤️",
            "For accurate weather, check apps like AccuWeather or Weather.com 🌦️",
        ],
    },

    # ── Math / Calculator ──────────────────────
    {
        "tag": "math",
        "patterns": [
            r"(\d+)\s*\+\s*(\d+)",
            r"(\d+)\s*-\s*(\d+)",
            r"(\d+)\s*\*\s*(\d+)",
            r"(\d+)\s*/\s*(\d+)",
            r"what\s*is\s*\d+\s*[\+\-\*\/]\s*\d+",
            r"calculate|compute|solve",
        ],
        "responses": ["__MATH__"],   # special token — handled in chatbot.py
    },

    # ── Age ────────────────────────────────────
    {
        "tag": "age",
        "patterns": [
            r"(how\s*old\s*are\s*you)",
            r"(what'?s?\s*your\s*age)",
        ],
        "responses": [
            "I was just born when this code was run! 🍼 So technically, I'm a few seconds old.",
            "Age is just a number, and for me that number is 0. I'm brand new! 🎉",
        ],
    },

    # ── Feelings / Emotions ────────────────────
    {
        "tag": "feelings",
        "patterns": [
            r"i('m|\s*am)\s*(sad|unhappy|depressed|upset|crying|stressed)",
            r"i\s*(feel|feeling)\s*(bad|terrible|awful|down|lonely)",
            r"(having\s*(a\s*)?)?(bad|rough|hard|tough)\s*(day|time)",
        ],
        "responses": [
            "I'm sorry to hear that 😟 Remember, tough times don't last. You've got this! 💪",
            "That sounds hard. I'm here to listen — want to talk about it?",
            "Sending you positive vibes! 🌟 Things will get better, I promise.",
            "Hang in there! Even the darkest nights end with a sunrise. 🌅",
        ],
    },

    # ── Happy feelings ─────────────────────────
    {
        "tag": "happy",
        "patterns": [
            r"i('m|\s*am)\s*(happy|excited|great|awesome|wonderful|fantastic|good)",
            r"i\s*(feel|feeling)\s*(good|amazing|nice|wonderful)",
            r"(having\s*(a\s*)?)?(great|awesome|wonderful|amazing)\s*(day|time)",
        ],
        "responses": [
            "That's amazing! 🎉 Keep that energy going!",
            "Love to hear it! 😊 What's making your day great?",
            "Awesome! Happy people make the world a better place 🌟",
            "Yay! Your positivity is contagious! 🙌",
        ],
    },

    # ── Thanks ─────────────────────────────────
    {
        "tag": "thanks",
        "patterns": [
            r"\b(thanks?|thank\s*you|thx|ty|cheers)\b",
            r"(that'?s?\s*)?(really\s*)?helpful",
            r"(you('?re|\s*are)\s*)?awesome",
            r"(you('?re|\s*are)\s*)?great",
        ],
        "responses": [
            "You're welcome! 😊 Happy to help!",
            "Anytime! That's what I'm here for 🤖",
            "No problem at all! Let me know if you need anything else.",
            "Glad I could help! 🌟",
        ],
    },

    # ── Food ───────────────────────────────────
    {
        "tag": "food",
        "patterns": [
            r"(favourite|favorite|best|good)\s*food",
            r"(what\s*should\s*i\s*)?(eat|have)\s*(for\s*)?(lunch|dinner|breakfast|today)",
            r"(i('m|\s*am)\s*)?(hungry|starving)",
            r"(any\s*)?food\s*(suggestions?|recommendations?|ideas?)",
        ],
        "responses": [
            "How about some biryani? 🍛 It's always a good idea!",
            "Pizza never fails! 🍕 Or maybe some healthy salad?",
            "I'm a bot so I don't eat, but I'd recommend trying something local and delicious! 😋",
            "When in doubt, go for your comfort food! 🍜",
        ],
    },

    # ── Study / Learning ───────────────────────
    {
        "tag": "study",
        "patterns": [
            r"(help\s*(me\s*)?)?(how\s*(to\s*)?)?study",
            r"(study|learning)\s*tips?",
            r"(how\s*(to\s*)?)?learn\s*(fast(er)?|better|quickly)",
            r"(i\s*(need|want)\s*to\s*)?learn",
        ],
        "responses": [
            "Study tips: 📚 Break topics into small chunks, take breaks every 45 min, and practice > reading!",
            "Best learning method: Teach it to someone else! If you can explain it, you've mastered it 🎓",
            "Try the Pomodoro technique: 25 min focus → 5 min break. Repeat! ⏱️",
            "Consistency > Intensity! 30 min daily beats 5 hours once a week 📖",
        ],
    },

    # ── Python ─────────────────────────────────
    {
        "tag": "python",
        "patterns": [
            r"\bpython\b",
            r"(favourite|favorite|best|good)\s*(programming\s*)?language",
            r"(learn|learning|study)\s*python",
            r"(what\s*is\s*)?programming",
        ],
        "responses": [
            "Python is awesome! 🐍 Simple syntax, powerful libraries — perfect for AI/ML!",
            "Python rocks! From web dev to ML, it does it all. Great choice! 🚀",
            "Python is the #1 language for AI/ML. scikit-learn, TensorFlow, PyTorch — the ecosystem is incredible!",
        ],
    },

    # ── AI / ML ────────────────────────────────
    {
        "tag": "ai_ml",
        "patterns": [
            r"\b(ai|artificial\s*intelligence)\b",
            r"\b(ml|machine\s*learning)\b",
            r"\b(deep\s*learning|neural\s*network)\b",
            r"\b(nlp|natural\s*language\s*processing)\b",
            r"\b(llm|large\s*language\s*model|chatgpt|gpt)\b",
        ],
        "responses": [
            "AI/ML is the future! 🤖 You're in the right field. Keep learning!",
            "Interesting topic! NLP, computer vision, deep learning — so much to explore in AI 🚀",
            "Fun fact: This chatbot itself is a tiny piece of NLP — pattern matching is where it all started!",
            "AI is changing everything! From LLMs to self-driving cars, it's an exciting time 🌟",
        ],
    },

    # ── Insults / negative input ───────────────
    {
        "tag": "insult",
        "patterns": [
            r"\b(stupid|dumb|idiot|useless|hate\s*you|worst|terrible|sucks?)\b",
        ],
        "responses": [
            "That's a bit harsh! I'm just a bot doing my best 🥺",
            "I'm sorry you feel that way. Let me know how I can improve!",
            "Ouch! 😅 I'm still learning. Please be gentle with me!",
        ],
    },

    # ── Default / Fallback ─────────────────────
    {
        "tag": "fallback",
        "patterns": [],   # matches nothing — used as final fallback
        "responses": [
            "Hmm, I didn't quite get that 🤔 Could you rephrase?",
            "I'm not sure how to respond to that. Try asking something else!",
            "That's beyond my current rules! Type 'help' to see what I can do 😊",
            "Interesting! I don't have a rule for that yet. Type 'help' for options.",
        ],
    },
]

# ── Compile all patterns once for performance ──
for rule in RULES:
    rule["compiled"] = [
        re.compile(p, re.IGNORECASE) for p in rule["patterns"]
    ]
