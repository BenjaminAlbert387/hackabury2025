import re #Import that parses words
import nltk #Import for downloading nltk resources
from nltk.corpus import stopwords #Import nltk module for parsing stopwords
from nltk.tokenize import word_tokenize #Import for tokenzising and processing words

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')