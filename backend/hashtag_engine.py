import re

STOPWORDS = {
    "is","am","are","was","were","be","being","been",
    "using","use","based","on","in","at","to","for",
    "and","or","of","a","an","the","with","by"
}

def clean(text):
    return re.sub(r"[^a-z0-9\s]", "", text.lower())

def tokens(text):
    words = clean(text).split()
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

def generate_hashtags(text: str):
    t = text.lower()
    words = tokens(text)

    tags = set()

    # ---------------- WORD TAGS ----------------
    for w in words:
        if w == "ai":
            tags.add("#AI")
        elif w == "iot":
            tags.add("#IoT")
        else:
            tags.add("#" + w.capitalize())

    # ---------------- DOMAIN LOGIC ----------------
    if "ai" in t:
        tags.update(["#ArtificialIntelligence", "#MachineLearning"])

    if "chatbot" in t:
        tags.add("#Chatbot")

    if "customer support" in t:
        tags.add("#CustomerSupport")

    if "agriculture" in t or "farming" in t:
        tags.update(["#Agriculture", "#AgriTech", "#SmartFarming"])

    # ---------------- CLEANING BAD TAGS ----------------
    remove = {"#Smart", "#System", "#Based", "#Using", "#Iot"}
    tags = tags - remove

    # ensure correct IoT format
    if "iot" in t:
        tags.add("#IoT")

    # core tags
    tags.add("#Technology")
    tags.add("#Innovation")

    return list(tags)[:12]
