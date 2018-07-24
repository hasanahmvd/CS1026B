# Written by Syed Ahmed (sahme339)
# 11 April 2018
# CS1026B Assignment 4 - Country file
# Purpose: Task 2  - implement the the class called CountryCatalogue that will use two files to build the data stractures

# Task 2
# import everything from country
from country import *
# implement a class that utilized both files given and stores information about the countries
class CountryCatalogue :
    # initialize two instance variables with constructor method
    def __init__(self, continentStr, dataStr):
        self._countryCat = {}
        self._cDictionary = {}

        # open, read, and modify the continent files and create dictionary for continents
        continentFile = open(continentStr, "r")
        continentFile.readline()
        for line in continentFile :
            stripLine = line.rstrip('/n')
            splitLine = stripLine.split(',')
            self._cDictionary[splitLine[0]] = splitLine[1]

        # open, read, and modify the data files and create dictionary for information
        dataFile = open(dataStr, 'r')
        dataFile.readline()
        for line2 in dataFile :
            stripLine2 = line2.rstrip('/n')
            splitLine2 = stripLine2.split('|')
            commaStrip1 = splitLine2[1].replace(",", "")
            commaStrip2 = splitLine2[2].replace(",", "")
            num1 = int(commaStrip1)
            num2 = float(commaStrip2)
            self._countryCat[splitLine2[0]] = Country(splitLine2[0], num1, num2, self._cDictionary[splitLine2[0]])

        # close the files
        continentFile.close()
        dataFile.close()

    # print all of the information currently stored
    def printCountryCatalogue(self) :
        for key in self._countryCat :
            print(key.__repr__())

    # check if country is currently stored
    def findCountry(self, name) :
        if name not in self._countryCat :
            return None
        else :
            return name

    # add a country to the dictionary if not already present
    def addCountry(self, name, pop, area, continent) :
        if name not in self._countryCat:
            self._countryCat[name] = Country(name, pop, area, continent)
            self._cDictionary[name] = continent
            print("Country was successfully added!")
            return True
        else :
            return False

    # delete a country from the dictionary if it is currently present
    def deleteCountry(self, name) :
        if name in self._countryCat :
            self._cDictionary.pop(name)
            self._countryCat.pop(name)
            print("Country was deleted")
        else :
            print("The entered country does not exist in this catalogue")

    # update the area of a country currently in the dictionary
    def setAreaOfCountry(self, name, area) :
        if name in self._countryCat :
            self._countryCat[name].setArea(area)
            print("The area has been updated!")
            return True
        else :
            return False

    # update the population of a country currently in the dictionary
    def setPopulationOfCountry(self, name, pop) :
        if name in self._countryCat :
            self._countryCat[name].setPopulation(pop)
            print("Population updated!")
            return True
        else :
            return False

    # save the current information in the dictionary
    def saveCountryCatalogue(self, filename) :
        catalogueFile = open(filename, "w")
        for key in self._countryCat :
            name = key
            continent = self._cDictionary[key]
            population = self._countryCat[key].getPopulation()
            populationDens = self._countryCat[key].getPopDensity()
            catalogueFile.write("{}|{}|{}|{}".format(name, continent, population, populationDens))
        #close the file
        catalogueFile.close()

        # return length of dictionary
        if len(self._countryCat) != 0 :
            return len(self._countryCat)
        else :
            return -1
        
    # determine all the countries stored that are within the entered continent
    def getCountriesByContinent(self, continent):
        listOfCountries = []
        for key in self._cDictionary :
            if continent in self._cDictionary.get(key) :
                listOfCountries.append(key)

        return listOfCountries

    # find the countries that have the population density in the bounds set and print in descending order
    def filterCountriesByPopDensity(self, lowerBound, upperBound) :
        countriesInRange = []
        for key in self._countryCat :
            name = key
            popDensity = self._countryCat[key].getPopDensity()
            if popDensity >= int(lowerBound) and popDensity <= int(upperBound) :
                countriesInRange.append((name, popDensity))
        countriesInRange.sort(key=lambda x:x[1], reverse = True)
        return countriesInRange

