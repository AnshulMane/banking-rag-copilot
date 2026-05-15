import re
import json


# =========================================
# LOAD JSON DATA
# =========================================

def load_cards():

    with open("data/banking_cards.json", "r") as f:
        return json.load(f)


def load_loans():

    with open("data/loan_eligibility_criteria.json", "r") as f:
        return json.load(f)


# =========================================
# DETECT CURRENCY
# =========================================

def detect_currency(user_input):

    text = user_input.lower()

    # INR
    if (
        "rupee" in text
        or "rupees" in text
        or "inr" in text
        or "lakh" in text
        or "crore" in text
        or "₹" in text
    ):
        return "INR", "₹"

    # USD
    elif (
        "dollar" in text
        or "dollars" in text
        or "usd" in text
        or "$" in text
    ):
        return "USD", "$"

    # GBP
    elif (
        "pound" in text
        or "pounds" in text
        or "gbp" in text
        or "£" in text
    ):
        return "GBP", "£"

    # EUR
    elif (
        "euro" in text
        or "euros" in text
        or "eur" in text
        or "€" in text
    ):
        return "EUR", "€"

    return "INR", "₹"


# =========================================
# EXTRACT INCOME
# =========================================

def extract_income(user_input):

    text = user_input.lower()

    match = re.search(r'(\d+)', text)

    if not match:
        return None

    amount = int(match.group(1))

    # INR
    if "crore" in text:
        amount *= 10000000

    elif "lakh" in text:
        amount *= 100000

    # INTERNATIONAL
    elif "million" in text:
        amount *= 1000000

    elif "billion" in text:
        amount *= 1000000000

    return amount


# =========================================
# FORMAT CURRENCY
# =========================================

def format_currency(user_input, symbol):

    income = extract_income(user_input)

    if income is None:
        return "Unknown"

    # INR
    if symbol == "₹":

        if income >= 10000000:
            return f"₹{income // 10000000} crore"

        elif income >= 100000:
            return f"₹{income // 100000} lakh"

        else:
            return f"₹{income:,}"

    # USD
    elif symbol == "$":

        if income >= 1000000:
            return f"${income // 1000000} million"

        else:
            return f"${income:,}"

    # GBP
    elif symbol == "£":

        if income >= 1000000:
            return f"£{income // 1000000} million"

        else:
            return f"£{income:,}"

    # EUR
    elif symbol == "€":

        if income >= 1000000:
            return f"€{income // 1000000} million"

        else:
            return f"€{income:,}"

    return str(income)


# =========================================
# EXTRACT CREDIT SCORE
# =========================================

def extract_credit_score(user_input):

    patterns = [

        r'credit score\s*(\d+)',
        r'cibil\s*(\d+)',
        r'score\s*(\d+)'

    ]

    for pattern in patterns:

        match = re.search(pattern, user_input.lower())

        if match:
            return int(match.group(1))

    return None


# =========================================
# DETECT CLIENT TIER
# =========================================

def detect_client_tier(income):

    if income is None:
        return "Unknown"

    if income >= 10000000:
        return "Ultra High Net Worth (UHNW)"

    elif income >= 1000000:
        return "High Net Worth (HNW)"

    elif income >= 300000:
        return "Affluent"

    return "Retail"


# =========================================
# DETECT QUERY INTENT
# =========================================

def detect_intent(user_input):

    text = user_input.lower()

    # LOANS
    if any(word in text for word in [

        "loan",
        "mortgage",
        "emi",
        "interest rate",
        "eligibility"

    ]):
        return "Loan Advisory"

    # FRAUD
    elif any(word in text for word in [

        "fraud",
        "suspicious",
        "compliance",
        "transaction",
        "aml"

    ]):
        return "Fraud & Compliance"

    # WEALTH
    elif any(word in text for word in [

        "wealth",
        "portfolio",
        "investment",
        "estate",
        "family office",
        "uhnw",
        "hni",
        "private banking"

    ]):
        return "Wealth Management"

    # CARDS
    elif any(word in text for word in [

        "credit card",
        "travel card",
        "premium card"

    ]):
        return "Premium Cards"

    return "General Banking"


# =========================================
# QUERY ROUTER
# =========================================

def route_query(user_input):

    intent = detect_intent(user_input)

    if intent == "Loan Advisory":
        return "loan"

    elif intent == "Fraud & Compliance":
        return "fraud"

    elif intent == "Wealth Management":
        return "wealth"

    elif intent == "Premium Cards":
        return "cards"

    return "general"


# =========================================
# LOAN ELIGIBILITY
# =========================================

def check_loan_eligibility(user_input):

    loans = load_loans()

    income = extract_income(user_input)

    credit_score = extract_credit_score(user_input)

    if income is None:
        return "Unable to determine eligibility"

    if credit_score is None:
        credit_score = 700

    for loan in loans:

        if (

            income >= loan["min_income"]
            and credit_score >= loan["min_credit_score"]

        ):

            return f"Eligible for {loan['type']}"

    return "Currently not eligible"


# =========================================
# CARD RECOMMENDATION
# =========================================

def recommend_cards():

    cards = load_cards()

    recommendations = []

    for card in cards:

        recommendations.append({

            "name": card["name"],
            "type": card["type"],
            "annual_fee": card["annual_fee"],
            "benefits": card["benefits"]

        })

    return recommendations


# =========================================
# EXECUTIVE SUMMARY
# =========================================

def executive_summary(user_input):

    currency_code, symbol = detect_currency(user_input)

    formatted_income = format_currency(
        user_input,
        symbol
    )

    income = extract_income(user_input)

    client_tier = detect_client_tier(income)

    intent = detect_intent(user_input)

    credit_score = extract_credit_score(user_input)

    summary = f"""
Executive Banking Summary
--------------------------------

Detected Currency:
{currency_code} ({symbol})

Estimated Client Income:
{formatted_income}

Client Tier:
{client_tier}

Detected Banking Intent:
{intent}
"""

    if credit_score:
        summary += f"\nCredit Score Detected:\n{credit_score}\n"

    return summary


# =========================================
# MAIN ENTERPRISE ANALYSIS
# =========================================

def banking_ai(user_input):

    currency_code, symbol = detect_currency(user_input)

    formatted_income = format_currency(
        user_input,
        symbol
    )

    income = extract_income(user_input)

    client_tier = detect_client_tier(income)

    intent = detect_intent(user_input)

    routed_department = route_query(user_input)

    eligibility = check_loan_eligibility(user_input)

    cards = recommend_cards()

    executive = executive_summary(user_input)

    card_output = ""

    for card in cards:

        card_output += f"""

Card Name: {card['name']}
Type: {card['type']}
Annual Fee: ₹{card['annual_fee']}
Benefits: {", ".join(card['benefits'])}

"""

    response = f"""
{executive}

Enterprise Banking Intelligence
--------------------------------

AI Query Routing:
{routed_department.upper()} PIPELINE

Loan Eligibility:
{eligibility}

Recommended Banking Products:
{card_output}

AI Banking Insights:
- Enterprise banking intent identified
- Client segmentation completed
- Personalized banking recommendations generated
- Risk and wealth profiling initiated
- Banking intelligence pipeline activated
"""

    return response