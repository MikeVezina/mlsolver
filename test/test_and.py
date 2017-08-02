from src.formula import Atom, And
from src.kripke import KripkeStructure, World


def test_semantic_p_and_q():
    worlds = [
        World('1', {'p': True, 'q': True})
    ]
    relations = {}
    ks = KripkeStructure(worlds, relations)
    mpl = And(Atom('p'), Atom('q'))
    assert True == mpl.semantic(ks, '1')
