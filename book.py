class Book:
    
    licznik= 0;
    
    
    def __init__(self,t,a,p,i):
        self.__title=t
        self.__autor=a
        self.__pubhlished=p
        self.__isbn=i
        
        Book.licznik+=1
        
    
    def __del__(self):
        Book.licznik-=1
        
    
    def __str__(self):
        
        n=self.GetAutor()
        s=""
        for i in range(len(n)):
            s+=n[i][0]+" "+n[i][1]+', '
        
        return "Tytuł: "+ self.GetTitle()+'\nAutorzy: '+s+"\nPublikacja: "+str(self.GetPublished())+"\nNumer ISBN: "+self.GetIsbn()
    
    def SetTitle(self,x):
        self.__title=x
        
    def SetAutor(self,x):
        self.__autor=x
        
    def SetPublished(self,x):
        self.__pubhlished=x
    
    def SetIsbn(self,x):
        self.__isbn=x
            
    
    
    def GetTitle(self):
        return self.__title
    
    def GetAutor(self):
        return self.__autor
        
    def GetPublished(self):
        return self.__pubhlished
    
    def GetIsbn(self):
        return self.__isbn
        
        


        
        