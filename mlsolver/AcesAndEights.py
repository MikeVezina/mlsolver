""" Three wise men puzzle

Module contains data model for three wise men puzzle as Kripke strukture and agents announcements as modal logic
formulas
"""
import copy
from mlsolver.kripke import KripkeStructure, World
from mlsolver.formula import Atom, And, Not, Or, Box_a, Box_star


class AcesAndEights:
    """
    Class models the Kripke structure of the "Three wise men example.
    """

    knowledge_base = []

    def __init__(self):
        worlds = [
            World('1AA_2AA_388', {'1AA': True, '2AA': True, '388': True}),
            World('1AA_2A8_3A8', {'1AA': True, '2A8': True, '3A8': True}),
            World('1AA_2A8_388', {'1AA': True, '2A8': True, '388': True}),
            World('1AA_288_3AA', {'1AA': True, '288': True, '3AA': True}),
            World('1AA_288_3A8', {'1AA': True, '288': True, '3A8': True}),
            World('1AA_288_388', {'1AA': True, '288': True, '388': True}),

            World('1A8_2AA_3A8', {'1A8': True, '2AA': True, '3A8': True}),
            World('1A8_2AA_388', {'1A8': True, '2AA': True, '388': True}),
            World('1A8_2A8_3AA', {'1A8': True, '2A8': True, '3AA': True}),
            World('1A8_2A8_3A8', {'1A8': True, '2A8': True, '3A8': True}),
            World('1A8_2A8_388', {'1A8': True, '2A8': True, '388': True}),
            World('1A8_288_3AA', {'1A8': True, '288': True, '3AA': True}),
            World('1A8_288_3A8', {'1A8': True, '288': True, '3A8': True}),

            World('188_2AA_3AA', {'188': True, '2AA': True, '3AA': True}),
            World('188_2AA_3A8', {'188': True, '2AA': True, '3A8': True}),
            World('188_2AA_388', {'188': True, '2AA': True, '388': True}),
            World('188_2A8_3AA', {'188': True, '2A8': True, '3AA': True}),
            World('188_2A8_3A8', {'188': True, '2A8': True, '3A8': True}),
            World('188_288_3AA', {'188': True, '288': True, '3AA': True})
        ]

        relations = {
            '1':
                {
                    ('1A8_2AA_3A8', '188_2AA_3A8'),
                    ('1AA_2AA_388', '1A8_2AA_388'), ('1AA_2AA_388', '188_2AA_388'), ('1A8_2AA_388', '188_2AA_388'),

                    ('1A8_2A8_3AA', '188_2A8_3AA'),
                    ('1AA_2A8_3A8', '1A8_2A8_3A8'), ('1AA_2A8_3A8', '188_2A8_3A8'), ('1A8_2A8_3A8', '188_2A8_3A8'),
                    ('1AA_2A8_388', '1A8_2A8_388'),

                    ('1AA_288_3AA', '1A8_288_3AA'), ('1AA_288_3AA', '188_288_3AA'), ('1A8_288_3AA', '188_288_3AA'),
                    ('1AA_288_3A8', '1A8_288_3A8')
                },

            '2':
                {
                    ('1AA_2AA_388', '1AA_2A8_388'), ('1AA_2AA_388', '1AA_288_388'), ('1AA_2A8_388', '1AA_288_388'),
                    ('1AA_2A8_3A8', '1AA_288_3A8'),

                    ('1A8_2AA_3A8', '1A8_2A8_3A8'), ('1A8_2AA_3A8', '1A8_288_3A8'), ('1A8_2A8_3A8', '1A8_288_3A8'),
                    ('1A8_2AA_388', '1A8_2A8_388'),
                    ('1A8_2A8_3AA', '1A8_288_3AA'),

                    ('188_2AA_3AA', '188_2A8_3AA'), ('188_2AA_3AA', '188_288_3AA'), ('188_2A8_3AA', '188_288_3AA'),
                    ('188_2AA_3A8', '188_2A8_3A8'),
                },

            '3':
                {
                    ('1AA_2A8_3A8', '1AA_2A8_3A8'),
                    ('1AA_288_3AA', '1AA_288_3A8'), ('1AA_288_3AA', '1AA_288_388'), ('1AA_288_3A8', '1AA_288_388'),

                    ('1A8_2AA_3A8', '1A8_2AA_388'),
                    ('1A8_2A8_3AA', '1A8_2A8_3A8'), ('1A8_2A8_3AA', '1A8_2A8_388'), ('1A8_2A8_3A8', '1A8_2A8_388'),
                    ('188_2A8_3AA', '188_2A8_3A8'),

                }
        }

        relations.update(add_reflexive_edges(worlds, relations))
        relations.update(add_symmetric_edges(relations))

        self.ks = KripkeStructure(worlds, relations)
        print(copy.deepcopy(relations))

        #print(self.ks.worlds.copy())

        # # Wise man ONE does not know whether he wears a red hat or not
        # self.knowledge_base.append(And(Not(Box_a('1', Atom('1:R'))), Not(Box_a('1', Not(Atom('1:R'))))))
        #
        # # This announcement implies that either second or third wise man wears a red hat.
        # self.knowledge_base.append(Box_star(Or(Atom('2:R'), Atom('3:R'))))
        #
        # # Wise man TWO does not know whether he wears a red hat or not
        # self.knowledge_base.append(And(Not(Box_a('2', Atom('2:R'))), Not(Box_a('2', Not(Atom('2:R'))))))
        #
        # # This announcement implies that third men has be the one, who wears a red hat
        # self.knowledge_base.append(Box_a('3', Atom('3:R')))


def add_symmetric_edges(relations):
    """Routine adds symmetric edges to Kripke frame
    """
    result = {}
    for agent, agents_relations in relations.items():
        result_agents = agents_relations.copy()
        for r in agents_relations:
            x, y = r[1], r[0]
            result_agents.add((x, y))
        result[agent] = result_agents
    return result


def add_reflexive_edges(worlds, relations):
    """Routine adds reflexive edges to Kripke frame
    """
    result = {}
    for agent, agents_relations in relations.items():
        result_agents = agents_relations.copy()
        for world in worlds:
            result_agents.add((world.name, world.name))
            result[agent] = result_agents
    return result
