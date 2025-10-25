import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# definir bbox ou ponto + distância
lat, lon = -20.35839, -40.4097
dist = 1000  # metros, pode ajustar para cobrir o bairro inteiro

# descarrega ruas + construções na área
G = ox.graph_from_point((lat, lon), dist=dist, network_type='drive')
buildings = ox.features_from_point((lat, lon), dist=dist)

# opcional: filtrar construções maiores ou agrupar em quadras
# por simplicidade vamos apenas exportar cada construção como SVG

out_dir = "quadras_svgs"
import os
os.makedirs(out_dir, exist_ok=True)

for idx, row in buildings.iterrows():
    geom = row.geometry
    fig, ax = plt.subplots(figsize=(2,2))
    gpd.GeoSeries([geom]).plot(ax=ax, facecolor="none", edgecolor="black", linewidth=0.5)
    ax.set_axis_off()
    fig.savefig(os.path.join(out_dir, f"building_{idx}.svg"), format="svg", bbox_inches='tight', pad_inches=0)
    plt.close(fig)

print("Exportado", len(buildings), "SVGs em", out_dir)
