dist = int( input("Informe uma distancia em metros: ") )
dist_km = dist / 1000
dist_hm = dist / 100
dist_dam = dist / 10
dist_dm = dist * 10
dist_cm = dist * 100
dist_mm = dist * 1000

print(f"""
{dist_km} km
{dist_hm} hm
{dist_dam} dam
{dist_dm} dm
{dist_cm} cm
{dist_mm} mm
""")

