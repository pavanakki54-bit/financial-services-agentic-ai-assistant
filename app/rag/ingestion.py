from pathlib import Path


POLICY_DIR = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "policies"
)


def load_policy_documents() -> list[dict[str, str]]:
    """
    Load synthetic Markdown policy documents.

    Returns each document with its source filename and text.
    """

    documents = []

    for file_path in sorted(POLICY_DIR.glob("*.md")):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "source": file_path.name,
                "text": text,
            }
        )

    return documents
