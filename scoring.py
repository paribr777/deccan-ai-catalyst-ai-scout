def score_interest(response):
    response = response.lower()
    if "actively looking" in response:
        return 1.0
    elif "interested" in response:
        return 0.7
    elif "maybe" in response:
        return 0.3
    else:
        return 0
