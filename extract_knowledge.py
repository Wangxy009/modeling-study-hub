import json
from pathlib import Path

from pypdf import PdfReader


SOURCE = Path("/Users/wangxiaoya/Downloads/数学建模培训")
OUTPUT = Path("/Users/wangxiaoya/Documents/Codex/modeling-study-hub/data/knowledge.json")

SKIP = {"彭幸春简历(2026.07).pdf"}


def clean(text):
    text = (text or "").encode("utf-8", "replace").decode("utf-8")
    lines = [" ".join(line.split()) for line in text.splitlines()]
    return "\n".join(line for line in lines if line).strip()


documents = []
for path in sorted(SOURCE.glob("*.pdf")):
    if path.name in SKIP:
        continue
    try:
        reader = PdfReader(path)
        pages = []
        for number, page in enumerate(reader.pages, 1):
            text = clean(page.extract_text())
            if text:
                pages.append({"page": number, "text": text})
        documents.append({
            "title": path.name,
            "path": str(path),
            "page_count": len(reader.pages),
            "text_pages": len(pages),
            "pages": pages,
        })
        print(path.name, len(reader.pages), len(pages))
    except Exception as exc:
        print("SKIP", path.name, exc)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps({"documents": documents}, ensure_ascii=False), encoding="utf-8")
print("OUTPUT", OUTPUT, OUTPUT.stat().st_size)
