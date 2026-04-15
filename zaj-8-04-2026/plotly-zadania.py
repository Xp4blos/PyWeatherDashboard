# Zadanie 4 Plotly
#
# godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
# wyniki = [40, 50, 55, 60, 70, 75, 85]
#
# Stwórz wykres punktowy, który pokaże zależność między:
#
# - liczbą godzin nauki
# - wynikiem egzaminu
#
#
# --------------------------------------------------------------
# Zadanie 5 Plotly
#
# jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
# udzial = [35, 30, 15, 10, 10]
#
# Stwórz wykres kołowy, który pokaże udział języków programowania używanych przez programistów w projekcie.
#
# ------------------------------------------------------------------------------
# Zadanie 6 Plotly
#
# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# temperatura = [18, 20, 19, 23, 25, 22, 21]
#
# Stwórz interaktywny wykres liniowy, który pokaże temperaturę w kolejnych dniach tygodnia.

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

#zad1

godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
wyniki = [40, 50, 55, 60, 70, 75, 85]

fig1 = px.scatter(x=godziny_nauki, y=wyniki, title="Godziny nauki do wyników", labels={"x":"Godziny nauki","y":"Wyniki"})
fig1.show()

#2
jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
udzial = [35, 30, 15, 10, 10]

fig2 = px.pie(jezyki,udzial,title="Języki Programowania")

fig2.show()

#3

dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
temperatura = [18, 20, 19, 23, 25, 22, 21]

fig3 = px.line(x=dni,y=temperatura,title="Wykres temperatury", labels={
    "x":"Dzień",
    "y":"Stopnie"
})
fig3.show()