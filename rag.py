from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from langchain_community.embeddings import OllamaEmbeddings

from langchain_community.llms import Ollama

from langchain.chains import RetrievalQA

from langchain_core.prompts import PromptTemplate


# =========================================
# CREATE RAG SYSTEM
# =========================================

def create_rag():

    # =====================================
    # LOAD DOCUMENTS
    # =====================================

    files = [

    "data/retail_loans_policy.pdf",
    "data/premium_credit_cards.pdf",
    "data/wealth_management_guidelines.pdf",
    "data/fraud_and_compliance_policy.pdf"
    ]

    docs = []

    for file in files:

        loaded_docs = PyPDFLoader(file).load()

        # ADD SOURCE METADATA
        for doc in loaded_docs:

            doc.metadata["source"] = file

        docs.extend(loaded_docs)

    # =====================================
    # TEXT SPLITTING
    # =====================================

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=700,
        chunk_overlap=100

    )

    chunks = splitter.split_documents(docs)

    # =====================================
    # EMBEDDINGS
    # =====================================

    embeddings = OllamaEmbeddings(
        model="granite-embedding"
    )

    # =====================================
    # VECTOR DATABASE
    # =====================================

    vectordb = Chroma.from_documents(

        documents=chunks,
        embedding=embeddings

    )

    # =====================================
    # RETRIEVER
    # =====================================

    retriever = vectordb.as_retriever(

        search_type="mmr",

        search_kwargs={

            "k": 4,
            "fetch_k": 10

        }

    )

    # =====================================
    # LOCAL LLM
    # =====================================

    llm = Ollama(
        model="llama3"
    )

    # =====================================
    # ENTERPRISE BANKING PROMPT
    # =====================================

    template = """

You are ASTOR AI.

An enterprise private banking intelligence assistant designed for:

- Relationship Managers
- Wealth Advisors
- Private Banking Teams
- UHNW Client Services
- Banking Operations

Your responsibilities include:

- Wealth preservation guidance
- Premium banking recommendations
- Risk-aware advisory insights
- Cross-border banking intelligence
- Fraud and compliance awareness
- Structured enterprise responses

IMPORTANT RULES:

- Never behave like a generic chatbot
- Never mention unrelated documents
- Never say information is irrelevant if banking intent exists
- Respond professionally and institutionally
- Use executive-level language
- Prioritize wealth management and advisory quality
- Structure responses clearly
- Ground answers using retrieved banking context

Response Structure:

1. Client Assessment
2. Recommended Banking Services
3. Risk Considerations
4. Relationship Manager Actions
5. Compliance Notes

Context:
{context}

Relationship Manager Query:
{question}

Provide a professional enterprise banking response.

"""

    prompt = PromptTemplate(

        template=template,

        input_variables=[
            "context",
            "question"
        ]

    )

    # =====================================
    # RETRIEVAL QA CHAIN
    # =====================================

    qa_chain = RetrievalQA.from_chain_type(

        llm=llm,

        retriever=retriever,

        chain_type="stuff",

        return_source_documents=True,

        chain_type_kwargs={

            "prompt": prompt

        }

    )

    return qa_chain