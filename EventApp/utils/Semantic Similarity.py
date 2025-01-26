import os
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np
import logging
from typing import List, Union
from numpy.linalg import norm 


load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

if not OPEN_AI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables")

class SemanticSimilarity(object):
    '''
    A class to handle semantic similarity computations using OpenAI's embeddings.
    
    This class provides methods to convert text to embeddings and compute
    similarity between texts using cosine similarity.
    '''

    def __init__(self, model="text-embedding-3-small"):
        """
        Initialize the SemanticSimilarity class with OpenAI client and model
        """
        self.client = OpenAI(api_key=OPEN_AI_API_KEY)
        self.model = model

    def text2vector(self, text):
        """
        Convert text to embedding vectors.
        """
        response = self.client.embeddings.create(
        input=text,
        model=self.model)
        embeddings = np.array(response.data[0].embedding)
        return embeddings

    def compute_similarity(self, text1, text2):
        '''
        Compute the similarity between two texts
        '''
        embedding1 = self.text2vector(text1)
        embedding2 = self.text2vector(text2)

        return np.dot(embedding1, embedding2)/(norm(embedding1)* norm(embedding2))