import re

# ----------------------------
# Stopwords (removed words)
# ----------------------------
STOPWORDS = {
    "is", "am", "are", "was", "were", "be", "being", "been",
    "using", "use", "based", "on", "in", "at", "to", "for",
    "and", "or", "of", "a", "an", "the", "with", "by"
}

# ----------------------------
# Clean text
# ----------------------------
def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

# ----------------------------
# Tokenize words
# ----------------------------
def tokenize(text: str):
    words = clean_text(text).split()
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

# ----------------------------
# Format hashtag
# ----------------------------
def format_tag(words):
    if words == ("ai",):
        return "#AI"
    return "#" + "".join(w.capitalize() for w in words)

# ----------------------------
# Main function
# ----------------------------
def generate_hashtags(text: str):
    words = tokenize(text)
    text_lower = text.lower()

    phrase_tags = set()
    word_tags = set()

    # ----------------------------
    # PHRASE LAYER (priority)
    # ----------------------------
    if "customer support" in text_lower:
        phrase_tags.add("#CustomerSupport")

    if "machine learning" in text_lower:
        phrase_tags.add("#MachineLearning")

    if "artificial intelligence" in text_lower or "ai" in text_lower:
        phrase_tags.add("#ArtificialIntelligence")
        phrase_tags.add("#MachineLearning")

    if "chatbot" in text_lower:
        phrase_tags.add("#Chatbot")

    # ----------------------------
    # WORD LAYER
    # ----------------------------
    for w in words:
        word_tags.add("#AI" if w == "ai" else "#" + w.capitalize())

    # ----------------------------
    # REMOVE SUB-WORDS IF PHRASE EXISTS
    # ----------------------------
    if "#CustomerSupport" in phrase_tags:
        word_tags.discard("#Customer")
        word_tags.discard("#Support")

    if "#MachineLearning" in phrase_tags:
        word_tags.discard("#Machine")
        word_tags.discard("#Learning")

    # ----------------------------
    # FINAL MERGE
    # ----------------------------
    final_tags = set()

    final_tags.update(word_tags)
    final_tags.update(phrase_tags)

    # ----------------------------
    # ALWAYS ADD CORE TAGS
    # ----------------------------
    final_tags.add("#Innovation")
    final_tags.add("#Technology")

    # ----------------------------
    # RETURN CLEAN LIST
    # ----------------------------
    return list(final_tags)[:12]
