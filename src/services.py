import json
import requests
from flask import jsonify
import re #Import that parses words
import nltk #Import for downloading nltk resources
from nltk.corpus import stopwords #Import nltk module for parsing stopwords
from nltk.tokenize import word_tokenize #Import for tokenzising and processing words


def uRLScan(uRL:str):
    try:

        prefix = "Submission failed - "
        headers = {'API-Key':'019711e1-3c21-754c-9f46-28d37ef18f80','Content-Type':'application/json'}
        data = {"url": uRL, "visibility": "public"}
        response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response = response.json()
        if response.get('message') == 'Submission successful': 
            status = response['result']
            return (f"Submission successful - <a href='{status}'>Click me for a report</a>")
        if response.get('message') == 'Scan prevented ...': return str(prefix+response["errors"][0]["detail"])
        if response.get('message') == 'DNS Error - Could not resolve domain': return str(prefix+response['detail'])
        return str(response.get('message'))
    except Exception as error:
        raise RuntimeError(f"Unexpected error while scanning URL details: {error}")



try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def text_scan(input_text):
    try: 
        report = ""
        if input_text is None or not isinstance(input_text, str) or not input_text.strip():
            return jsonify({"Error":"There is not anything provided or provided data is not text as expected"}),400
        else:
            input_text = input_text.strip().lower()

        wordtokens = word_tokenize(input_text)

        stop_words = set(stopwords.words("english"))
        filter_words = [word for word in wordtokens if word not in stop_words]

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
    
        report_lines = [f"Your Score is {score}\n"]

        if score >= 20:
            report_lines.append(
            "Highly likely to be a scam. Do not interact and report the sender.\n"
            "DO NOT click any links in this email.\n"
            "Remember: No legitimate business will tell you to give any personal details over email or phone.\n"
            "If you or someone you know has been a victim of fraud, contact Action Fraud:\n"
            "- Website: https://www.actionfraud.police.uk/\n"
            "- Phone Number: 0300 123 2040\n"
        )
        elif score >= 10: 
            report_lines.append(
         "May be a scam. Investigate the sender before proceeding.\n"
         "DO NOT click any links unless you know they're safe.\n"
         "Remember: No legitimate business will tell you to give any personal details over email or phone.\n"
         "If you or someone you know has been a victim of fraud, contact Action Fraud:\n"
         "- Website: https://www.actionfraud.police.uk/\n"
         "- Phone Number: 0300 123 2040\n\n"
        )
        else:
            report_lines.append(
        "Unlikely to be a scam, but remain cautious.\n"
        "DO NOT click any links unless you know they're safe.\n"
        "Remember: No legitimate business will tell you to give any personal details over email or phone.\n"
        "If you or someone you know has been a victim of fraud, contact Action Fraud:\n"
        "- Website: https://www.actionfraud.police.uk/\n"
        "- Phone Number: 0300 123 2040\n\n"
       )
        report_actual = "".join(report_lines)
        return jsonify({"report": report_actual}) 
    except Exception as error: 
        return jsonify({"Error": f"Unexpected error while scanning text: {error}"}), 500