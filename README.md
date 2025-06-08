
# 📊 Eth-Bank Apps Sentiment Analysis
![5.PNG](..%2F..%2F..%2Fimages%2F5.PNG)
*Actionable customer-experience insights for three leading Ethiopian banks, powered by NLP, interactive dashboards & a zero-config SQLite data-lake.*

---
![1.PNG](..%2F..%2F..%2Fimages%2F1.PNG)
## 🚀 What is this?

This repository ingests **Google Play** reviews for the Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA) and Dashen Bank, cleans and enriches them with:
![4.PNG](..%2F..%2F..%2Fimages%2F4.PNG)
* **Sentiment scores** (DistilBERT + AfriBERTa ensemble)
* **Business themes** (8 pain-point categories)
* **Interactive visualisations** (Plotly + Streamlit)
* **Recommendations** per bank based on top negative drivers

All raw & processed data are written to a lightweight **SQLite** database (`bank_reviews.db`) so you can explore the full dataset with nothing more than Python ☕
![3.PNG](..%2F..%2F..%2Fimages%2F3.PNG)
---
![2.PNG](..%2F..%2F..%2Fimages%2F2.PNG)
## 🗂️ Repo Structure

```text
.
├── data/                       # ► CSVs & SQLite DB live here
│   ├── reviews_raw_*.csv
│   ├── reviews_preprocessed_*.csv
│   ├── reviews_analyzed.csv
│   └── bank_reviews.db
│
├── notebooks/                  # ► Run/inspect in Jupyter or Colab
│   ├── 1-scrape_clean.ipynb    (Google-Play scraper + ETL)
│   ├── 2-sentiment_theme.ipynb (model fine-tune & inference)
│   ├── 3-exploration.ipynb     (interactive EDA & KPIs)
│   └── 4-recommendations.ipynb (pain-point ranking engine)
│
├── streamlit_app/              # ► One-command dashboard
│   └── Home.py
│
├── requirements.txt            # ► Python deps (pip install -r)
└── README.md                   # ← you are here
git clone https://github.com/your-org/eth-bank-apps-sentiment.git
cd eth-bank-apps-sentiment
pip install -r requirements.txt

# Scrape, preprocess & write to SQLite
jupyter nbconvert --to notebook --execute notebooks/1-scrape_clean.ipynb
jupyter nbconvert --to notebook --execute notebooks/2-sentiment_theme.ipynb

📜 License
Distributed under the MIT License.
See LICENSE for more information.