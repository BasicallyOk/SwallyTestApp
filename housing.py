self.swally_score = 0 #initializing swally points variable

#if statments to keep count of a user's swally points
def swally_score_calculate(self, flag):
    if flag == 0:
        self.swally_score +=100
        self.save()
    else:
        self.swally_score -=100
        self.save()

#if statments for the housing progression
if (self.swally_score < 200):
    housing.post('https://httpbin.org/post', data = {'1'})
 
if (self.swally_score >= 200) & (self.swally_score < 600):
    housing.put('https://httpbin.org/put', data = {'2'})
    
if (self.swally_score >= 600) & (self.swally_score < 1400):
    housing.put('https://httpbin.org/put', data = {'3'})
    
if (self.swally_score  >= 1400) & (self.swally_score < 2600):
    housing.put('https://httpbin.org/put', data = {'4'})
    
if (self.swally_score >= 2600) & (self.swally_score < 4300):
    housing.put('https://httpbin.org/put', data = {'5'})
    
if (self.swally_score  >= 4300) & (self.swally_score < 6500):
    housing.put('https://httpbin.org/put', data = {'6'})
    
if (self.swally_score >= 6500) & (self.swally_score < 9300):
    housing.put('https://httpbin.org/put', data = {'7'})
    
if (self.swally_score >= 9300) & (self.swally_score < 12700):
    housing.put('https://httpbin.org/put', data = {'8'})
    
if (self.swally_score >= 12700) & (self.swally_score < 16700)
    housing.put('https://httpbin.org/put', data = {'9'})
    
if (self.swally_score >= 16700) & (self.swally_score < 21400)
    housing.put('https://httpbin.org/put', data = {'10'}
    
if (self.swally_score >= 21400) & (self.swally_score < 26800):
    housing.put('https://httpbin.org/put', data = {'11'})
    
if (self.swally_score >= 26800) & (self.swally_score < 32900)
    housing.put('https://httpbin.org/put', data = {'12'})
    
if (self.swally_score >= 32900) & (self.swally_score < 3800):
    housing.put('https://httpbin.org/put', data = {'13'})
 
if (SP >= 39800) & (SP < 47500):
    housing.put('https://httpbin.org/put', data = {'14'})
    
if (SP >= 47500):  
    housing.put('https://httpbin.org/put', data = {'15'}
 
