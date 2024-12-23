import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "How can I help you today?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["Sorry, I didn't understand that.", "Can you please rephrase?", "I'm not sure what you mean."]
}

# Predefined patterns to identify user input
patterns = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "bye": ["bye", "goodbye", "see you", "later"],
    "thanks": ["thank you", "thanks", "thx"],
}

# Function to clean and process user input
def process_input(user_input):
    # Convert input to lowercase
    user_input = user_input.lower()

    # Remove punctuation
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the input (break it into words)
    words = word_tokenize(user_input)

    # Remove stopwords (common words like 'is', 'the', 'a' that don't carry much meaning)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return words

# Function to match user input to predefined patterns
def get_response(user_input):
    words = process_input(user_input)

    # Check for matching patterns
    for category, pattern_list in patterns.items():
        for pattern in pattern_list:
            if pattern in words:
                # Return a random response from the matching category
                return random.choice(responses[category])

    # If no match, return a default response
    return random.choice(responses["default"])

# Chatbot loop
def chat():
    print("Chatbot: Hi! I am a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # If user types 'exit', stop the conversation
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Get the response based on user input
        response = get_response(user_input)
        
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
