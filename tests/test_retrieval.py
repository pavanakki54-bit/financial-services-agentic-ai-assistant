import numpy as np
import pytest

from app.rag.retrieval import cosine_similarity, retrieve_chunks


def test_cosine_similarity():
    query = np.array([1.0, 0.0], dtype=np.float32)

    documents = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
        ],
        dtype=np.float32,
    )

    scores = cosine_similarity(query, documents)

    assert scores.shape == (2,)
    assert scores[0] > scores[1]


def test_dispute_policy_retrieval():
    results = retrieve_chunks(
        "How long do I have to dispute a transaction?",
        top_k=3,
    )

    assert len(results) == 3
    assert results[0]["source"] == "dispute_policy.md"


def test_fee_policy_retrieval():
    results = retrieve_chunks(
        "Can a customer request a fee waiver?",
        top_k=3,
    )

    assert len(results) == 3
    assert results[0]["source"] == "fee_policy.md"


def test_empty_query_rejected():
    with pytest.raises(ValueError):
        retrieve_chunks("", top_k=3)


def test_invalid_top_k_rejected():
    with pytest.raises(ValueError):
        retrieve_chunks(
            "test query",
            top_k=0,
        )
