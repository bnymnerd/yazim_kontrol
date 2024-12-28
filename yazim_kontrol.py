from textblob import TextBlob

def check_spelling(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()  # Yazım hatalarını düzeltiyor
    return str(corrected_text)