


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def Iniciar_sesion():

    # Configura el driver (asegúrate de que el chromedriver esté en el PATH o indica la ruta)
    service = Service('./chromedriver.exe')  # Ej: 'chromedriver.exe' si está en la misma carpeta
    options = webdriver.ChromeOptions()


    # Agregar configuración de impresión
    options.add_argument('--kiosk-printing')



    prefs = {
        'printing.print_preview_sticky_settings.appState': """
            {
                "recentDestinations": [{
                    "id": "Save as PDF",
                    "origin": "local",
                    "account": "",
                    "name": "Save as PDF"
                }],
                "selectedDestinationId": "Save as PDF",
                "version": 2,
                "isHeaderFooterEnabled": false,
                "mediaSize": {
                    "height_microns": 297000,
                    "width_microns": 210000,
                    "name": "ISO_A4"
                },
                "marginsType": 1,
                "scalingType": 3
            }
        """,
        'savefile.default_directory': os.path.abspath("boletas_pdf"),
        'download.prompt_for_download': False,
        'download.directory_upgrade': True
    }

    options.add_experimental_option('prefs', prefs)



    driver = webdriver.Chrome(service=service, options=options)

    # URL objetivo
    url = 'https://v2.be-flow.com/login'
    driver.get(url)


    # Buscar campos de login y completar e iniciar sesión
    driver.find_element(By.NAME, "email").send_keys(os.getenv("BEFLOW_EMAIL"))
    driver.find_element(By.NAME, "password").send_keys(os.getenv("BEFLOW_PASSWORD"))
    botonIniciarSesion = driver.find_element(By.CSS_SELECTOR, ".sc-dwalKd.ewKcxc.amplify-button.secondary")
    botonIniciarSesion.click()

    # Esperar a que cargue el contenido dinámico
    time.sleep(10)


    #retornar el driver
    return driver


