import tiktoken
import numpy as np


def get_max_tokens_for_model(model_name: str) -> int:
    token_limits = {
        "gpt-3.5-turbo": 4096,
        "gpt-3.5-turbo-16k": 16384,
        "gpt-4": 8192,
        "gpt-4-32k": 32768,
    }

    max_tokens = token_limits.get(model_name)

    if max_tokens is None:
        raise ValueError(f"Model '{model_name}' is not supported. Please use one of the supported models: {', '.join(token_limits.keys())}")

    return max_tokens
    
    
def cosine_distance(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    

def count_tokens(s: str, model_name: str) -> int:
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(s))
    return num_tokens
    

# Hybrid search helpers below
def sort_chunks_by_similarity(query_emb, vector_index):
    chunks = []

    for emb_tuple, text in vector_index.items():
        emb_array = np.array(emb_tuple)
        similarity = cosine_distance(query_emb, emb_array)
        chunks.append((-similarity, emb_tuple, text))

    chunks.sort()
    return chunks


def select_most_relevant_chunks(sorted_chunks, token_budget, model_name):
    num_tokens_spent = 0
    selected_chunks = []
    
    for similarity, emb_tuple, text in sorted_chunks:
        text_tokens = count_tokens(text, model_name)
        
        if num_tokens_spent + text_tokens  < token_budget:
            num_tokens_spent += text_tokens 
            selected_chunks.append(text)
        else:
            break
    
    return selected_chunks

