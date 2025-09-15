# Chemical-Equation-Balancer-with-SMILES-Input
A Python tool that converts SMILES strings to chemical formulas and balances chemical equations using the [ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py) class from GitHub.

# Features
1. ```SMILES to Formula Conversion```: Convert SMILES strings to molecular formulas using RDKit
2. ```Chemical Equation Balancing```: Automatically balance chemical equations using matrix methods
3. ```Interactive Interface```: User-friendly command-line interface with helpful prompts
4. ```Work Display```: Option to show step-by-step balancing work
5. ```Error Handling```: Robust error handling for invalid SMILES and equations

# Installation
## 1. Install Required Dependencies
```bash
pip install rdkit-pypi
```

## 2. Install ChemEqBalancer from GitHub
Since ```ChemEqBalancer``` is not available on PyPI, install it directly from the [GitHub repository](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py):
```bash
pip install git+https://github.com/chaog5/Chemical_equation_balancer.git
```

## Alternative: Manual Installation
If the pip installation doesn't work, you can download the file manually from the [source](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py):
```bash
# Download the required file directly
curl -O https://raw.githubusercontent.com/chaog5/Chemical_equation_balancer/main/ChemEqBalancer.py

# Or clone the repository
git clone https://github.com/chaog5/Chemical_equation_balancer.git
cp Chemical_equation_balancer/ChemEqBalancer.py 
```

# Usage

## Basic usage
Run the main script:
```bash
python chemical_equation_balancer.py
```

## Input format
When prompted, enter SMILES strings separated by semicolons:

### For example:
Reactants:
```text
CCO;O=O
```
Products:
```text
C(=O)=O;O
```

## Example Session
```text
Chemical Equation Balancer with SMILES Input
Enter reactant and product SMILES when prompted
Enter "show work" to see balancing steps
Enter "q" to quit

Enter command or press Enter to input SMILES: 

==================================================
Input the reactant SMILES separated by ";": CCO;O=O
Input the product SMILES separated by ";": C(=O)=O;O

Unbalanced equation: C2H6O + O2 -> CO2 + H2O

Balanced equation: C2H6O + 3O2 -> 2CO2 + 3H2O
To show work, enter "show work". To quit, enter "q".

==================================================
Enter command or press Enter to input SMILES: show work

[Step-by-step balancing work display]

==================================================
Enter command or press Enter to input SMILES: q

Good-bye
```

# Available Commands
1. Press Enter to input new SMILES and balance equations
2. Type "show work" to see detailed balancing steps for the last equation
3. Type "q" to quit the program

# Supported SMILES Formats
1. ```Organic molecules```: CCO (ethanol), c1ccccc1 (benzene)
2. ```Inorganic compounds```: O=O (oxygen), N#N (nitrogen)
3. ```Ions```: [Na+], [Cl-]
4. ```Isotopes```: [2H]C([2H])([2H])O (deuterated methanol)

```Note```: Ahthough ions can be parsed by the ```smile_to_unbalanced_eq()``` function in this script, the [ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py) class cannot process ionic equations See [README.md](https://github.com/chaog5/Chemical_equation_balancer/blob/main/README.md).

# Code Structure
```text
├── chemical_equation_balancer.py  # Main application
├── ChemEqBalancer.py              # Balancing logic (from GitHub)
└── README.md                      # This file
```

# Key Functions
```smile_to_unbalanced_eq()```: Converts SMILES inputs to chemical equation string
```get_balanced_eq()```: Wrapper function for ChemEqBalancer
```main()```: Interactive command-line interface

# Examples
## Combustion Reaction
```text
Input: CCO;O=O -> C(=O)=O;O
Output: C2H6O + 3O2 -> 2CO2 + 3H2O
```

## Photosynthesis
```text
Input: O=C=O;O -> C6H12O6;O=O
Output: 6CO2 + 6H2O -> C6H12O6 + 6O2
```

## Acid-Base Reaction
```text
Input: [Na+].[OH-];O=C(O)O -> [Na+].[O-]C(O)=O;O
Output: NaOH + CH3COOH -> CH3COONa + H2O
```

# Dependencies
```RDKit```: Chemical informatics and SMILES parsing
```[ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py)```: Chemical equation balancing logic
```NumPy```: Matrix operations (included with [ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py))

# Troubleshooting
## Common issues
1. "Module not found" error for ChemEqBalancer
```bash
# Ensure proper installation from the GitHub repo
pip install git+https://github.com/chaog5/Chemical_equation_balancer.git
```

2. Invalid SMILES strings
<1> heck SMILES syntax using online validators
<2> Ensure proper use of brackets for special atoms

3. Balance fails for complex equations
<1> The balancer uses matrix methods that may not work for all reaction types, such as ionic equations (See [README.md](https://github.com/chaog5/Chemical_equation_balancer/blob/main/README.md) of [ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py))
<2> Try simplifying or breaking down complex reactions

## Debug Mode
For troubleshooting, you can add debug prints:
```python
# Add to see what's being processed
print(f"Processing SMILES: {smile}")
print(f"Generated formula: {formula}")
```

# License
1. ```RDKit```: BSD license
2. ```[ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py)```: MIT license (from original GitHub repository)

# Acknowledgments
1. ```RDKit``` team for the excellent cheminformatics toolkit
2. ```OpenSMILES``` community for maintaining SMILES standards

# Contributing
I am greatful if you can contribute by giving:
<1> Additional SMILES support
<2> Improved balancing algorithms
<3> Enhanced user interface features
<4> Better error handling and validation

# Author
Chao Gao, PhD (in chemistry)
[![GitHub](https://img.shields.io/badge/GitHub-@chaog5-blue?style=flat&logo=github)](https://github.com/chaog5)

```Note```: This tool is designed for educational purposes. Always verify balanced equations, especially for complex biochemical or industrial reactions. For more details, visit the original [ChemEqBalancer](https://github.com/chaog5/Chemical_equation_balancer/blob/main/ChemEqBalancer.py) repository.

