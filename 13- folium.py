import folium

# 1 - Criando um mapa centrato em uma localização
mapa = folium.Map(location=[-23.533773, -46.625290], zoom_start=12)

# 2 - Adicionando um marcador
cafeteiras = [
    {"localizacao": [-23.533773, -46.625290], "nome": "Cafeteria"},
    {"localizacao": [-23.534773, -46.625290], "nome": "Cafeteria 2"},
    {"localizacao": [-23.535773, -46.625290], "nome": "Cafeteria 3"},
    {"localizacao": [-23.536773, -46.625290], "nome": "Cafeteria 4"},
]

for cafe in cafeteiras:
    folium.Marker(
        location=cafe["localizacao"],
        popup=cafe["nome"],
        icon=folium.Icon(color="red",icon='coffee'),
    ).add_to(mapa)

mapa.save("mapa.html")