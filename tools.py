import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk
from bs4 import BeautifulSoup

SENTENCE_NUMBER = 2


def get_contents(url: str) -> str:
    result = requests.get(url)
    return BeautifulSoup(result.text, 'html.parser').getText(separator='\n')


def summarizer(text: str) -> str:
    nltk.download('punkt')
    nltk.download('punkt_tab')
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize LexRank summarizer
    summarizer_lex = LexRankSummarizer()

    # Summarize using LexRank (e.g., 2 sentences)
    summary = summarizer_lex(parser.document, SENTENCE_NUMBER)

    # Convert summary to string
    lex_summary = ""
    for sentence in summary:
        lex_summary += str(sentence) + " "

    return lex_summary
