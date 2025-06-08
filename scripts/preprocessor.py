import pandas as pd
import re
from datetime import datetime


class ReviewPreprocessor:
    """Very light cleaning: drop dups, strip whitespace, normalise case."""

    @staticmethod
    def _clean_text(txt: str) -> str:
        txt = txt.strip()
        txt = re.sub(r"\s+", " ", txt)        # collapse spaces/newlines
        return txt

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.drop_duplicates(subset=["review", "rating", "date", "bank"], inplace=True)
        df["review"] = df["review"].astype(str).apply(self._clean_text)
        return df

    def to_csv(self, df: pd.DataFrame, folder: str = "data") -> str:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"{folder}/reviews_preprocessed_{ts}.csv"
        df.to_csv(path, index=False)
        return path
