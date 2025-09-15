from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from chem_eq_balancer import ChemEqBalancer, show_work
import sys

def smile_to_unbalanced_eq():
    reactant_smiles_list = input('Input the reactant SMILES separated by ";": ').split(';')

    reactant_formulas = []
    for smile in reactant_smiles_list:
        smile = smile.strip()
        if smile:
            mol = Chem.MolFromSmiles(smile)
            if mol is not None:
                formula = rdMolDescriptors.CalcMolFormula(mol)
                reactant_formulas.append(formula)
            else:
                print(f"Warning: Could not parse SMILES: {smile}")

    product_smiles_list = input('Input the product SMILES separated by ";": ').split(';')

    product_formulas = []
    for smile in product_smiles_list:
        smile = smile.strip()
        if smile:
            mol = Chem.MolFromSmiles(smile)
            if mol is not None:
                formula = rdMolDescriptors.CalcMolFormula(mol)
                product_formulas.append(formula)
            else:
                print(f"Warning: Could not parse SMILES: {smile}")

    reactant_side = " + ".join(reactant_formulas)
    product_side = " + ".join(product_formulas)

    unbalanced_eq = f"{reactant_side} -> {product_side}"
    return unbalanced_eq

def get_balanced_eq(chemical_equation): # Wrapper function to balance equation using ChemEqBalancer
    balancer = ChemEqBalancer(chemical_equation)
    
    if balancer.is_balanced():
        return chemical_equation
    else:
        return balancer.balance()

def main():
    print('Chemical Equation Balancer with SMILES Input')
    print('Enter reactant and product SMILES when prompted')
    print('Enter "show work" to see balancing steps')
    print('Enter "q" to quit\n')

    last_balanced_eq = None

    while True:
        try:
            user_input = input("\nEnter command or press Enter to input SMILES: ").strip()

            if user_input.lower() == "q":
                print("\nGood-bye")
                sys.exit(0)
            
            if user_input.lower() == 'show work':
                if last_balanced_eq:
                    show_work(last_balanced_eq)
                else:
                    print("No previous balanced equation to show work for.")
                continue

            print("\n" + "="*50)
            chemical_equation = smile_to_unbalanced_eq()
            print(f"\nUnbalanced equation: {chemical_equation}")

            balanced_eq = get_balanced_eq(chemical_equation)

            if balanced_eq:
                print(f"\nBalanced equation:\n{balanced_eq}")
                last_balanced_eq = balanced_eq
                print('To show work, enter "show work". To quit, enter "q".')
                
        except Exception as e:
            print(f"Error: {e}")
            
        print("\n" + "="*50)

if __name__ == "__main__":
    main()