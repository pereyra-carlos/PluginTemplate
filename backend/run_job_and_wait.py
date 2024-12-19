import time
import tkinter as tk
from tkinter import simpledialog
import requests
from requests.auth import HTTPBasicAuth


JENKINS_URL = "https://do.magiis.com"
JOB_NAME = "autom-test"
JENKINS_USER = "magiis_cicd_manager"
JENKINS_API_TOKEN = "11276d98157b2671f1e1cc09022cbad219"
PARAM_NAME = "version"

def obtener_version_desde_popup():
    # Crea una ventana temporal
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    # Solicita la versión al usuario
    version = simpledialog.askstring("Ingresar Versión", "Por favor, ingresa la versión:")
    
    #root.destroy()  # Destruir la ventana una vez obtenida la versión
    return version

def obtener_crumb(auth):
    crumb_issuer_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    crumb_data = requests.get(crumb_issuer_url, auth=auth).json()
    headers = {
        crumb_data['crumbRequestField']: crumb_data['crumb']
    }
    return headers

def disparar_job(version):
    auth = HTTPBasicAuth(JENKINS_USER, JENKINS_API_TOKEN)
    headers = obtener_crumb(auth)
    build_url = f"{JENKINS_URL}/job/{JOB_NAME}/buildWithParameters"
    params = { PARAM_NAME: "v" + version }

    response = requests.post(build_url, auth=auth, params=params, headers=headers)
    if response.status_code == 201:
        # Jenkins devuelve en la cabecera Location la URL del ítem en la cola
        queue_url = response.headers.get('Location')
        #print("Job disparado correctamente. Monitoreando la cola...")
        return queue_url
    else:
        print(f"Error al disparar el job: {response.status_code}")
        return None

def obtener_build_number(queue_url, auth):
    # Ej: queue_url suele ser algo como: https://jenkins_url/queue/item/123/
    # Necesitamos hacer /api/json a ese endpoint
    while True:
        time.sleep(5)
        r = requests.get(queue_url + "api/json", auth=auth)
        if r.status_code == 200:
            data = r.json()
            if 'executable' in data and data['executable'] is not None:
                build_number = data['executable']['number']
                #print(f"Job asignado a build #{build_number}")
                return build_number
            else:
                print("Esperando a que el ítem salga de la cola...")
        else:
            print(f"Error obteniendo el número de build: {r.status_code}")
            return None

def monitorear_build(build_number, auth):
    build_api_url = f"{JENKINS_URL}/job/{JOB_NAME}/{build_number}/api/json"
    while True:
        time.sleep(10)
        r = requests.get(build_api_url, auth=auth)
        if r.status_code == 200:
            data = r.json()
            # result será None mientras el job esté corriendo
            if data['result'] is not None:
                #print(f"Build finalizado con estado: {data['result']}")
                return data['result']
            else:
                print("Build en progreso...")
        else:
            print(f"Error consultando el estado del build: {r.status_code}")
            return None

def ejecutar_job_completo():
    version = obtener_version_desde_popup()
    auth = HTTPBasicAuth(JENKINS_USER, JENKINS_API_TOKEN)
    queue_url = disparar_job(version)
    if queue_url:
        yield "Encolado"
        build_number = obtener_build_number(queue_url, auth)
        if build_number:
            yield str("#" + build_number)
            result = monitorear_build(build_number, auth)
            yield str(result)
            #print("Resultado final del build:", result)

# Ejemplo de uso
if __name__ == "__main__":
    # Aquí podrías obtener la versión desde el popup
    # version = obtener_version_desde_popup()
    #version = "1.2.3"
    
    #ejecutar_job_completo()
    for estado in ejecutar_job_completo():
        print(estado)
        
