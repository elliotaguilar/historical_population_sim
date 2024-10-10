from population_class import Population
from reproduction_class import Reproduction
from genome_class import Genome
import math

def initialize_gen_zero(ancestors,perc_european,num_segments):
    num_euro = math.ceil(perc_european*ancestors.size)
    print(f'num_euro = {num_euro}')
    count = 0
    for ancestor in ancestors.population:
        count+=1
        if count <= num_euro:
            ancestor.label = 1
            copy1,copy2 = [1 for i in range(num_segments)],[1 for i in range(num_segments)]
            ancestor.genome = Genome(copy1,copy2)
        else:
            ancestor.label = 0
            copy1,copy2 = [0 for i in range(num_segments)],[0 for i in range(num_segments)]
            ancestor.genome = Genome(copy1,copy2)
    return ancestors

if __name__=="__main__":
    '''
    params
    '''
    size = 100
    perc_european = .05
    recomb_rate = 0.01
    num_segments = 1000
    '''
    Run simulation
    '''
    ancestors = Population(size)
    ancestors = initialize_gen_zero(ancestors,perc_european,num_segments)
    for ancestor in ancestors.population:
        print(f"ancestor {ancestor.name} = \
                \n{ancestor.label}\
                \n{ancestor.genome.copy1}\
                \n{ancestor.genome.copy2}\
                \n{ancestor.sex}")
    rp = Reproduction(recomb_rate)
    descendants = rp.make_descendant_population(ancestors)
    for descendant in descendants.population:
        print(f"descendant {descendant.name} = \
                \n{descendant.label}\
                \n{descendant.genome.copy1}\
                \n{descendant.genome.copy2}\
                \n{descendant.sex}")


