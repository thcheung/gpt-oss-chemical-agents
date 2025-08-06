# GPT-OSS Chemical Agents

This project provides a Python-based assistant agent that leverages RDKit for cheminformatics tasks. The agent is powered by the GPT-OSS model and can perform various molecular computations, such as calculating molecular weight, validating SMILES strings, and determining logP values.

## Features

- **Molecular Weight Calculation**: Computes the molecular weight of a molecule given its SMILES string.
- **SMILES Validation**: Validates whether a given SMILES string is valid.
- **LogP Calculation**: Calculates the logP (partition coefficient) of a molecule based on its SMILES string.

## Requirements

- Python 3.8 or higher
- RDKit
- OpenAI's Agent SDK

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thcheung/gpt-oss-chemical-agents
   cd gpt-oss-chemical-agents
   ```

2. Install the required dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the assistant agent with the following command:

```bash
python main.py --api_key <your_api_key> --base_url <base_url> --model <model_name>
```

### Arguments

- `--api_key`: API key for the OpenAI client (default: `ollama`).
- `--base_url`: Base URL for the OpenAI client (default: `http://localhost:11434/v1`).
- `--model`: Model name for the OpenAI client (default: `gpt-oss:20b`).

### Example Queries

The agent can handle queries such as:

1. **Calculate Molecular Weight**:
   ```
   Calculate the molecular weight of the molecule with SMILES CC(=O)OC1=CC=CC=C1C(=O)O
   ```

2. **Validate SMILES**:
   ```
   Is the SMILES string C1CCCCC1 valid?
   ```

3. **Calculate LogP**:
   ```
   What is the logP of the molecule with SMILES CCO?
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [RDKit](https://www.rdkit.org/) for cheminformatics tools.
- [OpenAI](https://openai.com/) for the GPT-OSS model.
