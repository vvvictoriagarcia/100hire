"""
get_transcripts.py
Collects YouTube transcripts for the cold outreach research project.

Usage:
    1. pip install youtube-transcript-api
    2. Fill in videos.csv (columns: expert,video_url,title,date)
    3. python scripts/get_transcripts.py

Output:
    research/youtube-transcripts/<expert>/<date>-<slug>.md
    One markdown file per video, with metadata header + full transcript.
"""

import csv
import re
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

INPUT_CSV = Path("scripts/videos.csv")
OUTPUT_DIR = Path("research/youtube-transcripts")
LANGUAGES = ["en", "es"]  # preferred transcript languages, in order


def extract_video_id(url: str) -> str | None:
    """Extract the 11-char video ID from any common YouTube URL format."""
    patterns = [
        r"(?:v=|/v/|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})",
        r"^([A-Za-z0-9_-]{11})$",  # already a bare ID
    ]
    for pattern in patterns:
        match = re.search(pattern, url.strip())
        if match:
            return match.group(1)
    return None


def slugify(text: str, max_len: int = 60) -> str:
    """Turn a video title into a safe filename slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len] or "untitled"


def fetch_transcript_text(video_id: str) -> str:
    """Fetch and join the transcript into plain paragraphs."""
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=LANGUAGES)
    lines = [snippet.text.strip() for snippet in fetched if snippet.text.strip()]
    # Group lines into readable paragraphs (~12 caption lines each)
    paragraphs = [
        " ".join(lines[i : i + 12]) for i in range(0, len(lines), 12)
    ]
    return "\n\n".join(paragraphs)


def write_markdown(expert: str, title: str, date: str, url: str, transcript: str) -> Path:
    expert_dir = OUTPUT_DIR / slugify(expert)
    expert_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{date}-{slugify(title)}.md"
    path = expert_dir / filename
    content = (
        f"# {title}\n\n"
        f"- **Author:** {expert}\n"
        f"- **Published:** {date}\n"
        f"- **Source:** {url}\n"
        f"- **Collected:** {time.strftime('%Y-%m-%d')}\n\n"
        f"---\n\n"
        f"## Transcript\n\n{transcript}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def main() -> None:
    if not INPUT_CSV.exists():
        print(f"Input file not found: {INPUT_CSV}")
        print("Create it with columns: expert,video_url,title,date")
        return

    ok, failed = 0, 0
    with INPUT_CSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Processing {len(rows)} videos...\n")

    for row in rows:
        expert = row["expert"].strip()
        url = row["video_url"].strip()
        title = row["title"].strip()
        date = row["date"].strip()  # YYYY-MM-DD

        video_id = extract_video_id(url)
        if not video_id:
            print(f"  SKIP  (bad URL) {url}")
            failed += 1
            continue

        try:
            transcript = fetch_transcript_text(video_id)
            path = write_markdown(expert, title, date, url, transcript)
            print(f"  OK    {path}")
            ok += 1
        except (TranscriptsDisabled, NoTranscriptFound):
            print(f"  SKIP  (no transcript available) {title} — {url}")
            failed += 1
        except VideoUnavailable:
            print(f"  SKIP  (video unavailable) {title} — {url}")
            failed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  ERROR {title}: {exc}")
            failed += 1

        time.sleep(1.5)  # be polite, avoid rate limiting

    print(f"\nDone. {ok} transcripts saved, {failed} skipped/failed.")


if __name__ == "__main__":
    main()
