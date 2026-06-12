def is_high_risk(text):
    keywords = ["inspectie", "tekort", "faillissement", "crisis", "IGJ"]
    matches = [k for k in keywords if k in text.lower()]
    return len(matches) > 0
