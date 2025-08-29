import pandas as pd
import panel as pn
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from dashboard_energia.transformacion.transformacion import transformar_columnas as trans_col, antiguamiento_luminarias as antig_lum    
from folium.plugins import MarkerCluster
from io import BytesIO
import geopandas as gpd
from shapely.geometry import Point
pn.extension()

# Cargar datos
df = pd.read_csv("dashboard_energia/data/EQUIPO_AP_LUMINARIA.csv", encoding="utf-8")

#tranformamos las columnas
antig_lum(trans_col(df))
# Graficamos el histograma


# Crear geometría de puntos
geometry = [Point(xy) for xy in zip(df["COORDENADA_X"], df["COORDENADA_Y"])]
gdf_luminarias = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")  # WGS84

gdf_distritos = gpd.read_file("dashboard_energia/data/DISTRITOS.shp")  # INEI o MIDIS
gdf_distritos = gdf_distritos.to_crs("EPSG:4326")  # Asegura que ambos estén en el mismo CRS

gdf_intersectado = gpd.sjoin(gdf_luminarias, gdf_distritos, how="inner", predicate="intersects")
print(gdf_intersectado.head())
print(gdf_intersectado.columns)

"""plt.figure(figsize=(10, 6))
plt.hist(df["ANTIGUEDAD"].dropna(), bins=44, color="#007acc", edgecolor="white")
plt.title("Distribución de Antigüedad de Luminarias (0–43 años)")
plt.xlabel("Antigüedad (años)")
plt.ylabel("Frecuencia")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

"""
"""# Ver valores únicos por columna
for col in df.columns:
    print(f"\nColumna: {col}")
    print(df[col].unique())
"""
"""# Centrado en Perú
m = folium.Map(location=[-9.19, -75.015], zoom_start=5, tiles='CartoDB positron')

heat_data = [[row['COORDENADA_Y'], row['COORDENADA_X']] for index, row in df.iterrows()]
HeatMap(heat_data, radius=8, blur=15, max_zoom=1).add_to(m)
m.save("mapa_calor_luminarias.html")
"""