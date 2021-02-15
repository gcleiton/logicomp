"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from entities.formula import *
from utils.functions import atoms

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
    pass
    # ======== YOUR CODE HERE ========


