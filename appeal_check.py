#!/usr/bin/env python3
"""
Criterion 3: in 10 of 10 valid appeals, the submission moves to under_review
and an appeal record appears in GET /log.

    python appeal_check.py --trial 1 --label before

Submits each of my ten pieces of writing, appeals the content_id that came
back, then reads GET /log and checks an appeal entry exists for it with status
under_review. Writes results/appeal_check_<label>_trial<N>.md.
"""

import argparse
import json
import urllib.error
import urllib.request
import uuid
from datetime import datetime
from pathlib import Path

from scenarios import MY_WRITING

BASE = "http://127.0.0.1:5000"


def call(method, path, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        BASE + path, data=data, method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        try:
            return exc.code, json.loads(raw)
        except json.JSONDecodeError:
            return exc.code, {"raw": raw[:200]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trial", type=int, required=True)
    parser.add_argument("--label", default="before")
    args = parser.parse_args()

    run_tag = uuid.uuid4().hex[:6]
    rows = []
    for i, text in enumerate(MY_WRITING, 1):
        creator = f"appeal_{args.label}_t{args.trial}_{run_tag}_{i:02d}"
        s_status, s_body = call("POST", "/submit", {"text": text, "creator_id": creator})
        content_id = s_body.get("content_id") if isinstance(s_body, dict) else None

        a_status, a_body = (None, {})
        if content_id:
            a_status, a_body = call("POST", "/appeal", {
                "content_id": content_id,
                "creator_id": creator,
                "reasoning": "I wrote this myself.",
            })
        rows.append({
            "n": i, "submit_status": s_status, "content_id": content_id,
            "appeal_status": a_status,
            "appeal_response_status": a_body.get("status") if isinstance(a_body, dict) else None,
        })
        print(f"  [{i:2d}/10] submit {s_status}  appeal {a_status}  "
              f"{rows[-1]['appeal_response_status']}  {content_id}")

    _, log = call("GET", "/log")
    entries = log.get("entries", []) if isinstance(log, dict) else []
    appealed = {
        e.get("content_id") for e in entries
        if e.get("event") == "appeal" and e.get("status") == "under_review"
    }

    passed = 0
    for row in rows:
        row["in_log"] = row["content_id"] in appealed
        row["pass"] = (
            row["appeal_status"] == 200
            and row["appeal_response_status"] == "under_review"
            and row["in_log"]
        )
        passed += row["pass"]

    print(f"\nTrial {args.trial}: {passed}/10 appeals moved to under_review and were logged.")

    out = Path("results") / f"appeal_check_{args.label}_trial{args.trial}.md"
    out.parent.mkdir(exist_ok=True)
    lines = [
        f"# Appeal check - {args.label}, trial {args.trial}",
        "",
        "- Produced by: `appeal_check.py::main`",
        f"- When: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"- Result: **{passed}/10**",
        "",
        "| # | content_id | submit | appeal | response status | in log | pass |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['n']} | `{r['content_id']}` | {r['submit_status']} | {r['appeal_status']} "
            f"| {r['appeal_response_status']} | {r['in_log']} | {'PASS' if r['pass'] else 'FAIL'} |"
        )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()