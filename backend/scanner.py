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

def scan(input_text):
    report = ""
    if input_text is None:
        input_text = ""
    else:
        input_text.strip().lower()

    wordtokens = word_tokenize(input_text)

    stop_words = set(stopwords.words("english"))
    filter_words = [word for word in words if word not in stop_words]

    bad_words = ["prize", "diamonds", "required", "inheritance", "now", "alaye",
                "consignment", "100", "government", "business", "urgent", "royalty"]

    bad_phrases = ["dear friend", "act now"]

    found_words = [word for word in filter_words if word in bad_words]
    found_phrases = [phrase for phrase in bad_phrases if re.search(r"\b" + re.escape(phrase) + r"\b", input_text)]

    score = 0
    word_point = 2
    phrase_point = 5

    for word in found_words:
        if word == "alaye":
            score += 20
        else:
            score += word_point

    score += len(found_phrases) * phrase_point

    report = f"Your score is: {score}\n\n"

    if score >= 20:
            report += "Highly likely to be a scam. Do not interact and report the sender.\n"
            report += "DO NOT click any links in this email.\n"
            report += "Remember: No legitimate business will tell you to give any personal details over email or phone.\n"
            report += "If you or someone you know has been a victim of fraud, contact Action Fraud:\n"
            report += "- Website: https://www.actionfraud.police.uk/\n"
            report += "- Phone Number: 0300 123 2040\n\n"
        elif score >= 10: 
            report += "May be a scam. Investigate the sender before proceeding.\n" 
            report += "DO NOT click any links unless you know they're safe.\n"
            report += "Remember: No legitimate business will tell you to give any personal details over email or phone.\n"
            report += "If you or someone you know has been a victim of fraud, contact Action Fraud:\n"
            report += "- Website: https://www.actionfraud.police.uk/\n"
            report += "- Phone Number: 0300 123 2040\n\n"
        else:
            report += "Unlikely to be a scam, but remain cautious.\n" 
            report += "DO NOT click any links unless you know they're safe.\n"
            report += "Remember: No legitimate business will tell you to give any personal details over email or phone.\n"
            report += "If you or someone you know has been a victim of fraud, contact Action Fraud:\n"
            report += "- Website: https://www.actionfraud.police.uk/\n"
            report += "- Phone Number: 0300 123 2040\n\n"

        return report