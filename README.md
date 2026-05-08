# ASTOR — Enterprise Private Banking Intelligence Platform

ASTOR is an enterprise-grade AI copilot designed for private banking, wealth advisory, and relationship management workflows.

Built using Retrieval-Augmented Generation (RAG), ASTOR combines local LLMs, vector search, enterprise knowledge retrieval, and PII protection to simulate modern institutional banking intelligence systems.

The platform enables Relationship Managers (RMs) and banking teams to interact with banking knowledge, client intelligence, lending policies, fraud controls, and wealth advisory workflows through natural language.

---

# Overview

ASTOR was built to explore how Generative AI can enhance enterprise banking operations through:

- AI-assisted relationship management
- Retrieval-Augmented Generation (RAG)
- Wealth advisory intelligence
- Enterprise document retrieval
- Fraud and compliance support
- Private banking workflows
- Cross-border financial intelligence
- PII-aware conversational AI

The project focuses on enterprise architecture patterns commonly used in modern AI copilots deployed within financial institutions.

---

# Key Features

## Enterprise Banking Intelligence

- Wealth preservation advisory
- UHNW/HNI client intelligence
- Estate and legacy planning insights
- Cross-border banking recommendations
- Premium banking product recommendations

---

## AI-Powered RAG Pipeline

- Retrieval-Augmented Generation using LangChain
- Semantic document search using ChromaDB
- Banking policy and advisory retrieval
- Context-aware response generation

---

## Security & Compliance

- PII detection and anonymization using Microsoft Presidio
- Secure local inference using Ollama
- No external LLM API dependency
- Enterprise-style privacy-aware workflow

---

## Conversational RM Workspace

- GPT-style banking workspace UI
- Natural language banking interactions
- Relationship manager productivity assistant
- Institutional AI copilot experience

---

## Multi-Currency Intelligence

Supports intelligent financial interpretation for:

- INR
- USD
- GBP
- EUR

Examples:

- 30 lakh rupees → ₹30,00,000
- 3 million dollars → $3,000,000
- 2 million pounds → £2,000,000

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

# Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM Runtime | Ollama |
| Language Model | Phi-3 |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | Granite Embeddings |
| Security Layer | Microsoft Presidio |
| Backend Language | Python |

---

# Project Structure

```text
banking-rag-copilot/
│
├── data/
│   ├── loans.pdf
│   ├── credit_cards.pdf
│   ├── fraud_policy.pdf
│   ├── wealth_management.pdf
│   ├── cards.json
│   └── loan_criteria.json
│
├── app.py
├── rag.py
├── pii.py
├── agent.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# RAG Workflow

## 1. Document Ingestion

Enterprise banking documents are loaded from:

- lending policies
- fraud policies
- wealth management documentation
- premium banking product datasets

---

## 2. Text Chunking

Documents are split into semantic chunks using LangChain text splitters.

---

## 3. Embedding Generation

Chunks are converted into vector embeddings using Granite Embeddings.

---

## 4. Vector Storage

Embeddings are stored in ChromaDB for semantic similarity retrieval.

---

## 5. Retrieval-Augmented Generation

Relevant banking context is retrieved and injected into prompts before inference.

This architecture improves:

- factual grounding
- domain accuracy
- response relevance
- hallucination reduction

---

# Example Enterprise Queries

## Wealth Advisory

```text
Recommend wealth preservation strategies for a UK-based UHNW client with £15 million in liquid assets and international investments.
```

---

## Lending Intelligence

```text
Analyze loan eligibility for a client earning ₹30 lakh annually with credit score 780.
```

---

## Fraud Intelligence

```text
Generate risk assessment summary for a high-value international transfer flagged for review.
```

---

## Premium Banking

```text
Compare premium international banking cards offering concierge services and global lounge access.
```

---

## Estate Planning

```text
Recommend estate planning services for a multi-generational family office client.
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/AnshulMane/banking-rag-copilot.git
cd banking-rag-copilot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv myenv
```

```bash
.\myenv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install:

https://ollama.com

---

## 5. Pull Required Models

```bash
ollama pull phi3
```

```bash
ollama pull granite-embedding
```

---

## 6. Launch Application

```bash
streamlit run app.py
```

---

# Enterprise Design Goals

This project was designed to simulate AI-assisted workflows commonly explored in:

- private banking
- wealth management
- institutional AI copilots
- relationship management platforms
- enterprise knowledge systems

The focus was on:

- modular AI architecture
- local LLM deployment
- enterprise RAG pipelines
- security-aware AI workflows
- domain-specific retrieval systems

---

# Why This Project Matters

Most AI chatbot projects stop at simple conversational interfaces.

ASTOR focuses on:

- enterprise architecture
- domain-specific RAG
- institutional workflows
- privacy-aware AI systems
- real-world banking use cases

This project demonstrates applied skills across:

- Generative AI
- Retrieval-Augmented Generation
- AI system design
- vector databases
- enterprise AI workflows
- local LLM deployment
- security-aware AI engineering

---

# Author

## Anshul Mane
