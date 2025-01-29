import bisect
import itertools
import time
import datetime
import torch
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def embedding_similarity(query_ix,corpus,corpus_embeddings):
    """
    Compute the similarity between a text (string) from a "corpus of texts" (list of strings) using cosine-similarity compuded on their embeddings.
    
    Args:
        - query_ix (int) : index of an item of the corpus (used as query)
        - corpus (list of strings) : corpus
        - corpus_embeddings (list of embeddings) : list of the embeddings corresponding to the corpus items
    Returns:
        - similarity_scores (tensor) : tensor containing the similarity scores between the query's embedding and all the elements of the corpus
    """
    query_embedding = embedder.encode(corpus[query_ix], output_value='token_embeddings', convert_to_tensor=True)
    # Cosine-similarity
    similarity_scores = embedder.similarity(query_embedding, corpus_embeddings)[0]
    return similarity_scores

def ranking_similarities(query_ix,corpus,similarity_scores,top_k='ALL'):
    """
    """
    if top_k == 'ALL':
        top_k = len(corpus)
        
    scores, indices = torch.topk(similarity_scores, k=top_k)
    
    #print("\nQuery:", corpus[query_ix])
    #print(f"Top {top_k} most similar sentences in corpus:")
    #for score, idx in zip(scores, indices):
        #print(ix, corpus[idx], f"(Score: {score:.4f})")

    return query_ix, scores, indices

def first_below_threshold(scores, threshold):
    # Find the first index where scores[index] < threshold
    index = bisect.bisect_right([-s for s in scores], -threshold)
    return index if index < len(scores) else -1  # Return -1 if all scores are above threshold

def compute_similarity_matrix(corpus,cosinus_similarity_treshold,top_k='ALL'):
    corpus_embeddings = embedder.encode(corpus, output_value='token_embeddings', convert_to_tensor=True)
    results = []
    for i in range(len(corpus)):
        similarity_scores = embedding_similarity(i,corpus,corpus_embeddings)
        query_ix, scores, indices = ranking_similarities(i,corpus,similarity_scores,top_k='ALL')
        treshold_elem_index = first_below_threshold(scores, cosinus_similarity_treshold)
        results.append([query_ix,indices[:treshold_elem_index],scores[:treshold_elem_index]])
    return results

def find_common_similarities(name_similar, firstnames_similar):
    """
    Given two lists of similar indices (name_similar and firstnames_similar),
    find the intersection for each text.
    
    Args:
    - name_similar (List[List[int]]): List of lists containing similar indices based on names.
    - firstnames_similar (List[List[int]]): List of lists containing similar indices based on firstnames.
    
    Returns:
    - List[List[int]]: List of lists containing common similar indices.
    """
    results = []
    for i in range(len(name_similar)):
        intersection = list(set(name_similar[i][1].tolist()).intersection(firstnames_similar[i][1].tolist()))
        results.append([name_similar[i][0],intersection])
    return results

def remove_duplicates(list_of_lists):
    unique_lists = []
    seen = set()

    for lst in list_of_lists:
        tuple_lst = tuple(lst)  # Convert list to tuple (hashable)
        if tuple_lst not in seen:
            seen.add(tuple_lst)
            unique_lists.append(lst)  # Keep original list format

    return unique_lists

def export_groups(filtered_similar_items):
    lists = [sorted(f[1]) for f in filtered_similar_items]
    return remove_duplicates(lists)