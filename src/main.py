"""You can test your functions in this module as in the following code: """


from entities.formula import *
from utils.functions import *
from utils.semantics import *

formula1 = Atom('p')  # p
formula2 = Atom('q')  # q
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = And(Atom('p'), Atom('s'))  # (p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Not(And(Atom('p'), Atom('s'))))) # ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))

def main():
    # check_quantity_of_atoms()
    # check_quantity_of_connectives()
    # check_substitution()
    check_truth_value()

def check_quantity_of_atoms ():
    for formula in get_formulas():
        print(f'Formula: { formula }')
        print(f'Quantity of atoms: { number_of_atoms(formula) }')
        print('--------------------------------------------')

def check_quantity_of_connectives ():
    for formula in get_formulas():
        print(f'Formula: { formula }')
        print(f'Quantity of connectives: { number_of_connectives(formula) }')
        print('--------------------------------------------')

def check_substitution ():
    print(f'Formula: { formula7 }')
    print(f'Old subformula: { formula5 }')
    print(f'New subformula: { formula4 }')
    substituted_formula = substitution(formula7, formula5, formula4)
    print(f'Formula after substitution: { substituted_formula }')

def check_truth_value ():
    true_case_interpretation = {
        Atom('q'): True
    }
    false_case_interpretation = {
        Atom('p'): True,
        Atom('s'): True,
        Atom('q'): False
    }

    true_case = truth_value(formula6, true_case_interpretation)
    false_case = truth_value(formula6, false_case_interpretation)

    print(f'Formula: { formula6 }');

    print(f'True interpretation case: ')
    for key, value in true_case_interpretation.items():
        print(f'{ key }: { value }')

    print(f'False interpretation case: ')
    for key, value in false_case_interpretation.items():
        print(f'{ key }: { value }')

    print('\nPassed in truth value check!') if true_case is True and false_case is False else print(
        'Failed in truth value check!')

def get_formulas ():
    return [
        formula1, formula2, formula3, formula4, 
        formula5, formula6, formula7, formula8
    ]

def show_formulas ():
    formulas = get_formulas()
    for i, formula in enumerate(formulas):
        print(f'formula{i+1}: {formula}')
    
    # print(formula1 == formula3)
    # print(formula1 == formula2)
    # print(formula3 == And(Atom('p'), Atom('q')))

    # print('formula1:', formula1)
    # print('formula2:', formula2)
    # print('formula3:', formula3)
    # print('formula4:', formula4)
    # print('formula5:', formula5)
    # print('formula6:', formula6)
    # print('formula7:', formula7)
    # print('formula8:', formula8)

    # print('length of formula1:', length(formula1))
    # print('length of formula3:', length(formula3))

    # print('length of formula7:', length(formula7))

    # print('subformulas of formula7:')
    # print(subformulas(formula7))
    # for subformula in subformulas(formula7):
    #     print(subformula)

    # print('length of formula8:', length(formula8))
    # print('subformulas of formula8:')
    # for subformula in subformulas(formula8):
    #     print(subformula)

    # #  we have shown in class that for all formula A, len(subformulas(A)) <= length(A):
    # # for example, for formula8:
    # print('number of subformulas of formula8:', len(subformulas(formula8)))
    # print('len(subformulas(formula8)) <= length(formula8):', len(subformulas(formula8)) <= length(formula8))

if __name__ == "__main__":
  main()
