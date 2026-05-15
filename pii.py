from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import re

# =========================================
# INITIALIZE PRESIDIO
# =========================================

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# =========================================
# PARTIAL ACCOUNT MASKING
# =========================================

def partial_mask_account_numbers(text):

    pattern = r'\b\d{8,16}\b'

    matches = re.findall(pattern, text)

    for match in matches:

        masked = "XXXXXX" + match[-4:]

        text = text.replace(match, masked)

    return text

# =========================================
# MAIN PII ANONYMIZATION
# =========================================

def anonymize_text(text):

    # =====================================
    # PARTIAL ACCOUNT MASKING
    # =====================================

    text = partial_mask_account_numbers(text)

    # =====================================
    # ALLOWED PII ENTITIES
    # =====================================

    allowed_entities = [

        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "CREDIT_CARD",
        "IBAN_CODE"

    ]

    # =====================================
    # ANALYZE TEXT
    # =====================================

    results = analyzer.analyze(
        text=text,
        language="en"
    )

    # =====================================
    # FILTER ONLY IMPORTANT ENTITIES
    # =====================================

    filtered_results = [

        r for r in results
        if r.entity_type in allowed_entities

    ]

    # =====================================
    # ANONYMIZE
    # =====================================

    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=filtered_results
    )

    return anonymized_result.text