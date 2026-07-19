import re

URL_RE = re.compile(r"http\S+|www\.\S+")
NON_ALPHA_RE = re.compile(r"[^a-zA-Z\s]")
MULTI_SPACE_RE = re.compile(r"\s+")


def clean_text(text: str) -> str:
    """Lowercase, strip URLs and non-alphabetic characters, collapse whitespace.

    Must stay IDENTICAL between training and inference, otherwise the
    vectorizer sees a different distribution of tokens than it was fit on.
    """
    text = text.lower()
    text = URL_RE.sub(" ", text)
    text = NON_ALPHA_RE.sub(" ", text)
    text = MULTI_SPACE_RE.sub(" ", text).strip()
    return text
