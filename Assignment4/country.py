# Written by Syed Ahmed (sahme339)
# 11 April 2018
# CS1026B Assignment 4 - Country file
# Purpose: Task 1  - implement the the class called Country that holds the information about a single country

# Task 1
class Country :

    # set up the __init__ with information
    def __init__(self, name, pop, area, continent = "") :
        self._name = name
        self._population = pop
        self._area = area
        self._continent = continent

    # set the population
    def setPopulation(self, pop) :
        self._population = pop

    # get the name
    def getName(self) :
        return self._name

    # get the area
    def getArea(self) :
        return self._area

    # set the area
    def setArea(self, newArea) :
        self._area = newArea

    # get the population
    def getPopulation(self) :
        return self._population

    # set the population
    def setPopulation(self, newPop) :
        self._population = newPop

    # get the continent
    def getContinent(self) :
        return self._continent

    # set the continent
    def setContinent(self, newCont) :
        self._continent = newCont

    # determine population density
    def getPopDensity(self) :
        popDensity = self._population / self._area

        popDensity = round(popDensity, 2)

        return popDensity

    # store all the key raw information in one statement
    def __repr__(self) :
        return (("{} (pop: {}, size: {}) in {}").format(self._name, str(self._population), str(self._area), self._continent))
