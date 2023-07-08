import tiktoken
import numpy as np
import openai
from itertools import islice

from .base_operator import BaseOperator
from .util import get_max_tokens_for_model

from ai_context import AiContext


# This is the size of each chunk in terms of tokens.I chose 1k because a small query could 
# hypothetically fit 4 chunks in the context. Feels like a good balance between speed and accuracy.
EMBEDDING_CTX_LENGTH = 1000
EMBEDDING_ENCODING = 'cl100k_base'


class IndexData(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Index Data'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MANIPULATE_DATA.value
    
    @staticmethod    
    def declare_parameters():
        return [
            {
                "name": "should_cache_embeddings",
                "data_type": "boolean",
                "description": "Do you want to cache the embeddings?",
            }
        ]
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "text",
                "data_type": "string",
            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return [
            {
                "name": "vector_index",
                # Just a dictionary, without specifying any keys that are expected to be present there.
                # Naturally since it is vector index, the keys are going to be str(embedding vector).
                "data_type": "{}",
            }
        ]

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        text = ai_context.get_input('text', self)
        text = self.clean_text(text)
        should_cache_embeddings = step['parameters'].get('should_cache_embeddings', False)
        embeddings_dict = self.len_safe_get_embedding(text, ai_context, should_cache_embeddings=should_cache_embeddings)
        ai_context.set_output('vector_index', embeddings_dict, self)
        ai_context.add_to_log("Indexing complete with {} chunk embeddings".format(len(embeddings_dict)))
    
    
    def clean_text(self, text):
        return text.replace("\n", " ")


    def batched(self, iterable, n):
        if n < 1:
            raise ValueError('n must be at least one')
        it = iter(iterable)
        while (batch := tuple(islice(it, n))):
            yield batch


    def chunked_tokens(self, text, encoding_name, chunk_length):
        encoding = tiktoken.get_encoding(encoding_name)
        tokens = encoding.encode(text)
        chunks_iterator = self.batched(tokens, chunk_length)
        for chunk in chunks_iterator:
            decoded_chunk = encoding.decode(chunk)  # Decode the chunk
            yield decoded_chunk


    def len_safe_get_embedding(
        self, 
        text, 
        ai_context,
        max_tokens=EMBEDDING_CTX_LENGTH, 
        encoding_name=EMBEDDING_ENCODING,
        should_cache_embeddings=False
    ):
        chunk_embeddings = {}
        for chunk in self.chunked_tokens(text, encoding_name=encoding_name, chunk_length=max_tokens):
            embedding = ai_context.embed_text(chunk, cache_response=should_cache_embeddings)
            embedding_key = tuple(embedding)  # Convert numpy array to tuple
            chunk_embeddings[embedding_key] = chunk

        return chunk_embeddings

