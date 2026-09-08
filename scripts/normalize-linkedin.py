#!/usr/bin/env python3
"""Normalize captured Oxygen LinkedIn exports without modifying original responses.

All source text is retained verbatim. Writes are append-only: an existing output
must match byte-for-byte. The selected corpus is 200 newest Adam-authored posts;
all extra items, including reposts, stay in exact provider/table captures.
"""
import argparse
import hashlib
import json
from pathlib import Path


def append(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        assert path.read_text() == body, f"Refusing to replace existing source: {path}"
    else:
        path.write_text(body)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="raw/sources/2026-09-08-linkedin")
    parser.add_argument("--export", required=True)
    args = parser.parse_args()
    base = Path(args.base)
    pilot_path = base / "responses/page-01-live.json"
    pilot = json.loads(pilot_path.read_text())["data"]["result"]["response"]["raw"]["elements"]
    table_path = Path(args.export)
    table = json.loads(table_path.read_text())
    records = [(p, str(pilot_path)) for p in pilot]
    records += [(r["source_payload"], str(table_path)) for r in table]
    unique = {}
    for post, source in records:
        unique.setdefault(str(post["id"]), (post, source))
    authored = [(p, s) for p, s in unique.values()
                if p.get("author", {}).get("publicIdentifier") == "retentionadam"]
    authored.sort(key=lambda pair: pair[0]["postedAt"]["date"], reverse=True)
    assert len(authored) >= 200, f"Only {len(authored)} authored posts"
    selected = authored[:200]
    normalized = []
    for rank, (post, origin) in enumerate(selected, 1):
        date = post["postedAt"]["date"]
        post_id = str(post["id"])
        path = base / "posts" / f"{date[:10]}-{post_id}.md"
        item = {
            "rank": rank, "id": post_id, "source_date": date,
            "source_url": post["linkedinUrl"], "author": post["author"]["name"],
            "author_identifier": post["author"]["publicIdentifier"],
            "content": post.get("content", ""), "source_file": origin,
            "markdown_path": str(path), "engagement": post.get("engagement", {}),
            "has_images": bool(post.get("postImages")),
            "has_repost": bool(post.get("repost")),
        }
        normalized.append(item)
        body = "\n".join([
            "---", "type: source", "status: captured", "owner: adam",
            "created: 2026-09-08", "updated: 2026-09-08",
            f"source_date: {json.dumps(date)}", f"post_id: {json.dumps(post_id)}",
            f"source_url: {json.dumps(post['linkedinUrl'])}",
            'source_author: "Adam Robinson"', 'attribution: "Published under Adam Robinson’s profile; writing process unverified"',
            'public_use: "Public-source research; approval for new first-person copy unresolved"',
            f"sources: [{json.dumps(origin)}]", "tags: [source, linkedin, adam-robinson]", "---", "",
            f"# LinkedIn post — {date[:10]} — {post_id}", "",
            f"- Published: {date}", f"- Source: {post['linkedinUrl']}",
            f"- Capture: 2026-09-08; Oxygen native `scraper.linkedin_profile_posts`.",
            f"- Recency rank: {rank} of 200 Adam-authored posts.", "",
            "## Exact post text", "", post.get("content", ""), "",
            "## Source Notes", "",
            f"Exact source object retained in `{origin}` (post ID `{post_id}`).",
            "Engagement is a capture-time snapshot, not a business outcome. Mentions and third-party metrics remain attributed to their subjects.", "",
        ])
        append(path, body)
    append(base / "posts.normalized.json", json.dumps(normalized, indent=2, ensure_ascii=False) + "\n")
    audit = {
        "selected_count": len(selected), "selected_unique_ids": len({p['id'] for p in normalized}),
        "selected_author_identifiers": sorted({p['author_identifier'] for p in normalized}),
        "captured_unique_timeline_items": len(unique), "captured_adam_authored": len(authored),
        "excluded_other_authors": [{"id": p['id'], "author": p.get('author', {}).get('name'),
                                   "url": p.get('linkedinUrl')} for p, _ in unique.values()
                                  if p.get('author', {}).get('publicIdentifier') != 'retentionadam'],
        "newest_date": normalized[0]['source_date'], "oldest_selected_date": normalized[-1]['source_date'],
        "empty_text_ids": [p['id'] for p in normalized if not p['content'].strip()],
        "post_text_sha256": {p['id']: hashlib.sha256(p['content'].encode()).hexdigest() for p in normalized},
        "selection": "Sort by postedAt.date descending; dedupe id; filter author.publicIdentifier=retentionadam; take 200",
        "limits": "Provider-visible public posts at capture; deleted/private/unreturned content cannot be recovered. Original pilot raw envelope and exact table source_payload objects preserved. Media URLs retained but image text not transcribed.",
    }
    append(base / "selection-audit.json", json.dumps(audit, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in audit.items() if k != 'post_text_sha256'}, indent=2))


if __name__ == "__main__":
    main()
