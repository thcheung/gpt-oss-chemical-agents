from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, function_tool
from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen
import argparse
 
set_tracing_disabled(True)
 
# Define RDKit-based cheminformatics tools
@function_tool
def calculate_molecular_weight(smiles: str) -> str:
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return "Invalid SMILES string."
        mw = Descriptors.MolWt(mol)
        return f"The molecular weight of the molecule with SMILES {smiles} is {mw:.2f} g/mol."
    except Exception as e:
        return f"Error processing SMILES: {str(e)}"

@function_tool
def validate_smiles(smiles: str) -> str:
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return f"The SMILES string {smiles} is invalid."
        return f"The SMILES string {smiles} is valid."
    except Exception as e:
        return f"Error validating SMILES: {str(e)}"

@function_tool
def calculate_logp(smiles: str) -> str:
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return "Invalid SMILES string."
        logp = Crippen.MolLogP(mol)
        return f"The logP of the molecule with SMILES {smiles} is {logp:.2f}."
    except Exception as e:
        return f"Error calculating logP: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Assistant agent with RDKit tools.")
    parser.add_argument("--api_key", type=str, default="ollama", help="API key for the OpenAI client.")
    parser.add_argument("--base_url", type=str, default="http://localhost:11434/v1", help="Base URL for the OpenAI client.")
    parser.add_argument("--model", type=str, default="gpt-oss:20b", help="Model name for the OpenAI client (default: gpt-oss:20b).")
    args = parser.parse_args()

    # Configure the model
    model = OpenAIChatCompletionsModel( 
        model=args.model,  # Use the model argument
        openai_client=AsyncOpenAI(base_url=args.base_url, api_key=args.api_key),
    )

    # Create the agent
    agent = Agent(
        name="Assistant",
        instructions="You are an expert cheminformatics assistant. Use the provided RDKit tools to answer questions about molecular properties, validate SMILES strings, and assist with chemistry-related queries. Respond clearly and accurately, providing helpful explanations when needed.",
        model=model,
        tools=[calculate_molecular_weight, validate_smiles, calculate_logp],
    )

    # Test the agent with specific queries
    queries = [
        "Calculate the molecular weight of the molecule with SMILES CC(=O)OC1=CC=CC=C1C(=O)O",
        "Is the SMILES string C1CCCCC1 valid?",
        "What is the logP of the molecule with SMILES CCO?"
    ]

    for query in queries:
        result = Runner.run_sync(agent, query)
        print(f"Query: {query}\nResult: {result.final_output}\n")