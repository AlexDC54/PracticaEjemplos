import requests

def solicitar():
    #realizamos la peticion http
    response=requests.get('https://reqres.in/api/users')
    #si se recuperan los datos
    if response.status_code==200:
        #extraemos los datos de la respuesta y almacenamos
        respuesta=response.json()
        return respuesta.get('data')
    return ''


def obtenersms():
    response=requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        mensajes = response.json()
        return mensajes[:5]  
    return ''
