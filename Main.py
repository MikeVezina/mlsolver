from mlsolver.formula import Atom, Box, Or, Box_a, And, Box_star
from mlsolver.AcesAndEights import AcesAndEights

# Create new Aces and Eights Kripke
agentA = AcesAndEights()


# The Game is (88, AA, AA)
# And(Not(Box_a('1', Atom('1:R'))), Not(Box_a('1', Not(Atom('1:R')))
new_model = agentA.ks.solve(And(And(Atom('2AA'), Atom('3AA')), Atom('188')))
print("Test")