from book import Book
from books import Books

k1=Book("opowieci Zbysia",[["Kuba","nowak"],["Agata","Nowak"]],1912,"qwertyuiopasdf")
k2=Book("opowieci Staszka",[["Bartek","nowak"],["Staszek","Nowak"]],1954,"qwertyufghasdf")
k3=Book("opowieci Gienka",[["Stefan","nowak"],["Pawełk","Nowak"]],2000,"qvbfhrjfghasdf")
k4=Book("Nigdy nie mów nigdy",[["Stefan","Krzyszczak"],["Pawełk","Nowak"]],2000,"qvbfhrjfghasdf")
print(k1)
print('\n')
print(k2)
print('\n')
print(k3)
print('\n')
print(Book.licznik)

tab=[]
tab.append(k1)
tab.append(k2)
tab.append(k3)

baza=Books(tab)

baza.sprawdz(k1)
baza.sprawdz(k4)

