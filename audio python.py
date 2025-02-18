from gtts import gTTS
import os
from IPython.display import Audio, display

# Define a dictionary to map inputs to responses
responses = {
    "hello": "Hello! How are you?",
    "hi": "Hi! What's up?",
    "how are you": "I'm doing great, thanks!",
    "what's your name": "My name is Python Bot!",
    "goodbye": "Goodbye! See you later!",
    "bye": "Bye! Have a great day!",
    "what is machine learning":"Machine learning is a branch of artificial intelligence that enables computers to learn from data and improve their performance over time without being explicitly programmed.",
    "tell me about data science":"Data science is the interdisciplinary field that extracts insights and knowledge from structured and unstructured data through methods from statistics, computer science, and domain expertise.",
    "what is ai":"Artificial Intelligence (AI) is the simulation of human intelligence in machines designed to perform tasks that typically require human cognition, such as learning, reasoning, and problem-solving.",
}

# Define a function to speak the response
def speak(response):
    try:
        tts = gTTS(text=response, lang='en')
        filename = "response.mp3"
        filepath = os.path.join(os.getcwd(), filename)
        tts.save(filepath)
        display(Audio(filepath,autoplay=True))
    except Exception as e:
        print(f"Error: {e}")

# Define the main function
def main():
    while True:
        try:
            user_input = input("user: ")
            user_input = user_input.lower()
            if user_input in responses:
                speak(responses[user_input])
            else:
                speak("I didn't understand that. Try again!")
        except Exception as e:
            print(f"Error: {e}")

# Run the main function
main()