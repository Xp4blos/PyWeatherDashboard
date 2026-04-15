import matplotlib.pyplot as plt

x = [1,2,3,4,9]
y = [2,3,6,8,4]

#wykres liniowy

plt.plot(x,y)
plt.title("Linear plot")
plt.xlabel("oś xów")
plt.ylabel("oś igreków")
plt.grid()
plt.show()

#wykres słupkowy
produkty = ["a","b","c","d","e"]
wyniki = [5,10,2,10,8]

plt.bar(produkty,wyniki)
plt.show()


#Histogram
oceny = [0,1,2,3,4,5,6,7,3,3,3,1,1,2]

plt.hist(oceny,bins=8)
plt.title("Histogram Ocen")
plt.xlabel("Ocena")
plt.xlabel("Liczba Wystąpień")
plt.ylim(0,5)
plt.show()

#Wykres kołowy
etykiety = ["Python","Java", "C++","JS"]
wartosci =  [40,20,25,15]
plt.pie(x=wartosci,labels=etykiety,autopct="%1.1f%%")
plt.show()

#Punktowy

a =[1,2,3,4,5]
b = [3,7,4,8,9]

plt.scatter(x=a,y=b)
plt.show()

#2 linie

c = [1,2,3,4,5,6,7,8]
d = [4,3,2,3,4,5,6,5]

