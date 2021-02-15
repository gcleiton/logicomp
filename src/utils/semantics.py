"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from entities.formula import *
from utils.functions import atoms
from .common import *

def truth_value(formula: Formula, interpretation: dict):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    if isinstance(formula, Atom):
        return interpretation[formula] if interpretation.__contains__(formula) else None

    if isinstance(formula, Not):
        value = truth_value(formula.inner, interpretation)
        return None if value is None else not value

    if isinstance(formula, Implies):
        left = truth_value(formula.left, interpretation)
        right = truth_value(formula.right, interpretation)

        return False if left and not right else None if left is None else True

    if isinstance(formula, And):
        left = truth_value(formula.left, interpretation)
        right = truth_value(formula.right, interpretation)

        return True if left and right else None if left is None or right is None else False

    if isinstance(formula, Or):
        left = truth_value(formula.left, interpretation)
        right = truth_value(formula.right, interpretation)

        return True if left or right else None if left is None or right is None else False


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def is_satisfiable(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    

def is_satisfiable(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    atom_list = atoms(formula)
    initial_interpretation = generate_initial_interpretation(formula)

    if initial_interpretation:
        new_atom_list = generate_new_atoms(atom_list, initial_interpretation)
        return get_satisfability_interpretation(formula, new_atom_list, initial_interpretation)
        
    else:
        return get_satisfability_interpretation(formula, atom_list, {})

def generate_new_atoms (atoms_list, interpretation):
    new_atoms = []

    for atom in atoms_list: 
        if atom not in interpretation:
            new_atoms.append(atom)
        
    return new_atoms

def generate_initial_interpretation (formula):
    if isinstance(formula, Atom):
        return { formula: True }

    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return { formula.inner: False }
        # return generate_initial_interpretation(formula.inner)

    if isinstance(formula, And):
        left = generate_initial_interpretation(formula.left)
        right = generate_initial_interpretation(formula.right)
        
        if left and right: # a ^ b -> a: True, b: True
            return union_dict(left, right)
        
        return left if left else right # a ^ (!(b ^ c)) -> a: True, !(b ^ c) não é possível determinar

    return None # retorna None se nenhuma condição for satisfeita

def get_satisfability_interpretation (formula, atoms: dict, interpretation: dict):
    if not atoms:
        output = truth_value(formula, interpretation)
        return interpretation if output else False

    removed_atom = atoms.pop()
    true_interpretation = union_dict(interpretation, {
        removed_atom: True
    })
    false_interpretation = union_dict(interpretation, {
        removed_atom: False
    })

    result = get_satisfability_interpretation(formula, atoms.copy(), true_interpretation)

    return result if result else get_satisfability_interpretation(formula, atoms.copy(), false_interpretation)
