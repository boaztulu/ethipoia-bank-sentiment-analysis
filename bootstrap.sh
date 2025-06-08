#!/usr/bin/env bash
# ────────────────────────────────────────────────────────────────
#  Bootstrap: creates the directory tree and placeholder files
#              for “Eth-Bank-Apps-Sentiment-Analysis”.
# ────────────────────────────────────────────────────────────────
set -e

root="Eth-Bank-Apps-Sentiment-Analysis"
mkdir -p "$root"/{scripts,notebooks,data,database}

# Script stubs
touch "$root"/scripts/{review_scraper.py,review_preprocessor.py,sentiment_analysis.py,thematic_analysis.py}

# Notebook stubs
for nb in 1-data_collection \
          2-sentiment_thematic_analysis \
          3-database_storage \
          4-insights_recommendations
do
  touch "$root"/notebooks/"$nb".ipynb
done

# Data / DB placeholders
touch "$root"/data/{reviews_raw.csv,reviews_cleaned.csv,reviews_with_sentiment.csv,reviews_analyzed.csv}
touch "$root"/database/bank_reviews_dump.sql

# requirements.txt
cat > "$root"/requirements.txt <<'REQ'
google-play-scraper
pandas
numpy
nltk
textblob
REQ

# .gitignore
cat > "$root"/.gitignore <<'GIT'
# Python
__pycache__/
*.pyc
.venv/

# Jupyter
*.ipynb_checkpoints/

# Data & DB
Eth-Bank-Apps-Sentiment-Analysis/data/
Eth-Bank-Apps-Sentiment-Analysis/database/

# OS / IDE
.DS_Store
.vscode/
GIT

# README
cat > "$root"/README.md <<'MD'
# Ethiopia Bank Sentiment Analysis

Google-Play review scraping and sentiment / thematic analysis for major Ethiopian
banking apps.

## Reproduce environment

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r Eth-Bank-Apps-Sentiment-Analysis/requirements.txt
