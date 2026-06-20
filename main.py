import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file")
    print("Please add your API key to the .env file")
    exit(1)

# Configure the Gemini API
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-pro")

def chat_with_gemini(user_message):
    """Send a message to Gemini and get a response"""
    try:
        response = model.generate_content(user_message)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main chat loop"""
    print("=" * 50)
    print("Welcome to Gemini AI Chat!")
    print("Type 'exit' to quit")
    print("=" * 50)
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break
        
        if not user_input:
            continue
        
        print("\nGemini: ", end="")
        response = chat_with_gemini(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()
