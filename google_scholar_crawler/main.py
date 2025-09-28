import time
import json
from datetime import datetime
from pathlib import Path
from scholarly import scholarly, ProxyGenerator, MaxTriesExceededException

# Set up proxy and User-Agent
pg = ProxyGenerator()
pg.FreeProxies()  # Use free proxies (consider paid proxies for reliability)
scholarly.use_proxy(pg)
scholarly.set_user_agent(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

# Hard-coded Google Scholar ID
GG_SCHOLAR_ID = "4Yr_icEAAAAJ"

# Retry logic for fetching author data
max_attempts = 3
author = None
for attempt in range(max_attempts):
    try:
        print(f"Attempt {attempt + 1} to fetch author data...")
        author = scholarly.search_author_id(GG_SCHOLAR_ID)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'], publication_limit=20)  # Limit publications
        break
    except MaxTriesExceededException as e:
        print(f"Max tries exceeded: {e}. Retrying after {10 * (attempt + 1)} seconds...")
        time.sleep(10 * (attempt + 1))  # Exponential backoff: 10s, 20s, 30s
    except Exception as e:
        print(f"Unexpected error: {e}")
        break

if author is None:
    print("Failed to fetch author data after all attempts.")
    exit(1)

# Process and save data
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
print(json.dumps(author, indent=2))

# Save main data
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

# Save Shields.io data
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# Save stats data
repo_root = Path(__file__).resolve().parent.parent
data_dir = repo_root / "_data"
data_dir.mkdir(exist_ok=True)
with open(data_dir / "google_scholar_stats.json", 'w', encoding='utf-8') as outfile:
    json.dump({"citedby": author['citedby'], "updated": author['updated']}, outfile, ensure_ascii=False)

print("Data successfully saved.")
