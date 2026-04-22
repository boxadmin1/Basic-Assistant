import datetime
import urllib.request
import math
import random
import re

class AI:
    def __init__(self):
        self.name = "AI"
        self.running = True

    def get_weather(self):
        """Fetches live weather using built-in urllib (No pip install)"""
        print(f"[{self.name}]: Accessing atmospheric satellites...")
        try:
            # format=3 gives a clean, one-line plain text response
            url = "https://wttr.in/?format=3"
            with urllib.request.urlopen(url, timeout=5) as response:
                return response.read().decode('utf-8').strip()
        except:
            return "Error: Unable to reach weather service. Check internet connection."

    def solve_math(self, query):
        """Solves math safely using Python's math module"""
        # Clean the string to only allow math-related characters for safety
        expression = re.sub(r'[^0-9+\-*/().% ]', '', query)
        try:
            # We make 'math' functions available inside eval
            result = eval(expression, {"__builtins__": None}, vars(math))
            return f"Calculation Result: {result}"
        except:
            return "Error: Invalid math expression. Use numbers and symbols (+, -, *, /)."

    def process_command(self, user_input):
        cmd = user_input.lower().strip()

        # 1. EXIT
        if cmd in ["exit", "quit", "off", "shutdown"]:
            self.running = False
            return "Systems powering down. Goodbye."

        # 2. HELP
        if "help" in cmd:
            return "Supported: [weather], [time], [date], [math 5+5], [roll dice], [status]"

        # 3. WEATHER
        if "weather" in cmd:
            return self.get_weather()

        # 4. TIME & DATE
        if "time" in cmd:
            return f"Internal Clock: {datetime.datetime.now().strftime('%H:%M:%S')}"
        if "date" in cmd:
            return f"Current Date: {datetime.datetime.now().strftime('%Y-%m-%d')}"

        # 5. MATH
        if "math" in cmd:
            return self.solve_math(cmd.replace("math", ""))

        # 6. FUN / MISC
        if "roll" in cmd or "dice" in cmd:
            return f"Dice Result: {random.randint(1, 6)}"
        
        if "status" in cmd:
            return "System Status: Nominal. Connection: Stable. Dependencies: Zero."

        # 7. DEFAULT
        responses = [
            "Command not recognized. Type 'help' for options.",
            "I'm not programmed for that specific task yet.",
            "Please rephrase. My logic gates are strictly defined."
        ]
        return random.choice(responses)

    def start(self):
        print(f"--- {self.name} SENTINEL v3.0 ---")
        print("Type 'help' to begin.")
        
        while self.running:
            try:
                user_in = input("\n>> ")
                if not user_in: continue
                
                response = self.process_command(user_in)
                print(f"[{self.name}]: {response}")
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    bot = AI()
    bot.start()
