#!/usr/bin/python3

import random

#Instructions :
#
#This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.#
#
#    Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
#        A Gene is a single value 0 or 1, it can mutate (flip).
#        A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
#        A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.
#
#    Implement these classes as you see fit.
#
#    Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.#
#
#    Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of 
# generations (iterations) it took.
#
#Write your results in you personal biology research notebook and tell us your conclusion :).


class Gene:
    ''' a single value 0 or 1'''
    def __init__(self):
        self.value = random.randint(0, 1) 
    def mutate(self):
        if self.value == 0: #mutate only if the gene is 0
            self.value = 1
    
        #self.value = 1 - self.value

class Chromosome():
    '''composed of 10 Gens'''
    def __init__(self):
        self.genes = []
        for _ in range(10):
            self.genes.append(Gene())
    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

class DNA:
    '''composed of 10 chromosomes'''
    def __init__(self):
        self.chromosomes = []
        for _ in range(10):
            self.chromosomes.append(Chromosome())


    def mutate(self):
        for chrom in self.chromosomes:
            chrom.mutate()

class Organism:
    '''accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate'''
    def __init__(self,  dna, environment_prob):
        self.dna = dna
        self.environment_prob = environment_prob

    def mutate(self):
        if random.random() < self.environment_prob:
            self.dna.mutate()

    def all_one(self):
        for chrom in self.dna.chromosomes:
            for gene in chrom.genes:
                if gene.value == 0:
                    return False
        return True

    def show_dna(self):
        if self.all_one():
            return 

        for chrom in self.dna.chromosomes:
            print([gene.value for gene in chrom.genes])
            print("")

generations = 0
organism = Organism(DNA(), 1)  # 100% mutation chance

while not organism.all_one():
    print(f"Generation: {generations}")
    organism.mutate()
    organism.show_dna()
    generations += 1
    if generations > 10000:
        print("Too many generations! Something is wrong.")
        break


print(f"Perfect DNA achieved in {generations} generations.")

