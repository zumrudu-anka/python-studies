import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import pandas as pd
import os


gdf = gpd.read_file("./data/shapefiles/turkeyborder/TUR_adm1.shp")

# print(gdf)

# print(gdf.columns)

gdf_unique_cities = gdf["NAME_1"].unique()

# gdf.plot()

# plt.show()

df = pd.read_csv("./data/shapefiles/turkeyborder/migration-city-data.csv")

# print(df)

# print(df.columns)

# df_unique_cities = df["city"].unique()

# for city in gdf_unique_cities:
#     if city not in df_unique_cities:
#         print(city)

replace_map = {
    "Çankiri" : "Çankırı",
    "Adiyaman" : "Adıyaman",
    "Afyon" : "Afyonkarahisar",
    "Agri" : "Ağrı",
    "Aydin" : "Aydın",
    "Balikesir" : "Balıkesir",
    "Diyarbakir" : "Diyarbakır",
    "Eskisehir" : "Eskişehir",
    "Gümüshane" : "Gümüşhane",
    "Istanbul" : "İstanbul",
    "Izmir" : "İzmir",
    "K. Maras" : "Kahramanmaraş",
    "Kinkkale" : "Kırıkkale",
    "Kirklareli" : "Kırklareli",
    "Kirsehir" : "Kırşehir",
    "Mugla" : "Muğla",
    "Mus" : "Muş",
    "Nevsehir" : "Nevşehir",
    "Nigde" : "Niğde",
    "Sanliurfa" : "Şanlıurfa",
    "Sirnak" : "Şırnak",
    "Tekirdag" : "Tekirdağ",
    "Usak" : "Uşak",
    "Zinguldak" : "Zonguldak"
}

gdf["NAME_1"] = gdf["NAME_1"].replace(replace_map)

# gdf["NAME_1"].replace(replace_map, inplace = True)

# turkish_chars = {
#     "İ" : "I",
#     "ı" : "i",
#     "Ş" : "S",
#     "ş" : "s",
#     "Ğ" : "G",
#     "ğ" : "g",
#     "Ü" : "U",
#     "ü" : "u",
#     "Ö" : "O",
#     "ö" : "o",
#     "Ç" : "C",
#     "ç" : "c"
# }

# translation_table = str.maketrans(turkish_chars)

# df["city"] = df["city"].str.translate(translation_table)
# gdf["NAME_1"] = gdf["NAME_1"].str.translate(translation_table)

# print(gdf["NAME_1"].unique())
# print(df["city"].unique())

gdf.merge(df, how="left", left_on="NAME_1", right_on="city")

ax = gdf.plot(
    column="NAME_1",
    cmap = "Blues",
    figsize=(20, 10),
    edgecolor="gray",
    linewidth=0.5
)

ax.set_axis_off()

for x, y, city_name in zip(gdf['geometry'].centroid.x, gdf['geometry'].centroid.y, gdf['NAME_1']):
    if city_name == "Antalya":
        ax.text(
            x - 0.3, y + 0.15, city_name, fontsize=8, path_effects=[pe.withStroke(linewidth = 2, foreground='white')]
        )
    else:
        ax.text(
            x - 0.3, y, city_name, fontsize=8, path_effects=[pe.withStroke(linewidth = 2, foreground='white')]
        )

ax.set_title(
    "Şehir Bazlı Alınan İç Göç Sayısı (2022)",
    fontsize=16,
    fontdict={"fontweight":'bold'}
)

plt.show()

os.makedirs("./outputs", exist_ok=True)

# TODO Cannot get output like this. Fix it later
plt.savefig(
    "outputs/sehir-bazli-goc-2022.png",
    dpi = 300,
    bbox_inches = "tight"
)