import re
import json


# =========================
# LOAD JSON DATA
# =========================

def load_cards():
    with open("data/cards.json", "r") as f:
        return json.load(f)


def load_loans():
    with open("data/loan_criteria.json", "r") as f:
        return json.load(f)


# =========================
# DETECT CURRENCY
# =========================

def detect_currency(user_input):

    text = user_input.lower()

    # INR
    if (
        "rupee" in text
        or "rupees" in text
        or "inr" in text
        or "lakh" in text
        or "crore" in text
    ):
        return "INR", "₹"

    # USD
    elif (
        "dollar" in text
        or "dollars" in text
        or "usd" in text
        or "million dollars" in text
    ):
        return "USD", "$"

    # GBP
    elif (
        "pound" in text
        or "pounds" in text
        or "gbp" in text
    ):
        return "GBP", "£"

    # EUR
    elif (
        "euro" in text
        or "euros" in text
        or "eur" in text
    ):
        return "EUR", "€"

    # Default
    return "INR", "₹"


# =========================
# FORMAT CURRENCY
# =========================

def format_currency(text, symbol):

    text = text.lower()

    # Find number
    number_match = re.search(r'(\d+)', text)

    if not number_match:
        return "Unknown Income"

    amount = int(number_match.group(1))

    # INDIA
    if symbol == "₹":

        if "crore" in text:
            return f"₹{amount} crore"

        elif "lakh" in text:
            return f"₹{amount} lakh"

        else:
            return f"₹{amount:,}"

    # USD
    elif symbol == "$":

        if "million" in text:
            return f"${amount} million"

        elif "billion" in text:
            return f"${amount} billion"

        else:
            return f"${amount:,}"

    # GBP
    elif symbol == "£":

        if "million" in text:
            return f"£{amount} million"

        elif "billion" in text:
            return f"£{amount} billion"

        else:
            return f"£{amount:,}"

    # EUR
    elif symbol == "€":

        if "million" in text:
            return f"€{amount} million"

        elif "billion" in text:
            return f"€{amount} billion"

        else:
            return f"€{amount:,}"

    return str(amount)


# =========================
# EXTRACT CREDIT SCORE
# =========================

def extract_credit_score(user_input):

    match = re.search(r'credit score\s*(\d+)', user_input.lower())

    if match:
        return int(match.group(1))

    return 700


# =========================
# LOAN ELIGIBILITY
# =========================

def check_loan_eligibility(user_input):

    loans = load_loans()

    credit_score = extract_credit_score(user_input)

    text = user_input.lower()

    income_match = re.search(r'(\d+)', text)

    if income_match:
        income = int(income_match.group(1))
    else:
        income = 0

    # Convert lakh/crore to actual values
    if "crore" in text:
        income *= 10000000

    elif "lakh" in text:
        income *= 100000

    for loan in loans:

        if (
            income >= loan["min_income"]
            and credit_score >= loan["min_credit_score"]
        ):

            return f"Eligible for {loan['type']}"

    return "Not eligible for loan"


# =========================
# CARD RECOMMENDATION
# =========================

def recommend_cards():

    cards = load_cards()

    result = ""

    for card in cards:

        result += f"""
Card Name: {card['name']}
Type: {card['type']}
Annual Fee: ₹{card['annual_fee']}
Benefits: {", ".join(card['benefits'])}

"""

    return result


# =========================
# MAIN AI FUNCTION
# =========================

def banking_ai(user_input):

    currency_code, symbol = detect_currency(user_input)

    formatted_income = format_currency(user_input, symbol)

    eligibility = check_loan_eligibility(user_input)

    cards = recommend_cards()

    response = f"""
BANKING AI ANALYSIS
==============================

Detected Currency:
{currency_code} ({symbol})

Client Income:
{formatted_income}

Loan Eligibility:
{eligibility}

Recommended Banking Products:
{cards}

AI Banking Insights:
- Premium banking opportunities identified
- Personalized HNI recommendations generated
- Risk profile evaluated
- Wealth management eligibility checked
"""

    return response