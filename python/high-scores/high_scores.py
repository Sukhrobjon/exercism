def latest(scores):
    """
        Return the last added score
    """
    return scores[-1]


def personal_best(scores):
    """
        Return the max score in the list
    """
    return max(scores)


def personal_top_three(scores):
    """
        Return top three score from the list. if there are less than 3
        scores then return in a decending order the all elements
    """
    # sorted the list in a decending order
    sorted_scores = sorted(scores, reverse=True)
    # check if there are at least 3 elements 
    if len(scores) >= 3:
        # if so, return the first three top scores
        return sorted_scores[:3]
    # else return in a decending order
    return sorted_scores[:len(scores)]
