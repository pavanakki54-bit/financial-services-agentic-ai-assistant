import numpy as np
import pytest

from app.rag.embeddings import embed_text, embed_texts


def test_embed_single_text():
    embedding = embed_text(
        "Customers may dispute an eligible transaction."
    )

    assert isinstance(embedding, np.ndarray)
    assert embedding.ndim == 1
    assert embedding.shape[0] > 0


def test_embed_multiple_texts():
    embeddings = embed_texts(
        [
            "Transaction dispute policy",
            "Fee waiver eligibility",
        ]
    )

    assert isinstance(embeddings, np.ndarray)
    assert embeddings.ndim == 2
    assert embeddings.shape[0] == 2
    assert embeddings.shape[1] > 0


def test_empty_text_rejected():
    with pytest.raises(ValueError):
        embed_text("")
