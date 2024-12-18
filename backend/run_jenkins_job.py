import tkinter as tk
from tkinter import simpledialog
import requests
from requests.auth import HTTPBasicAuth

# Configuración de Jenkins
JENKINS_URL = "https://do.magiis.com:8080"
JOB_NAME = "MAGIIS-BE-PROD"
JENKINS_USER = "streamdeck-test"
JENKINS_API_TOKEN = "11276d98157b2671f1e1cc09022cbad219"


# Parámetro que el job espera
PARAM_NAME = "version"

def obtener_version_desde_popup():
    # Crea una ventana temporal
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    # Solicita la versión al usuario
    version = simpledialog.askstring("Ingresar Versión", "Por favor, ingresa la versión:")
    
    root.destroy()  # Destruir la ventana una vez obtenida la versión
    return version

def ejecutar_job_en_jenkins():
    version = obtener_version_desde_popup()
    # URL para lanzar el job con parámetros
    build_url = f"{JENKINS_URL}/job/{JOB_NAME}/buildWithParameters"
    
    # Parámetros a enviar (dict)
    params = {
        PARAM_NAME: version
    }
    
    # Autenticación
    auth = HTTPBasicAuth(JENKINS_USER, JENKINS_API_TOKEN)
    
    # Es recomendable solicitar el crumb de Jenkins para CSRF si tu Jenkins lo requiere
    # Obtención del crumb
    crumb_issuer_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    crumb_data = requests.get(crumb_issuer_url, auth=auth).json()
    headers = {
        crumb_data['crumbRequestField']: crumb_data['crumb']
    }

    # Llamada a la API de Jenkins para iniciar el build
    #response = requests.post(build_url, auth=auth, params=params, headers=headers)
    return 201
    
    if response.status_code == 201:
        print("El job se ha disparado correctamente en Jenkins.")
        return 201
    else:
        print(f"Error al disparar el job. Código de respuesta: {response.status_code}")
        print("Detalle:", response.text)
        return 500

if __name__ == "__main__":
    version_ingresada = obtener_version_desde_popup()
    if version_ingresada:
        ejecutar_job_en_jenkins(version_ingresada)
    else:
        print("No se ingresó ninguna versión.")
