# ASTOR — Enterprise Private Banking Intelligence Copilot

ASTOR is an enterprise-grade AI copilot designed for private banking and wealth management environments.  
The platform leverages Retrieval-Augmented Generation (RAG), vector search, local LLM inference, and PII masking to assist relationship managers with intelligent financial advisory workflows.

This project simulates how AI copilots can support ultra-high-net-worth (UHNW) banking operations through contextual intelligence, advisory automation, risk-aware responses, and secure knowledge retrieval.

---

# Overview

ASTOR is built as an enterprise AI assistant capable of:

- Wealth preservation advisory
- Private banking intelligence
- Relationship manager productivity support
- Cross-border banking insights
- Fraud and compliance intelligence
- Multi-generational estate planning guidance
- Premium banking recommendations
- Secure document-grounded AI responses

The system uses local LLM inference through Ollama combined with ChromaDB vector retrieval and LangChain orchestration.

---

# Key Features

- Retrieval-Augmented Generation (RAG)
- Enterprise AI Copilot Architecture
- ChromaDB Vector Database
- Phi-3 Local LLM Inference
- PII Detection and Masking
- Relationship Manager Advisory Workflows
- Wealth Management Intelligence
- Private Banking Use Cases
- Context-Aware AI Responses
- Streamlit Enterprise UI
- Local-First AI Deployment
- Multi-Document Financial Knowledge Retrieval

---

# Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM Runtime | Ollama |
| Language Model | Phi-3 |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | Ollama Embeddings |
| PII Security | Microsoft Presidio |
| Programming Language | Python |

---

# System Architecture

<p align="center">
User Query<br>
↓<br>
PII Detection & Masking<br>
↓<br>
RAG Retrieval Pipeline<br>
↓<br>
ChromaDB Vector Search<br>
↓<br>
Context Injection<br>
↓<br>
Local LLM (Phi-3 via Ollama)<br>
↓<br>
Enterprise Banking Response
</p>

---

# Workspace Preview

## ASTOR Banking Workspace

<p align="center">
  <img width="1845" height="692" alt="astor_workspace" src="https://github.com/user-attachments/assets/2198ab3c-356d-44f9-a4e7-74912ccb4d98" />
</p>

---

# AI Advisory Demonstrations

## Wealth Preservation Advisory Demo

<p align="center">
  <img width="1813" height="831" alt="wealth_preservation_demo_1" src="https://github.com/user-attachments/assets/a0312acb-8a29-4547-a23f-509cb7c82a7c" /> 
</p>  
<img width="1780" height="326" alt="wealth_preservation_demo_1 1" src="https://github.com/user-attachments/assets/46d8d4eb-1e44-4ec7-ae73-4c54c157763e" />

</p>

---

## Premium Banking Intelligence Demo

<p align="center">
  <img width="1768" height="828" alt="premium_banking_demo" src="https://github.com/user-attachments/assets/e062b4b7-556d-4413-9cbc-71f555925f52" />
</p>

---

## Relationship Manager Productivity Intelligence

<p align="center">
  <img width="1788" height="486" alt="relationship manager_productivity_ai_demo" src="https://github.com/user-attachments/assets/a944a8d4-2511-4e7a-9801-5c7b16947745" />

</p>

---

## Multi-Generational Client Engagement Strategy

<p align="center">
  <img width="1867" height="773" alt="client_engagement_strategy_demo_1" src="https://github.com/user-attachments/assets/dee0a40d-7241-44ec-a443-90a6cb030861" />
</p>
<img width="1828" height="484" alt="client_engagement_strategy_demo_1 1" src="https://github.com/user-attachments/assets/50ee289d-c387-4020-8648-f670bb0d6e30" />


</p>

---

## PII Detection & Security Layer

<p align="center">
 <img width="1799" height="747" alt="pii_security_demo" src="https://github.com/user-attachments/assets/e136e5f9-2945-4f74-8cb2-5ced5417ba8c" />

</p>

---

# Enterprise Banking Use Cases

## Wealth Management

- Wealth preservation strategies
- UHNW advisory workflows
- Investment intelligence
- Portfolio guidance
- Cross-border banking insights

## Relationship Management

- Personalized client engagement
- Multi-generational banking support
- Advisory automation
- Productivity enhancement
- AI-assisted client servicing

## Compliance & Security

- PII masking
- Secure AI responses
- Risk-aware retrieval
- Internal knowledge grounding
- Controlled local inference

---

# Project Structure

```text
banking-rag-copilot/
│
├── data/
│   ├── retail_loans_policy.pdf
│   ├── premium_credit_cards.pdf
│   ├── wealth_management_guidelines.pdf
│   ├── fraud_and_compliance_policy.pdf
│   ├── banking_cards.json
│   └── loan_eligibility_criteria.json
│
├── app.py
├── agent.py
├── rag.py
├── pii.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/AnshulMane/banking-rag-copilot.git
```

---

## Navigate to Project

```bash
cd banking-rag-copilot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv myenv
```

### Activate Environment

```bash
myenv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama:

https://ollama.com

---

# Pull Phi-3 Model

```bash
ollama pull phi3
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Security Architecture

ASTOR includes a dedicated PII detection and masking pipeline powered by Microsoft Presidio.

Sensitive information such as:
- account numbers
- phone numbers
- emails
- financial identifiers

can be detected and masked before entering the LLM pipeline.

This architecture enables safer enterprise AI deployment for regulated banking environments.

---

# Enterprise AI Design Principles

ASTOR is designed around enterprise AI engineering principles:

- Retrieval-grounded generation
- Secure local inference
- Explainable AI workflows
- Data privacy awareness
- Modular AI architecture
- Scalable advisory pipelines
- Human-in-the-loop banking support

---

# Author

Anshul Mane

