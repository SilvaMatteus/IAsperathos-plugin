import requests
from math import log
import json

class IAsperathosController(object):
    
    def __init__(self, progress_limit):
        self.__progress_limit = progress_limit
    
    def expected_progress_function(self,time_spent):
        return math.log10(time_spent)

    def get_progress(self,url):
        try:
            r = requests.get(url)
            progress = json.loads(r.json)
            return float(progress["real_progress"])
        except:
            return None

    def evaluate_efficiency(self,url, time_spent): 
        real_progress = get_progress(url)
        if not real_progress:
            return None
        progress_percentage = real_progress / self.progress_limit;
        expected_progress = expected_progress_function(time_spent)
        return progress_percentage - expected_progress
