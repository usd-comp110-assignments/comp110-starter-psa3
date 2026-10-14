"""COMP 110, PSA 3, Problem 2 (Sentiment Analysis).

Program to analyze movie reviews and predict the sentiment of new reviews.

Author: <INSERT YOUR NAME AND EMAIL HERE>
"""

def calculate_average_review(target_word, review_filename):
    """Insert a one-sentence description of the function here.

    Args:
        target_word: The word to look for in the reviews.
        To Do: Add info about the other parameter.

    Returns:
        float: Insert a one-sentence description of the return value here.
    """

    review_file = open(review_filename, 'r')

    for review in review_file:
        # make lower case to avoid case sensitivity
        review_lower = review.lower()  

        # FIXME: finish implementing this loop body


    # done reading file, so close it
    review_file.close()

    # FIXME: calculate the average review score

    return None     # replace this with returning the calculated average


def calculate_estimated_score(review_text, review_filename):
    return None     # replace this with returning the estimated review



def get_review_and_estimate():
    """Determines the estimated score of a user-entered movie review and indicates
    the sentiment of that review (e.g. "positive").
    """

    pass # replace this line of code with your function implementation


# DO NOT modify anything after this point.
if __name__ == "__main__":
    get_review_and_estimate()
