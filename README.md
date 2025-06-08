
# 📊 Eth-Bank Apps Sentiment Analysis
![5](https://github.com/user-attachments/assets/a41b5c9b-9960-4ff5-b61a-74d5265573ce)

*Actionable customer-experience insights for three leading Ethiopian banks, powered by NLP, interactive dashboards & a zero-config SQLite data-lake.*

---![1](https://github.com/user-attachments/assets/7c348e45-656c-4390-90a0-9ac9ae351c92)


## 🚀 What is this?

This repository ingests **Google Play** reviews for the Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA) and Dashen Bank, cleans and enriches them with:
![2](https://github.com/user-attachments/assets/562ae616-22b7-458b-8003-e15480238dfb)

* **Sentiment scores** (DistilBERT + AfriBERTa ensemble)
* **Business themes** (8 pain-point categories)
* **Interactive visualisations** (Plotly + Streamlit)
* **Recommendations** per bank based on top negative drivers
![3](https://github.com/user-attachments/assets/e749d859-5bc6-42bc-a0e6-764a234de109)

All raw & processed data are written to a lightweight **SQLite** database (`bank_reviews.db`) so you can explore the full dataset with nothing more than Python ☕
![3.PNG](..%2F..%2F..%2Fimages%2F3.PNG)
---

## 🗂️ Repo Structure
![4](https://github.com/user-attachments/assets/e30c8d42-8309-456d-88df-1cde2488cf51)

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
