#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        scores = []
        for i, j in my_dict.items():
            scores.append(j)
        scores.sort()
        high_score = scores[-1]
        for i, j in my_dict.items():
            if my_dict[i] is high_score:
                return i
    return None
