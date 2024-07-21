import pandas as pd
import folium

#1-Importando o Dataset
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv'
dados_terremotos = pd.read_csv(url)

#2-FIltrar os dados para obter terremotos mais significativos
terremotos_significativos = dados_terremotos[dados_terremotos['mag'] >= 6.0]

#3- Criar o mapa
mapa_terremotos = folium.Map(location=[0, 0], zoom_start=2)

# 4 - Adicionar os marcadores
for index, row in terremotos_significativos.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['place'],
        icon=folium.Icon(color='red', icon='asterisk')
    ).add_to(mapa_terremotos)

mapa_terremotos.save('mapa_terremotos.html')