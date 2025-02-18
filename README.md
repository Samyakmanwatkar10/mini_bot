# mini_bot

This Python-based chatbot is designed to interact with users in a conversational manner, providing responses based on a pre-defined text document. The chatbot leverages **Natural Language Processing (NLP)** techniques to understand and generate human-like replies. It's capable of handling basic conversational queries, including greetings and general AI-related topics.

### Features:

1. **Greeting Detection:**
   - The chatbot recognizes common greetings such as "hello", "hi", "hey", and "what's up". It responds with a variety of friendly responses, making the conversation more interactive and natural.

2. **Natural Language Processing (NLP):**
   - **Tokenization:** The bot breaks the input text into sentences and words, which is crucial for understanding the structure of language.
   - **Lemmatization:** Using the **NLTK** library, the bot reduces words to their root form (e.g., "running" becomes "run"), which helps it understand variations of words.
   - **Stop Words Removal:** Common words like "is", "and", "the" are ignored to improve the relevance of the text.

3. **Response Generation:**
   - The chatbot generates responses by comparing the user's input to a stored document using **TF-IDF vectorization** and **cosine similarity**. The document (`chatbot.txt`) is analyzed, and the chatbot looks for the most similar sentences to respond with.
   - **Cosine Similarity:** This is a measure used to compare the input sentence with the sentences in the document and find the closest match. If no match is found, the bot will apologize and indicate that it doesn’t understand the query.

4. **Contextual Interaction:**
   - **Dynamic Response:** The bot continuously learns from the ongoing conversation by appending the user’s input to the document (temporarily) and then removing it after generating a response. This ensures that each query is analyzed in the context of the conversation.
   - **Exit Conditions:** The conversation ends if the user types "bye", expresses gratitude (e.g., "thank you"), or asks how the bot is doing (e.g., "how are you?").

5. **Customizable Knowledge Base:**
   - The bot uses a custom text file (`chatbot.txt`) that contains the information or knowledge it can reference to generate answers. You can update or expand this document to provide new information that the bot can use.

### Technologies Used:

1. **Python:** The programming language used for building the chatbot.
2. **NLTK (Natural Language Toolkit):** A powerful library for text processing and NLP tasks. It is used for tokenization, lemmatization, and downloading necessary datasets.
3. **Scikit-learn:** A machine learning library for Python that provides the **TfidfVectorizer** and **cosine_similarity** functions to handle text vectorization and similarity computation.
4. **Random:** Used for selecting random greeting responses.

### Installation Instructions:

To run this chatbot, you will need Python installed on your machine, along with the following libraries:
- **numpy**
- **nltk**
- **scikit-learn**

You can install these dependencies via `pip` by running the following commands in your terminal or command prompt:

```bash
pip install numpy
pip install nltk
pip install scikit-learn
```

You also need to download some essential NLTK datasets, which are handled within the script:

```python
nltk.download('punkt')
nltk.download('wordnet')
```

### How to Run the Chatbot:

1. Ensure you have the necessary libraries installed (refer to the installation instructions above).
2. Create or download the `chatbot.txt` file that contains the knowledge the bot will reference for generating responses.
3. Place the `chatbot.txt` file in the appropriate directory (in the code, it is loaded from `'J:/New folder/chatbot.txt'`).
4. Run the script, and it will prompt you for input. You can start the conversation by typing a sentence, and the bot will respond accordingly.

Example of a conversation:

```
BOT: My name is Mini Bot, I can help you with any AI related term, Let's have a conversation!
You: Hello
BOT: hi
You: What is Deep Learning?
BOT: Deep learning is a subset of machine learning that focuses on using artificial neural networks...
You: How are you?
BOT: I am awesome
You: Thank you!
BOT: You're welcome!
```

### Customization:

- **Custom Responses:** You can easily extend the bot’s functionality by adding new response patterns and adding more knowledge to the `chatbot.txt` document.
- **Additional NLP Features:** You could integrate other NLP techniques like named entity recognition (NER) or sentiment analysis to make the chatbot more sophisticated.

### Limitations:

- **Simple Document-based Response:** This chatbot only generates responses based on the text document provided. It does not handle dynamic conversations or continuously learn from real-time interactions (apart from the temporary context during the conversation).
- **Limited Understanding:** While the chatbot uses cosine similarity for response matching, it does not understand the content deeply and may fail to provide appropriate responses if the input is very different from the document's content.

### Future Improvements:

- **Machine Learning Integration:** Add a machine learning model to allow the chatbot to generate more accurate responses based on previous conversations or learning from new data.
- **User Intent Recognition:** Incorporate more advanced intent recognition to understand user queries more accurately (e.g., using a classifier like Naive Bayes or Support Vector Machines).
- **Voice Interaction:** Enable voice-based input and output for a more interactive experience.
