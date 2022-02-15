import requests

self.swally_score = 0 #initializing swally points variable

#if statments to keep count of a user's swally points
def swally_score_calculate(self, flag):
    if flag == 0:
        self.swally_score +=100
        self.save()
    else:
        self.swally_score -=100
        self.save()

#if statments and api for the housing progression
housing = {'first': '1', 'second': 2, 'third': 3,'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7,'eighth': 8, 'ninth': 9, 'tenth': 10,'eleventh': 11, 'twelth': 12, 'thirteenth': 13, 'fourteenth': 14,'fifthteenth': 15}
api_url = "https://jsonplaceholder.typicode.com/todos/10"

if (self.swally_score < 200):
    response = requests.post(api_url, housing = {'first': 1})
    response = requests.get(api_url)
    response.housing()
 
if (self.swally_score >= 200) & (self.swally_score < 600):
    response = requests.put(api_url, housing = {'second': 2})
    response.housing()
    
if (self.swally_score >= 600) & (self.swally_score < 1400):
    response = requests.put(api_url, housing = {'third': 3})
    response.housing()
    
if (self.swally_score  >= 1400) & (self.swally_score < 2600):
    response = requests.put(api_url, housing = {'fourth': 4})
    response.housing()
    
if (self.swally_score >= 2600) & (self.swally_score < 4300):
    response = requests.put(api_url, housing = {'fifth': 5})
    response.housing()
    
if (self.swally_score  >= 4300) & (self.swally_score < 6500):
    response = requests.put(api_url, data = {'sixth': 6})
    response.housing()
    
if (self.swally_score >= 6500) & (self.swally_score < 9300):
    response = requests.put(api_url, data = {'seventh': 7})
    response.housing()
    
if (self.swally_score >= 9300) & (self.swally_score < 12700):
    response = requests.put(api_url, data = {'eighth': 8})
    response.housing()
    
if (self.swally_score >= 12700) & (self.swally_score < 16700)
    response = requests.put(api_url, data = {'ninth': 9})
    response.housing()
    
if (self.swally_score >= 16700) & (self.swally_score < 21400)
    response = requests.put(api_url, data = {'tenth': 10})
    response.housing()
                            
if (self.swally_score >= 21400) & (self.swally_score < 26800):
    response = requests.put(api_url, data = {'eleventh': 11}
    response.housing()
                            
if (self.swally_score >= 26800) & (self.swally_score < 32900)
    response = requests.put(api_url, data = {'twelth': 12})
    response.housing()
                            
if (self.swally_score >= 32900) & (self.swally_score < 3800):
    response = requests.put(api_url, data = {'thirteenth': 13})
    response.housing()
                            
if (SP >= 39800) & (SP < 47500):
    response = requests.put(api_url, data = {'fourteenth': 14})
    response.housing()
                            
if (SP >= 47500):  
    response = requests.put(api_url, data = {'fifthteenth': 15'})
    response.housing()
                            
