from book import Book
class Books:
    
    
    
    def __init__(self, ksiazki):
        self.__tablica=ksiazki  
        
    def __del__(self):
        pass
    
    
            
    def SetKsiazki(self,x):
        self.__tablica=x
    
    
    def GetKsiazki(self):
        return self.__tablica
    
    def sprawdz(self,k):
        n=self.GetKsiazki()
        a=k.GetAutor()
        
        for i in n:
            au=i.GetAutor()
            if (au==a):
                print("Książka jest w bazie!")
                return
        
        print("Nie ma książki w bazie!")
            