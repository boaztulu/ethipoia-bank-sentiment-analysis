import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

custom_stop_words = list(ENGLISH_STOP_WORDS.union({
    # General app and banking words
    'app', 'application', 'applications', 'apps', 'bank', 'banks', 'banking', 'mobile', 
    'service', 'services', 'user', 'users', 'customer', 'customers', 'ethiopia', 'ethiopian',
    'dashen', 'boa', 'cbe',

    # Common verbs and actions
    'use', 'using', 'used', 'make', 'made', 'update', 'updated', 'updates', 'work', 'working',

    # Generic qualitative terms
    'good', 'great', 'best', 'better', 'nice', 'excellent', 'perfect', 'fine', 'super', 
    'awesome', 'cool', 'wow', 'bad', 'poor', 'worst', 'amazing',

    # Time and frequency
    'time', 'just', 'really', 'always', 'never', 'often', 'sometimes',

    # Technical/common issues
    'slow', 'crash', 'crashes', 'loading', 'lag', 'lagging', 'freeze', 'frozen',
    'error', 'issue', 'issues', 'problem', 'problems', 'doesnt', 'dont',

    # Account access and authentication
    'login', 'log', 'signin', 'sign', 'password', 'authentication', 'fingerprint', 
    'otp', 'code', 'verification',

    # User interface and design
    'easy', 'interface', 'ui', 'design', 'ux', 'navigation', 'layout',

    # Support-related
    'support', 'help', 'customer service', 'call center', 'contact', 'agent', 'staff', 
    'response', 'respond',

    # Feature-related
    'feature', 'features', 'improve', 'improvement', 'suggestion', 'suggestions',

    # Financial terms
    'transaction', 'transactions', 'transfer', 'money', 'payment', 'payments', 'send', 
    'receive', 'balance', 'amount', 'bill', 'charge', 'fee', 'limit', 'statement', 'history',

    # Connectivity terms
    'network', 'internet', 'connection', 'data',

    # Miscellaneous common words
    'version', 'need', 'needs', 'like', 'experience', 'experiences', 'additional', 
    'add', 'added', 'new', 'please', 'kindly', 'thank', 'thanks', 'hi', 'hello'
}))


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_keywords(df, top_n=10):
    # Explicit preprocessing
    df['clean_review'] = df['review'].apply(preprocess)

    # Vectorizer
    vectorizer = TfidfVectorizer(
        stop_words=custom_stop_words,
        max_df=0.7,
        min_df=5,
        ngram_range=(1, 2),
        max_features=100
    )

    X = vectorizer.fit_transform(df['clean_review'])
    feature_names = vectorizer.get_feature_names_out()
    mean_scores = X.mean(axis=0).A1

    indices = mean_scores.argsort()[-top_n:][::-1]

    keywords = [(feature_names[i], mean_scores[i]) for i in indices]
    return keywords


def assign_themes(df, theme_mapping):
    def find_themes(review):
        review_lower = review.lower()
        matched_themes = []
        for theme, keywords in theme_mapping.items():
            if any(keyword.lower() in review_lower for keyword in keywords):
                matched_themes.append(theme)
        return ', '.join(matched_themes) if matched_themes else 'Other'

    df['theme'] = df['review'].apply(find_themes)
    return df
