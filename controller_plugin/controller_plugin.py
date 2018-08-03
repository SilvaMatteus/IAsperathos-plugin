import requests
from math import log10
import json

class IAsperathosController(object):
    
    def __init__(self, time_limit):
        self.__time_limit = time_limit
    
    def __get_fitness_percentage(self,real_fitness, fitness_limit):
        return log10(real_fitness) / log10(fitness_limit)
    
    def __get_time_spent_percentage(self, real_time, time_limit):
        return float(real_time) / time_limit

    def __get_fitness(self,url):
        try:
            r = requests.get(url)
            progress = json.loads(r.json)
            return float(progress["real_progress"])
        except:
            return None

    def evaluate_efficiency(self, url, fitness_limit,time_spent): 
        real_fitness = self.__get_fitness(url)
        if not real_fitness:
            return None
        fitness_percentage = self.__get_fitness_percentage(real_fitness, fitness_limit)
        time_percentage = self.__get_time_spent_percentage(time_spent, self.__time_limit)
        return fitness_percentage - time_percentage
