import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from matplotlib.pyplot import xlabel

pio.renderers.default='browser'

x = [1,2,3,4,5]
y = [10,15,13,17,20]

fig1 = px.line(x=x, y=y, title="Wykres liniowy", markers=True)

# fig1.show()

produkty = ["A","B","C","D"]
wyniki = [12,19,7,15]

fig2 = px.bar(
    x=produkty,
    y=wyniki,
    title="Wykres slupkowy",
    orientation="h",
)
# fig2.show()

a = [1,2,3,4,5]
b = [3,7,4,9,6]

fig3= px.scatter(x=a, y=b)
# fig3.show()


oceny = [2,2,5,5,4,3,2,5,4,3]
fig4 = px.histogram(x=oceny, title="Oceny", nbins=4)
fig4.show()

etykiety = ["Python","Java","C++","JS"]
wartosci = [40,25,15,20]

fig5 = px.pie(names=etykiety, values=wartosci, title="Udział języków")
# fig5.show()


dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
sprzedaz = [120, 150, 180, 160, 170, 210, 190]

fig6 = px.area(x=dni, y=sprzedaz, title="Wykres obszarowy")
fig6.show()

dni = [1,2,3,4,5]
sprzedaz = [10,12,35,14,78]
koszty = [6,7,8,7,9]

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=dni, y=sprzedaz, mode="lines+markers", name="Sprzedaż")
)
fig.add_trace(
    go.Scatter(x=dni, y=koszty, mode="lines+markers", name="Koszty")
)

fig.update_layout(
    title="Wykresy liniowe",
    xaxis_title="Dzień",
    yaxis_title="Kwota",
)

fig.show()