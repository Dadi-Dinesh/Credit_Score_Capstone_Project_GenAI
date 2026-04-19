import os
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

# Explicitly check and set if needed
if "GROQ_API_KEY" in os.environ:
    api_key = os.environ["GROQ_API_KEY"]
else:
    # Try reading directly from .env if load_dotenv failed
    api_key = ""

from agent_pipeline import run_per_agent, print_per_trace, save_graph_visualization

def test_pipeline():
    # Sample applicant data
    applicant = {
        "age": 25,
        "income": 45000,
        "home_ownership": "RENT",
        "employment_years": 3,
        "loan_intent": "EDUCATION",
        "loan_amount": 10000,
        "interest_rate": 11.5
    }

    print("Starting LangGraph Pipeline Verification...")
    
    try:
        # Generate visualization first
        save_graph_visualization("graph.md")
        
        # Run the agent
        state = run_per_agent(applicant, verbose=True)
        
        # Print trace
        print_per_trace(state)
        
        print("\nVerification Successful!")
        return True
    except Exception as e:
        print(f"\nVerification Failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_pipeline()
