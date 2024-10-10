from person_class import Person

class Population:

    def __init__(self,size):
        self.size = size
        self.population = self.build_population()

    def build_population(self):
        population = [Person(i) for i in range(self.size)]
        return population


