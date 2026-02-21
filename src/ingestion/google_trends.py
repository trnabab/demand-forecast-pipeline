from pytrends.request import TrendReq

pytrends = TrendReq(hl="en-US")

kw_list = ["dumbbells", "necklace", "smart tv", "samsung galaxy", "lego"]
pytrends.build_payload(kw_list, timeframe="2025-01-01 2026-01-01", geo="AU")

pytrends.interest_over_time().to_csv("../../data/raw/google_trends.csv")
