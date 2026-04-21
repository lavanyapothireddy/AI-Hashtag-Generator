import re

# ----------------------------
# STOPWORDS
# ----------------------------
STOPWORDS = {
    "is", "am", "are", "was", "were", "be", "being", "been",
    "using", "use", "based", "on", "in", "at", "to", "for",
    "and", "or", "of", "a", "an", "the", "with", "by"
}

# ----------------------------
# CLEAN TEXT
# ----------------------------
def clean_text(text: str):
    text = text.lower()
    return re.sub(r"[^a-z0-9\s]", "", text)

# ----------------------------
# TOKENIZE
# ----------------------------
def tokenize(text: str):
    words = clean_text(text).split()
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

# ----------------------------
# DOMAIN INTELLIGENCE LAYER
# ----------------------------
def apply_domain_logic(text: str, hashtags: set):
    t = text.lower()

    # AI domain
    if "ai" in t or "artificial intelligence" in t:
        hashtags.add("#AI")
        hashtags.add("#ArtificialIntelligence")
        hashtags.add("#MachineLearning")

    # Chatbot
    if "chatbot" in t:
        hashtags.add("#Chatbot")

    # Customer support
    if "customer support" in t:
        hashtags.add("#CustomerSupport")

    # IoT normalization (fix duplicates)
    if "iot" in t:
        hashtags.discard("#Iot")
        hashtags.discard("#iOT")
        hashtags.add("#IoT")

    # Agriculture domain upgrade
    if "agriculture" in t or "farming" in t:
        hashtags.add("#Agriculture")
        hashtags.add("#AgriTech")
        hashtags.add("#SmartFarming")

    # Tech base tags
    hashtags.add("#Technology")
    hashtags.add("#Innovation")

    return hashtags

# ----------------------------
# MAIN FUNCTION
# ----------------------------
def generate_hashtags(text: str):
    words = tokenize(text)

    hashtags = set()

    # word-level hashtags (clean only)
    for w in words:
        if w == "ai":
            hashtags.add("#AI")
        else:
            hashtags.add("#" + w.capitalize())

    # apply domain intelligence
    hashtags = apply_domain_logic(text, hashtags)

    # remove noisy generic tags (quality control)
    noisy = {"#Smart", "#System", "#Based", "#Using"}

    hashtags = hashtags - noisy

    return list(hashtags)[:12]
