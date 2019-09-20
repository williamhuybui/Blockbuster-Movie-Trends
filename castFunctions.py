import sqlite3
import requests
import pandas as pd
import difflib #This is for 
from api_key import key
api_key = key

class functions():
    #Contain a local list that has 1000 top actors
    def __init__(self):
        self.conn = sqlite3.connect('Data/actorRank.db')
        self.cur=self.conn.cursor()
        self.cur.execute("""SELECT * FROM rank ;""")
        self.nameList=pd.DataFrame(self.cur.fetchall())    
        self.nameList.columns=[x[0] for x in self.cur.description]
    
    #Just a dumb function for testing
    def bark(self):
        return self.nameList
    
    #Given movie ID return cast list
    def cast(self,id):
        castList=[]
        film=requests.get("http://api.themoviedb.org/3/movie/"+str(id)+"/casts?"+'api_key='+api_key).json()
        for i in film['cast'][:10]:
            fullName=" ".join(i['name'].split()[:3])
            castList.append(fullName)
        return castList
    
    #Given name of the actor, return their rank
    #Child of cast()
    def castRank(self, castName):
        if castName in self.nameList["Name"]:
            return  (self.nameList[self.nameList["Name"]==castName])
        else :
            dfTemp=self.nameList.copy()
            ratioList=[]
            for i in self.nameList["Name"]:
                ratio=difflib.SequenceMatcher(None,castName,i).ratio() #Cool trick that return similarity ratio
                ratioList.append(ratio)

            dfTemp["Ratio"]=ratioList
            if max(ratioList) == 0:
                return (0,0)
            elif max(ratioList)>0.7: #This is the typo tolerance
                dfTemp2=dfTemp[dfTemp["Ratio"]==max(ratioList)].copy()
                return (dfTemp2.iloc[0]["Rank"],dfTemp2.iloc[0]["Name"])
            else:
                return (0,0)
            
    #Given movie id, return list of all actor with their rank    
    #Child of cast() and castRank(). The most useful function for main
    def castRankList(self,id):
        listFoo=pd.DataFrame({'Rank':[],'Name':[]})
        for name in self.cast(id):
            if self.castRank(name)[0]==0:
                pass
            else:
                listFoo.loc[len(listFoo)]=[self.castRank(name)[0],self.castRank(name)[1]] #Cool
        return listFoo.sort_values('Rank')
   