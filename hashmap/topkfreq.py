from collections import defaultdict


def topkfreq(nums, k):
    """
    Find the k most frequent elements in the list.
    :param nums: List of integers
    :param k: Number of top frequent elements to return
    :return: List of the k most frequent elements
    """
   
    freq_map = defaultdict()
    
    for num in nums:
        freq_map[num] += 1
    
    # Sort the items by frequency in descending order and get the top k
    sorted_items = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
    
    return [item[0] for item in sorted_items[:k]]