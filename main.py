import numpy as np
import nltk
import nltk
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess the document
with open('J:/New folder/chatbot.txt', 'r', errors='ignore') as f:
    raw_doc = f.read().lower()

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Tokenize the document
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

# Lemmatization
lemmer = nltk.stem.WordNetLemmatizer()
def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return [lemmer.lemmatize(token) for token in nltk.word_tokenize(text.lower().translate(remove_punct_dict))]

# Greetings
GREET_INPUTS = ("hello", "hi", "hii", "what's up", "hey")
GREET_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad you're talking to me", "Yes, how can I help you?"]

def greet(sentence):
    if any(word.lower() in GREET_INPUTS for word in sentence.split()):
        return random.choice(GREET_RESPONSES)
    return None

# Response generation
def response(user_response):
    sent_tokens.append(user_response)
    tfidf_vec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = tfidf_vec.fit_transform(sent_tokens)
    cosine_sim = cosine_similarity(tfidf[-1], tfidf[:-1])
    sent_tokens.pop()  # Remove the user input from the token list

    if cosine_sim.max() == 0:
        return "I am sorry! I don't understand you."
    else:
        idx = cosine_sim.argmax()
        return sent_tokens[idx]

# Main loop
print("BOT: My name is Mini Bot, I can help you with any AI releated term, Let's have a conversation!")
while True:
    user_response = input("You: ").lower()
    if user_response == 'bye':
        print("BOT: Goodbye!")
        break
    elif user_response == 'how are you':
        print("I am awsome")
        continue
    elif user_response in ('thanks', 'thank you', 'exit'):
        print("BOT: You're welcome!")
        break
    elif greet(user_response):
        print(f"BOT: {greet(user_response)}")
    else:
        print(f"BOT: {response(user_response)}")
