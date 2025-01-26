import pytest
import numpy as np
from EventApp.utils.semantic_similarity import SemanticSimilarity

@pytest.fixture
def semantic_similarity():
    """Fixture to create SemanticSimilarity instance"""
    return SemanticSimilarity()

def test_initialization():
    """Test if class initializes correctly"""
    ss = SemanticSimilarity()
    assert ss.model == "text-embedding-3-small"
    assert ss.client is not None

def test_text2vector_single(semantic_similarity):
    """Test vector generation for single text"""
    text = "Hello world"
    vector = semantic_similarity.text2vector(text)
    assert isinstance(vector, np.ndarray)
    assert len(vector.shape) == 1  # Should be 1D array
    assert vector.shape[0] > 0     # Should have non-zero dimensions

def test_compute_similarity_similar_texts(semantic_similarity):
    """Test similarity computation for similar texts"""
    text1 = "The quick brown fox"
    text2 = "The fast brown fox"
    similarity = semantic_similarity.compute_similarity(text1, text2)
    assert isinstance(similarity, float)
    assert 0 <= similarity <= 1    # Cosine similarity range
    assert similarity > 0.5        # Similar texts should have high similarity

def test_compute_similarity_different_texts(semantic_similarity):
    """Test similarity computation for different texts"""
    text1 = "The quick brown fox"
    text2 = "The weather is nice today"
    similarity = semantic_similarity.compute_similarity(text1, text2)
    assert isinstance(similarity, float)
    assert 0 <= similarity <= 1
    assert similarity < 0.5        # Different texts should have low similarity

def test_empty_input(semantic_similarity):
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        semantic_similarity.text2vector("")

def test_invalid_model():
    """Test initialization with invalid model"""
    with pytest.raises(Exception):
        SemanticSimilarity(model="invalid-model")