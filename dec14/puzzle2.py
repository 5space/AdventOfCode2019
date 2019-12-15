import sys, os, math
sys.path.append(os.getcwd())
from util.intcode import IntCode

with open("dec14/input.txt", "r") as file:
    lines = file.readlines()
reactions = []
nodes = []
for line in lines:
    line = line.strip()
    r, p = line.split(" => ")
    reactants = [r.split(" ") for r in r.split(", ")]
    products = [p.split(" ") for r in p.split(", ")]
    reactions.append(({k: int(v) for [v, k] in reactants}, {k: int(v) for [v, k] in products}))
    nodes.append(products[0][1])

def get_reaction(product):
    for r in reactions:
        if product in r[1]:
            return r

def get_reactions_from_reactant(reactant):
    for r in reactions:
        if reactant in r[0]:
            yield r

def ore_amt(fuel_amt):
    supplies = {"FUEL": fuel_amt}
    ore_consumed = 0
    reactions_consumed = list()
    frontier_nodes = {"FUEL"}

    while True:
        to_add = set()
        to_remove = set()
        if frontier_nodes == {"ORE"} or frontier_nodes == set():
            break
        for node in frontier_nodes:
            if all(r in reactions_consumed for r in get_reactions_from_reactant(node)):
                new_reaction = get_reaction(node)
                new_reactants, new_product = new_reaction
                items = list(new_product.items())
                prodtype, prodamt = items[0][0], items[0][1]
                multiplier = math.ceil(supplies[node]/prodamt)
                for reactant in new_reactants:
                    if reactant not in supplies:
                        supplies[reactant] = 0
                    supplies[reactant] += new_reactants[reactant] * multiplier
                    to_add.add(reactant)
                to_remove.add(node)
                if get_reaction(node) not in reactions_consumed:
                    reactions_consumed.append(get_reaction(node))
        frontier_nodes = frontier_nodes.union(to_add)
        frontier_nodes -= to_remove

    return(supplies["ORE"])

n = 998000
while True:
    if ore_amt(n) >= 1000000000000:
        break
    n += 1
print(n)