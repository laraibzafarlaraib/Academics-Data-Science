from random import randint
#life history of a batsman
class Batsman:
    def __init__(self, name, country, no_matches=None):
        self.__name = name
        self.__country = country
        self.score = []
        
        if no_matches:
           self.no_matches = no_matches
        else:
            #self.no_matches = 0
            self._randomscore()
#generating scores list by random function            
    def _randomscore(self): 
        for i in range(self.no_matches):
            r = randint(1,185)
            self.score.append(r)
        return self.score
        
#caculating total no of score of a batsman from score list
    def calTotal(self):
        self.total=0
        for i in range (len(self.score)):
            self.total += self.score[i]
        return self.total
            
#calculating... 
    
    def calAvg(self):
        avg = self.total/len(self.score)
        return avg
        
    def findMaxScore(self):
        self.maxscore=0
        self.maxscore = max(self.score)
        return self.maxscore
        
    def count50s(self):
        cfifty = 0
        for i in range(len(self.score)):
            if self.score[i] >= 50:
                cfifty +=1      
        return cfifty
        
    def count100s(self):
        c = 0
        for i in range(len(self.score)):
            if self.score[i] >= 100:
                c +=1      
        return c
        
    def show(self):
        return f"Name:{self.__name}\nCountry:{self.__country}\nNo of matches: {self.no_matches}\nScore: {self._randomscore()} \nTotal Score: {self.calTotal()}\nAverage:{self.calAvg()}\nMAx score: {self.findMaxScore()}\nCount of 50s:{self.count50s()}\nCount of 100:{self.count100s()}"
        
def main():
    a=Batsman("ALi","Pakistan", 5)
    b=Batsman("Muhammad","Pakistan", 8)
    c=Batsman('Babar Azam', 'Pakistan', 10)
    print(a.show())
    print('Player 2')
    print(b.show())
    print('Player 3')
    print(c.show())
    
if __name__ == "__main__":
    main()
