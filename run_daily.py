from scrapers.gov_api import fetch_jobs
import json
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_json = os.path.join(directorio_actual,'config','profile.json')

with open(ruta_json,'r',encoding='utf-8') as perfiles:
    datos = json.load(perfiles)

for perfil in datos["perfiles"]:
    print(f"Buscando empleos para: {perfil}")
    fetch_jobs(perfil)

# jobs = fetch_jobs("analista+de+datos")
# print(jobs)