"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""

def average_review(word, review_filename):
    """
    FIXME: Add function synopsis here.

    Parameters:
    word (type: string): The word to look for in the reviews.
    FIXME: add info about second parameter

    Returns:
    (type: float) FIXME by describing what is returned here.
    """

    review_file = open(review_filename, 'r')

    for line in review_file:
        # make lower case to avoid case sensitivity
        lower_line = line.lower()  

        # FIXME: finish implementing this loop body


    # done reading file, so close it
    review_file.close()

    # FIXME: calculate the average review score

    return None     # replace this with returning the calculated average


def estimate_review_score(movie_review, review_filename):
    """
    FIXME: Fill in this docstring comment, using the exact format given for the
    average_review docstring comment.
    """

    return None     # replace this with returning the estimated review



def estimate_user_review():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """

    pass # replace this line of code with your function implementation


# Do not modify anything after this point.
if __name__ == "__main__":
    estimate_user_review()
