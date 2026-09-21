"""Optional AI caption rewriter (OpenAI-compatible API).

If AI_API_KEY is set, daily.py uses this to freshen up captions every day.
Without it, the built-in 30-day content bank is used (free forever).

Works with OpenAI or any compatible endpoint:
  AI_API_KEY=...  AI_BASE_URL=https://api.openai.com/v1  AI_MODEL=gpt-4o-mini
"""
import json
import os
import urllib.request


def rewrite_caption(base_caption, context, timeout=25):
    key = os.environ.get("AI_API_KEY")
    if not key:
        return None
    base = os.environ.get("AI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("AI_MODEL", "gpt-4o-mini")
    prompt = (
        "Rewrite this Instagram caption for an Indian perfume brand (Shabnal Perfumes). "
        "Keep it in Hinglish (Hindi in Roman script mixed with English), keep emojis, "
        "keep the order line with number 90263 99218, keep it under 900 characters, "
        "make it fresh and catchy but same meaning.\n\n"
        f"Context: {context}\n\nCaption:\n{base_caption}"
    )
    body = json.dumps({
        "model": model, "temperature": 0.9, "max_tokens": 500,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        f"{base}/chat/completions", data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.load(r)
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"(AI rewrite skipped: {e})")
        return None
