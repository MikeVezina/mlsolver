from itertools import chain, combinations


class KripkeStructure:
    """
    This class describes a Kripke Frame with it's possible worlds and their transition relation.
    """

    def __init__(self, worlds, relations):
        if not isinstance(worlds, list) or isinstance(worlds[0], World):
            self.worlds = worlds
            self.relations = relations
        else:
            raise TypeError

    # Removes minimum sub set of nodes, therefore formula is satisfiable in each node of Kripke structure.
    def solve(self, formula):
        # print(self.nodes_not_follow_formula(formula))#TODO
        # print(self.__get_power_set_of_worlds__())  # TODO
        ks = []
        for i, subset in enumerate(self.__get_power_set_of_worlds__()):
            ks.append(KripkeStructure(self.worlds, self.relations))
            for element in subset:
                ks[i]._remove_node_by_name(element)
            print(ks[i].nodes_not_follow_formula(formula))  # TODO
            print(subset)  # TODO
            for w in ks[i].worlds:  # TODO
                print(w.name)  # TODO
            print()  # TODO
            if ks[i].nodes_not_follow_formula(formula) == []:
                return ks[i]

    # Removes ONE node of Kripke frame, therefore we can make knowledge base consistent with announcement.
    def _remove_node_by_name(self, node_name):

        # make copy, because change while iteration
        for world in self.worlds.copy():
            if node_name == world.name:
                self.worlds.remove(world)

        if isinstance(self.relations, set):
            for (start_node, end_node) in self.relations.copy():
                if start_node == node_name or end_node == node_name:
                    self.relations.remove((start_node, end_node))

        if isinstance(self.relations, dict):
            for key, value in self.relations.items():
                for (start_node, end_node) in value.copy():
                    if start_node == node_name or end_node == node_name:
                        value.remove((start_node, end_node))

    # Returns a list with all possible sub sets of world names, sorted by ascending number of their elements.
    def __get_power_set_of_worlds__(self):
        sub_set = [{}]
        worlds_by_name = []

        for w in self.worlds:
            worlds_by_name.append(w.name)

        for z in chain.from_iterable(combinations(worlds_by_name, r + 1) for r in range(len(worlds_by_name) + 1)):
            sub_set.append(set(z))
        return sub_set

    # Returns a list with all worlds of Kripke structure, where formula is not satisfiable
    def nodes_not_follow_formula(self, formula):
        nodes_not_follow_formula = []
        for nodes in self.worlds:
            if not formula.semantic(self, nodes.name):
                nodes_not_follow_formula.append(nodes.name)
        return nodes_not_follow_formula

    def __eq__(self, other):
        for (i, j) in zip(self.worlds, other.worlds):
            if not i.__eq__(j):
                return False

        if isinstance(self.relations, set):
            for (i, j) in zip(self.relations, other.relations):
                if not i == j:
                    return False

        if isinstance(self.relations, dict):
            for key, value in self.relations.items():
                try:
                    if not value == other.relations[key]:
                        return False
                except KeyError:
                    if not value == set():
                        return False

        return True


class World:
    """
    Represents the nodes of Kripke and it extends the graph to Kripke Structure by assigning a subset of propositional
    variables to each world.
    """

    def __init__(self, name, assignment):
        self.name = name
        self.assignment = assignment

    def __eq__(self, other):
        return self.name == other.name and self.assignment == other.assignment
