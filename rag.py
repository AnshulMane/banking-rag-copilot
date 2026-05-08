from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

def create_rag():

    files = [
        "data/loans.pdf",
        "data/credit_cards.pdf",
        "data/wealth_management.pdf",
        "data/fraud_policy.pdf"
    ]

    docs = []
    for f in files:
        docs.extend(PyPDFLoader(f).load())

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=30)
    chunks = splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        chunks,
        OllamaEmbeddings(model="granite-embedding")
    )

    retriever = vectordb.as_retriever()

    llm = Ollama(model="llama3")

    prompt = PromptTemplate(
        template="Context:\n{context}\n\nQuestion:\n{question}\nAnswer:",
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )