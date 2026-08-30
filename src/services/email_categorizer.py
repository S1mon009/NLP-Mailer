"""
Machine learning-based email categorization.

This module provides the :class:`EmailCategorizer` class, which uses a
TF-IDF vectorizer and a Multinomial Naive Bayes classifier to categorize
emails into predefined categories.

The module also handles text preprocessing, feature extraction, model
training, prediction, and persistence using Python's ``pickle`` module.
"""
import re
import pickle
from typing import Optional, Dict, Any, List, Tuple
from pathlib import Path
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords
from src.config.config import CATEGORIES, MODEL_PATH, get_training_data

# Download NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)


class EmailCategorizer:
    """Machine learning-based email categorizer.

    This class provides functionality for training and using a machine
    learning model to automatically categorize emails. The classification
    pipeline consists of a TF-IDF vectorizer followed by a Multinomial
    Naive Bayes classifier.

    The trained model can be saved to and loaded from disk using the
    configured model path.

    Attributes:
        model_path: Path where the trained model is stored.
        categories: List of available email categories.
        pipeline: Scikit-learn pipeline containing the TF-IDF vectorizer
            and Naive Bayes classifier.
        stop_words: Set of English stop words used during text processing.
    """
    def __init__(self, model_path: Optional[str] = None) -> None:
        """Initialize the email categorizer.

        If a trained model exists at the specified path, it is loaded.
        Otherwise, a new machine learning pipeline is initialized.

        Args:
            model_path: Optional path to the serialized machine learning
                model. If not provided, the default ``MODEL_PATH`` is used.
        """
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

    def _initialize_model(self) -> None:
        """Initialize the machine learning classification pipeline.

        Creates a scikit-learn pipeline consisting of a TF-IDF vectorizer
        and a Multinomial Naive Bayes classifier.

        Returns:
            None.
        """
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000, stop_words='english')),
            ('classifier', MultinomialNB())
        ])

    def preprocess_text(self, text: Any) -> str:
        """
        Clean and normalize email text.

        Removes URLs, email addresses, non-alphabetic characters,
        converts text to lowercase, and normalizes whitespace.

        Args:
            text: Raw email text to preprocess.

        Returns:
            A cleaned and normalized text string.
        """
        text = re.sub(r'http\\S+|www.\\S+', '', text)
        text = re.sub(r'\\S+@\\S+', '', text)
        text = re.sub(r'[^a-zA-Z\\s]', '', text)
        text = text.lower()
        text = ' '.join(text.split())
        return text

    def extract_features(self, email: Dict[str, Any]) -> str:
        """
        Extract and preprocess features from an email.

        Combines the email subject and body into a single text representation
        and passes it through the text preprocessing pipeline.

        Args:
            email: Dictionary containing email data. The expected keys are
                ``subject`` and ``body``.

        Returns:
            Preprocessed text containing the extracted email features.
        """
        subject = email.get('subject', '')
        body = email.get('body', '')
        combined = f"{subject} {subject} {body}"
        return self.preprocess_text(combined)

    def train(self, training_emails: Optional[List[Dict[str, Any]]] = None) -> None:
        """
        Train the email categorization model.

        If no training data is provided, the method loads the configured
        local training dataset using :func:`get_training_data`.

        The extracted email features are used to train the TF-IDF and
        Multinomial Naive Bayes pipeline. After successful training,
        the model is automatically saved to disk.

        Args:
            training_emails: Optional list of email dictionaries containing
                email content and category labels. If ``None``, the training
                data is loaded using :func:`get_training_data`.

        Returns:
            None.
        """
        if training_emails is None:
            training_emails = get_training_data()

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

    def categorize(self, email: Dict[str, Any]) -> Tuple[str, float]:
        """
        Categorize a single email.

        Uses the trained machine learning pipeline to predict the category
        of the provided email and calculates the model's confidence based
        on the highest predicted probability.

        Args:
            email: Dictionary containing the email data. The expected keys
                are ``subject`` and ``body``.

        Returns:
            A tuple containing the predicted category and its confidence
            score. If no pipeline is available, returns ``("Unknown", 0.0)``.
        """
        if not self.pipeline:
            return 'Unknown', 0.0

        text = self.extract_features(email)
        category = self.pipeline.predict([text])[0]
        probabilities = self.pipeline.predict_proba([text])[0]
        confidence = max(probabilities)

        return category, confidence

    def has_category_tag(self, subject: Any) -> bool:
        """
        Check whether an email subject already contains a category tag.

        Category tags are expected to appear at the beginning of the subject
        in square brackets, for example ``[Work]`` or ``[Finance]``.

        Args:
            subject: Email subject to check.

        Returns:
            ``True`` if the subject starts with a recognized category tag,
            otherwise ``False``.
        """
        pattern = r'^\\[(' + '|'.join(self.categories) + r')\\]'
        return bool(re.match(pattern, subject))

    def save_model(self) -> None:
        """
        Save the trained machine learning model to disk.

        Creates the parent directory of the configured model path if it does
        not exist and serializes the current pipeline using ``pickle``.

        Returns:
            None.
        """
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.pipeline, f)
        print(f"Model saved to {self.model_path}")

    def load_model(self) -> None:
        """
        Load a trained machine learning model from disk.

        Attempts to deserialize the model stored at ``model_path``.
        If loading fails, a new untrained machine learning pipeline is
        initialized instead.

        Returns:
            None.
        """
        try:
            with open(self.model_path, 'rb') as f:
                self.pipeline = pickle.load(f)
            print(f"Model loaded from {self.model_path}")
        except Exception as e:
            print(f"Could not load model: {e}")
            self._initialize_model()
