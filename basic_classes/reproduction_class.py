from population_class import Population
from genome_class import Genome
import math
import random
from random import sample
import numpy as np

class Reproduction:
    def __init__(self,recomb_rate=None,growth_rate=None):
        if not growth_rate: self.growth_rate = 0
        else: self.growth_rate = growth_rate
        if not recomb_rate: self.recomb_rate = 0
        else: self.recomb_rate = recomb_rate

    def make_descendant_population(self,ancestors):
        pop_size = math.ceil((1+self.growth_rate)*ancestors.size)
        descendants = Population(pop_size)
        for offspring in descendants.population:
            self.create_offspring(offspring,ancestors)
        return descendants

    def create_offspring(self,offspring,ancestors):
        parent1,parent2 = self.choose_parents(ancestors)
        offspring.genome = self.make_offspring_genome(parent1,parent2)
        offspring.label = min(parent1.label,parent2.label)
        offspring.parents = (parent1,parent2)

    def choose_parents(self,ancestors):
        parent_index = random.randint(0,ancestors.size-1)
        parent1= ancestors.population[parent_index]
        if parent1.label == 1:
            ancestor_indices = [index for index in range(ancestors.size) if ancestors.population[index].label != 1]
            parent_index_list = sample(ancestor_indices, 1)
            parent2 = ancestors.population[parent_index_list[0]]
        else:
            parent_index = random.randint(0, ancestors.size - 1)
            parent2 = ancestors.population[parent_index]
        return parent1,parent2

    def make_offspring_genome(self,parent1,parent2):
        '''
        naive random sampling of parent genomes
        '''
        chromosome1 = self.make_chromosome(parent1)
        chromosome2 = self.make_chromosome(parent2)
        genome = Genome(chromosome1,chromosome2)
        return genome

    def make_chromosome(self,parent):
        '''
        generate parental conttribution to genome
        allowing for recombination.  Assumption is 
        of a single chromosome.
        '''
        if np.random.binomial(1,.5) > 0:
            chromosome = parent.genome.copy1
            for site in range(len(chromosome)):
                if self.recomb_rate > 0:
                    if np.random.uniform(0,1) < self.recomb_rate:
                        chromosome[site] = parent.genome.copy2[site]
        else:
            chromosome = parent.genome.copy2
            for site in range(len(chromosome)):
                if self.recomb_rate > 0:
                    if np.random.uniform(0,1) < self.recomb_rate:
                        chromosome[site] = parent.genome.copy1[site]
        return chromosome




