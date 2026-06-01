# ============================================================
#  chatbot.py  —  Core engine: matching + response logic
# ============================================================

import re
import random
import datetime
from rules import RULES

# ── Colour helpers (works on Windows 10+, macOS, Linux) ────
class Color:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BLUE   = "\033[94m"
    MAGENTA= "\033[95m"

# ── Help menu text ──────────────────────────────────────────
HELP_TEXT = f"""
{Color.CYAN}{Color.BOLD}╔══════════════════════════════════════════╗
║          🤖  CHATBOT HELP MENU           ║
╠══════════════════════════════════════════╣
║  💬 Greetings     → hi, hello, hey       ║
║  👋 Farewells     → bye, goodbye         ║
║  😄 How are you   → how are you          ║
║  🤖 Bot info      → who are you          ║
║  🕐 Time/Date     → what time is it      ║
║  😂 Jokes         → tell me a joke       ║
║  🧮 Math          → 25 + 37, 10 * 5      ║
║  🌤️  Weather       → how's the weather    ║
║  😊 Feelings      → I'm happy / sad      ║
║  🙏 Thanks        → thank you            ║
║  🍕 Food          → I'm hungry           ║
║  📚 Study         → study tips           ║
║  🐍 Python        → tell me about Python ║
║  🤖 AI/ML         → what is AI           ║
║  ❌ Quit          → quit / exit / q      ║
╚══════════════════════════════════════════╝{Color.RESET}"""


def evaluate_math(user_input: str) -> str | None:
    """
    Safely evaluate simple arithmetic expressions found in user_input.
    Returns a string answer or None if no valid expression is found.
    """
    # Extract expression like  25 + 37,  100 / 4,  etc.
    expr_match = re.search(r"(\d+\.?\d*)\s*([\+\-\*\/])\s*(\d+\.?\d*)", user_input)
    if not expr_match:
        return None
    a   = float(expr_match.group(1))
    op  = expr_match.group(2)
    b   = float(expr_match.group(3))

    if op == "+" : result = a + b
    elif op == "-": result = a - b
    elif op == "*": result = a * b
    elif op == "/":
        if b == 0:
            return "❌ Division by zero is not allowed!"
        result = a / b

    # Show as int if no decimal needed
    if result == int(result):
        return f"🧮 {int(a)} {op} {int(b)} = {Color.YELLOW}{Color.BOLD}{int(result)}{Color.RESET}"
    return f"🧮 {a} {op} {b} = {Color.YELLOW}{Color.BOLD}{result:.4f}{Color.RESET}"


def get_time_date() -> str:
    now = datetime.datetime.now()
    return (
        f"🕐 Current time : {Color.YELLOW}{Color.BOLD}{now.strftime('%I:%M %p')}{Color.RESET}\n"
        f"📅 Today's date : {Color.YELLOW}{Color.BOLD}{now.strftime('%A, %d %B %Y')}{Color.RESET}"
    )


def match_rule(user_input: str) -> dict:
    """
    Walk through RULES in order and return the first matching rule.
    Falls back to the 'fallback' rule if nothing matches.
    """
    fallback_rule = None

    for rule in RULES:
        if rule["tag"] == "fallback":
            fallback_rule = rule
            continue
        for pattern in rule["compiled"]:
            if pattern.search(user_input):
                return rule

    return fallback_rule


def get_response(user_input: str) -> str:
    """
    Main response function.
    1. Match input against rules
    2. Handle special tokens (__MATH__, __TIME_DATE__, __HELP_MENU__)
    3. Return a random response from the matched rule
    """
    stripped = user_input.strip()
    if not stripped:
        return "Please type something! 😊"

    rule = match_rule(stripped)
    response = random.choice(rule["responses"])

    # ── Handle special tokens ──────────────────
    if response == "__MATH__":
        math_result = evaluate_math(stripped)
        if math_result:
            return math_result
        return "Please give me a math expression like  10 + 5  or  100 / 4 🧮"

    if response == "__TIME_DATE__":
        return get_time_date()

    if response == "__HELP_MENU__":
        return HELP_TEXT

    return response
