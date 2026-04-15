import matplotlib.pyplot as plt


# Zadanie 1 Matplotlib

dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
sprzedaz = [120, 150, 180, 160, 170, 210, 190]

plt.title("Sprzedaż w tygodniu")
plt.xlabel("Dni tygodnia")
plt.ylabel("Sprzedaż")
plt.plot(dni,sprzedaz)
plt.show()

#Zadanie 2 Matplotlib

produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
sprzedaz = [25, 18, 40, 12]

plt.bar(produkty,sprzedaz)
plt.title("Sprzedaż")
plt.xlabel("Produkty")
plt.ylabel("Ilość")
plt.show()

#Zadanie 3 Matplotlib

wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]

plt.hist(wyniki)
plt.title("wyniki testu")
plt.xlabel("Oceny")
plt.show()