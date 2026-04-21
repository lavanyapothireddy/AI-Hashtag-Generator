import re

STOPWORDS = {
    "is", "am", "are", "was", "were", "be", "being", "been",
    "using", "use", "based", "on", "in", "at", "to", "for",
    "and", "or", "of", "a", "an", "the", "with", "by"
}

def clean_text(text: str):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())

def tokenize(text: str):
    words = clean_text(text).split()
    return [w for w in words if w not in STOPWORDS]

def generate_hashtags(text: str):
    words = tokenize(text)
    t = text.lower()

    hashtags = set()

    # ---------------- AI DOMAIN LOGIC ----------------
    if "ai" in t or "artificial intelligence" in t:
        hashtags.add("#AI")
        hashtags.add("#ArtificialIntelligence")
        hashtags.add("#MachineLearning")

    if "chatbot" in t:
        hashtags.add("#Chatbot")

    if "customer support" in t:
        hashtags.add("#CustomerSupport")

    if "iot" in t:
        hashtags.add("#IoT")

    # ---------------- WORD-LEVEL TAGS ----------------
    for w in words:
        if len(w) > 2:
            hashtags.add("#" + w.capitalize())

    # ---------------- CORE TAGS ----------------
    hashtags.add("#Innovation")
    hashtags.add("#Technology")

    return list(hashtags)[:12]
