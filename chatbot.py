import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
training_data = {
    "fever": "It looks like you have a fever. Please rest and stay hydrated.",
    "cough": "A cough can be caused by a cold or allergy. Drink warm fluids.",
    "headache": "Headaches can happen due to stress or dehydration. Try relaxing and drink water.",
    "stomach pain": "You may have indigestion. Eat light and avoid spicy food.",
    "cold": "You seem to have a common cold. Rest well and stay warm."
}

# Preprocessing
lemmatizer = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('wordnet')

# Prepare training data
X = list(training_data.keys())
y = list(training_data.values())

vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

def get_response(user_input):
    """Takes user input and returns chatbot response"""
    user_input = user_input.lower()
    input_vector = vectorizer.transform([user_input])
    response = model.predict(input_vector)[0]
    return response
