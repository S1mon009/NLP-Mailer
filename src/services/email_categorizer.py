import re
import pickle
from pathlib import Path
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords
from src.config.config import CATEGORIES, MODEL_PATH, TRAINING_DATA

# Download NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


class EmailCategorizer:
    '''ML-based email categorizer'''
    
    def __init__(self, model_path=None):
        self.model_path = Path(model_path or MODEL_PATH)
        self.categories = CATEGORIES
        self.pipeline = None
        
        if self.model_path.exists():
            self.load_model()
        else:
            self._initialize_model()
        
        try:
            self.stop_words = set(stopwords.words('english'))
        except:
            self.stop_words = set()
    
    def _initialize_model(self):
        '''Initialize ML pipeline'''
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english')),
            ('classifier', MultinomialNB())
        ])
    
    def preprocess_text(self, text):
        '''Clean and preprocess email text'''
        text = re.sub(r'http\\S+|www.\\S+', '', text)
        text = re.sub(r'\\S+@\\S+', '', text)
        text = re.sub(r'[^a-zA-Z\\s]', '', text)
        text = text.lower()
        text = ' '.join(text.split())
        return text
    
    def extract_features(self, email):
        '''Extract relevant features from email'''
        subject = email.get('subject', '')
        body = email.get('body', '')
        combined = f"{subject} {subject} {body}"
        return self.preprocess_text(combined)
    
    def train(self, training_emails=None):
        '''Train the categorizer'''
        if training_emails is None:
            training_emails = TRAINING_DATA
        
        print(f"Training model with {len(training_emails)} emails...")
        
        texts = [self.extract_features(email) for email in training_emails]
        labels = [email['category'] for email in training_emails]
        
        self.pipeline.fit(texts, labels)
        
        label_counts = Counter(labels)
        print("Training data distribution:")
        for category, count in label_counts.most_common():
            print(f"   • {category}: {count} emails")
        
        print("Model trained successfully")
        self.save_model()
    
    def categorize(self, email):
        '''Categorize a single email'''
        if not self.pipeline:
            return 'Unknown', 0.0
        
        text = self.extract_features(email)
        category = self.pipeline.predict([text])[0]
        probabilities = self.pipeline.predict_proba([text])[0]
        confidence = max(probabilities)
        
        return category, confidence
    
    def has_category_tag(self, subject):
        '''Check if subject already has a category tag'''
        pattern = r'^\\[(' + '|'.join(self.categories) + r')\\]'
        return bool(re.match(pattern, subject))
    
    def save_model(self):
        '''Save trained model'''
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.pipeline, f)
        print(f"Model saved to {self.model_path}")
    
    def load_model(self):
        '''Load trained model'''
        try:
            with open(self.model_path, 'rb') as f:
                self.pipeline = pickle.load(f)
            print(f"Model loaded from {self.model_path}")
        except Exception as e:
            print(f"Could not load model: {e}")
            self._initialize_model()