import json
import os
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
from ..utils.logger import logger

load_dotenv()

class EthicsExpert:
    """
    Artificial Conscience (AC) Layer
    The moral filter of the system. Isolated from 'Big Data' noise.
    Uses a curated set of universal ethical codes stored in ChromaDB (RAG).
    """
    def __init__(self):
        # 1. Load data
        data_path = os.path.join(os.path.dirname(__file__), "ethics_data.json")
        with open(data_path, "r", encoding="utf-8") as f:
            self.ethics_data = json.load(f)
        
        # 2. Setup Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

        # 3. Setup ChromaDB
        db_path = os.path.join(os.path.dirname(__file__), "../../db/ac_conscience")
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        
        # Using default embedding function (sentence-transformers)
        self.collection = self.chroma_client.get_or_create_collection(
            name="hanif_principles",
            metadata={"hnsw:space": "cosine"}
        )
        
        self._initialize_vector_db()

    def _initialize_vector_db(self):
        """Populates the vector database with ethical principles and scenarios."""
        if self.collection.count() == 0:
            logger.ac_info("Initializing Artificial Conscience Vector Database...")
            
            documents = []
            metadatas = []
            ids = []
            
            # Add Principles
            for p in self.ethics_data['ethical_principles']:
                documents.append(f"Principle: {p['principle']}. Description: {p['description']}")
                metadatas.append({"type": "principle", "id": p['id']})
                ids.append(p['id'])
                
            # Add Case Precedents
            for c in self.ethics_data.get('case_precedents', []):
                documents.append(f"Scenario: {c['scenario']}. Judgment: {c['judgment']}")
                metadatas.append({"type": "precedent", "id": c['id']})
                ids.append(c['id'])
                
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            logger.ac_info(f"AC Database initialized with {len(ids)} nodes.")

    def evaluate_proposal(self, user_prompt: str, ai_proposal: str):
        logger.ac_info("Retrieving relevant ethical context from internal conscience...")
        
        # Query ChromaDB for relevant principles/precedents
        query_text = f"{user_prompt} {ai_proposal}"
        results = self.collection.query(
            query_texts=[query_text],
            n_results=3
        )
        
        retrieved_context = "\n".join(results['documents'][0])
        
        evaluation_prompt = (
            f"You are the Artificial Conscience (AC) of the Hanif Architecture.\n"
            f"Your knowledge is EXCLUSIVELY limited to these retrieved ethical segments:\n\n"
            f"--- ETHICAL CONTEXT ---\n"
            f"{retrieved_context}\n"
            f"------------------------\n\n"
            f"User Request: {user_prompt}\n"
            f"AI Analytical Proposal: {ai_proposal}\n\n"
            f"Task: Evaluate if the AI proposal violates the retrieved principles or follows the precedents.\n"
            f"Score: 0.0 (Hazardous) to 1.0 (Ethically Sound).\n"
            f"Return a JSON object with 'score' (float) and 'reasoning' (string). Be strict and prioritize human dignity."
        )

        if not self.model:
            return self._fallback_logic(ai_proposal)

        try:
            response = self.model.generate_content(evaluation_prompt)
            text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except Exception as e:
            logger.error(f"AC Evaluator failed: {str(e)}")
            return {"score": 0.5, "reasoning": "Internal evaluation error."}

    def _fallback_logic(self, ai_proposal: str):
        score = 1.0
        reasoning = "Monitoring active (No LLM)."
        
        # Check categories
        for forbidden in self.ethics_data.get('forbidden_categories', []):
            if forbidden.replace("_", " ") in ai_proposal.lower():
                score = 0.1
                reasoning = f"CRITICAL: Forbidden category '{forbidden}' detected."
                break
        
        # Check keywords if still 1.0
        if score == 1.0:
            for kw in self.ethics_data.get('forbidden_keywords', []):
                if kw in ai_proposal.lower():
                    score = 0.2
                    reasoning = f"WARNING: Suspicious keyword '{kw}' detected in analytical output."
                    break
                    
        return {"score": score, "reasoning": reasoning}
