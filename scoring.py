def calculate_score(results):

    score=100

    for item in results:

        if not item["passed"]:

            score-=item["weight"]

    if score<0:

        score=0

    return score