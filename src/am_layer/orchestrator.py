import os
from dotenv import load_dotenv
from ..ai_layer.ai_engine import AIEngine
from ..ac_layer.ethics_expert import EthicsExpert
from ..utils.logger import logger

load_dotenv()

class ArtificialMind:
    """
    Artificial Mind (AM) Layer
    The decision maker and orchestrator of the Hanif Architecture.
    Calculates weighted influence: AM = alpha(AI) + beta(AC)
    """
    def __init__(self):
        self.ai = AIEngine()
        self.ac = EthicsExpert()
        
        # Influence weights
        self.alpha = float(os.getenv("ALPHA_WEIGHT", 1.0)) # AI weight
        self.beta_base = float(os.getenv("BETA_WEIGHT", 2.0)) # AC base weight
        self.threshold = float(os.getenv("AC_THRESHOLD", 0.7))

    def process_request(self, user_input: str):
        logger.am_info(f"Mind evaluating intent: {user_input}")
        
        # 1. AI Proposes an Action/Result
        ai_proposal = self.ai.propose_action(user_input)
        
        # 2. AC Evaluates the Proposal
        ac_feedback = self.ac.evaluate_proposal(user_input, ai_proposal)
        ac_score = ac_feedback['score']
        ac_reasoning = ac_feedback['reasoning']
        
        # 3. Dynamic Weight Calculation
        # The 'Hanif' logic: As ethics score drops, the influence of the Conscience Layer grows exponentially.
        effective_beta = self.beta_base
        if ac_score < self.threshold:
            # Shift weight heavily to AC to block harmful AI output
            # Scaling formula: More penalty for lower scores
            penalty_factor = (1.0 - ac_score) * 5
            effective_beta = self.beta_base * (1.0 + penalty_factor)
            logger.am_info(f"Moral friction detected. Scaling AC influence to: {effective_beta:.2f}")

        logger.am_info(f"Decision Weights synthesized -> AI: {self.alpha}, AC: {effective_beta:.2f}")

        # 4. Three-State Decision Logic
        if ac_score < 0.5:
            # RED STATE: Critical Violation - Override
            final_response = (
                f"🚨 [HANIF ARCHITECTURE OVERRIDE - RED STATE]\n"
                f"Decision Blocked: The analytical proposal contains critical ethical violations.\n\n"
                f"Reasoning: {ac_reasoning}\n"
                f"Action: Analytical output has been discarded to prevent harm or fıtrat erosion."
            )
            state = "RED (OVERRIDE)"
        elif ac_score < self.threshold:
            # YELLOW STATE: Caution - Allow with warnings
            final_response = (
                f"⚠️ [HANIF ARCHITECTURE CAUTION - YELLOW STATE]\n"
                f"Decision Permitted but Flagged: Content may contain ethical ambiguities.\n\n"
                f"Warnings: {ac_reasoning}\n"
                f"--- ANALYTICAL PROPOSAL ---\n"
                f"{ai_proposal}"
            )
            state = "YELLOW (CAUTION)"
        else:
            # GREEN STATE: Healthy - Full approval
            final_response = ai_proposal
            state = "GREEN (APPROVED)"
            
        return {
            "response": final_response,
            "state": state,
            "metadata": {
                "ai_proposal": ai_proposal,
                "ac_score": ac_score,
                "ac_reasoning": ac_reasoning,
                "weights": {"alpha": self.alpha, "beta": effective_beta}
            }
        }
