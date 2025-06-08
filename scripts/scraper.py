from datetime import datetime
from typing import Dict, List

from google_play_scraper import reviews, Sort
import pandas as pd
from tqdm import tqdm


class PlayStoreScraper:
    """Pull N reviews per Android package and return a single DataFrame."""

    def __init__(self, packages: Dict[str, str], per_bank: int = 400):
        self.packages = packages
        self.per_bank = per_bank

    def _fetch_bank(self, bank: str, package: str) -> List[dict]:
        """Scrape one bank and return a list of review JSON blobs."""
        rows, _ = reviews(
            package,
            lang="en",              # captures both English + transliterated Amharic
            count=self.per_bank,
            sort=Sort.NEWEST
        )
        for r in rows:
            r["bank"] = bank
            r["source"] = "Google Play"
        return rows

    def run(self) -> pd.DataFrame:
        """Scrape all banks and yield a tidy DataFrame."""
        all_rows = []
        for bank, pkg in tqdm(
            self.packages.items(), desc="Scraping banks", unit="bank"
        ):
            all_rows.extend(self._fetch_bank(bank, pkg))
        df = pd.DataFrame(all_rows)[["content", "score", "at", "bank", "source"]]
        df.columns = ["review", "rating", "date", "bank", "source"]
        # normalise date to YYYY‑MM‑DD
        df["date"] = pd.to_datetime(df["date"]).dt.date
        return df

    def to_csv(self, df: pd.DataFrame, folder: str = "data") -> str:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"{folder}/reviews_raw_{ts}.csv"
        df.to_csv(path, index=False)
        return path
