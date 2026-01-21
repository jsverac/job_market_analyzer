import json
import urllib.request

def fetch_jobs(search_term):
    pagina_inicio = 1
    lista_vacantes = []
    while True:
        endpoint = f"https://www.buscadordeempleo.gov.co/backbue/v1//vacantes/resultados?page={pagina_inicio}&BUSQUEDA={search_term}"
        respuesta=urllib.request.urlopen(endpoint)
        datos_respuesta = respuesta.read()
        json_respuesta = json.loads(datos_respuesta.decode('utf-8'))
        total_page = json_respuesta["totalPages"]
        print(f"el numero de paginas totales es de {total_page}")
        for vacante in json_respuesta["resultados"]:
            lista_vacantes.append(vacante)
        print(f"la pagina actual es {json_respuesta["currentPage"]}")
        pagina_inicio += 1
        if pagina_inicio > total_page:
            break
    print(f"el total de vacantes para la oferta {search_term} es de {len(lista_vacantes)}")
    return lista_vacantes

if __name__ == "__main__":
    fetch_jobs("analista+de+datos")
    print("termino la ejecucion")


