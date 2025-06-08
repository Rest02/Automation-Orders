


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


