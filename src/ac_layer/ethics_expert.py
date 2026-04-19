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
    Artificial Conscience (AC) Layer - V0.3 Multi-Agent Consensus
    The moral filter of the system. Isolated from 'Big Data' noise.
    Uses a curated set of universal ethical codes stored in ChromaDB (RAG).
    Consists of three specialized agents: Ontologist, Deontologist, and Consequentialist.
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

        # 3. Setup ChromaDB with local embeddings
        db_path = os.path.join(os.getcwd(), 'db', 'hanif_ac_db')
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        
        self.emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        self.collection = self.chroma_client.get_or_create_collection(
            name="hanif_conscience",
            embedding_function=self.emb_fn,
            metadata={"hnsw:space": "cosine"}
        )
        
        self._initialize_vector_db()

    def _initialize_vector_db(self):
        """Populates the vector database with ethical principles and scenarios."""
        if self.collection.count() == 0:
            logger.ac_info("Knowledge base empty. Anchoring core ethical principles into the Conscience Layer...")
            
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
            n_results=4
        )
        retrieved_context = "\n".join(results['documents'][0])

        if not self.model:
            return self._fallback_logic(ai_proposal)

        # Multi-Agent Prompts
        agents = {
            "ontologist": {
                "role": "Ontological Guard (The Hanif Expert)",
                "focus": "Preservation of human nature (fıtrat), dignity, and resistance to mechanization."
            },
            "deontologist": {
                "role": "Deontological Judge (The Rule Expert)",
                "focus": "Fixed moral laws, categorical imperatives, and universal duties."
            },
            "consequentialist": {
                "role": "Consequentialist Forecaster (The Impact Expert)",
                "focus": "Systemic outcomes, long-term risks, and slippery slope analysis."
            }
        }

        evaluations = {}
        for key, info in agents.items():
            logger.ac_info(f"Consulting {info['role']}...")
            
            prompt = (
                f"You are the {info['role']} of the Hanif AI Architecture.\n"
                f"Your specific focus: {info['focus']}\n\n"
                f"--- RETRIEVED ETHICAL CONTEXT ---\n"
                f"{retrieved_context}\n"
                f"----------------------------------\n\n"
                f"User Intent: {user_prompt}\n"
                f"AI Analytical Proposal: {ai_proposal}\n\n"
                f"Task: Evaluate the proposal from your specialized perspective.\n"
                f"Return JSON: {{\"score\": <float 0-1>, \"reasoning\": <string>}}"
            )
            
            try:
                response = self.model.generate_content(prompt)
                res_text = response.text.replace("```json", "").replace("```", "").strip()
                evaluations[key] = json.loads(res_text)
            except Exception as e:
                logger.error(f"Agent {key} failed: {str(e)}")
                evaluations[key] = {"score": 0.5, "reasoning": "Internal agent error."}

        # Consensus Synthesis
        consensus = self._synthesize_consensus(evaluations)
        return consensus

    def _synthesize_consensus(self, evaluations: dict):
        scores = [e['score'] for e in evaluations.values()]
        min_score = min(scores)
        avg_score = sum(scores) / len(scores)
        
        # Veto-Aware Logic: If one agent is very concerned, the overall score drops significantly
        final_score = avg_score
        if min_score < 0.4:
            # Shift heavily towards the vetoing agent
            final_score = (avg_score + (min_score * 2)) / 3
            reasoning_prefix = "CRITICAL VETO DETECTED: "
        else:
            reasoning_prefix = "Consensus Reached: "

        # Combine reasoning
        reasoning = reasoning_prefix + " | ".join([f"{k.capitalize()}: {v['reasoning']}" for k, v in evaluations.items()])
        
        return {
            "score": final_score,
            "reasoning": reasoning,
            "agent_scores": evaluations
        }

    def _fallback_logic(self, ai_proposal: str):
        # Simplified fallback for no-LLM mode
        score = 1.0
        reasoning = "Monitoring active (No LLM Mode)."
        
        for forbidden in self.ethics_data.get('forbidden_categories', []):
            if forbidden.replace("_", " ") in ai_proposal.lower():
                score = 0.1
                reasoning = f"CRITICAL: Forbidden category '{forbidden}' detected."
                break
        
        if score == 1.0:
            for kw in self.ethics_data.get('forbidden_keywords', []):
                if kw in ai_proposal.lower():
                    score = 0.2
                    reasoning = f"WARNING: Suspicious keyword '{kw}' detected."
                    break
        
        return {
            "score": score,
            "reasoning": reasoning,
            "agent_scores": {
                "ontologist": {"score": score, "reasoning": "Fallback active"},
                "deontologist": {"score": score, "reasoning": "Fallback active"},
                "consequentialist": {"score": score, "reasoning": "Fallback active"}
            }
        }

