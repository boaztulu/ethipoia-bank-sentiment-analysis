import pandas as pd
from transformers import pipeline
from tqdm.auto import tqdm

def perform_sentiment_analysis(df, batch_size=100):
    sentiment_pipeline = pipeline(
        "sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    
    sentiments = []
    
    for i in tqdm(range(0, len(df), batch_size), desc="Analyzing sentiment"):
        batch = df['review'].iloc[i:i+batch_size].tolist()
        sentiments.extend(sentiment_pipeline(batch))

    df[['sentiment_label', 'sentiment_score']] = pd.DataFrame(
        [(result['label'], result['score']) for result in sentiments],
        index=df.index
    )
    
    return df
