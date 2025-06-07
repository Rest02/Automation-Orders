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

def pruebas_imprimir_boleta(numero_pedido):
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

    time.sleep(10)

    preparacion_link = driver.find_element(By.XPATH, "//a[span[text()='Preparación']]")
    preparacion_link.click()

    time.sleep(3)

    # Encuentra el campo de búsqueda
    campo_busqueda = driver.find_element(By.CSS_SELECTOR, "input.ant-input[placeholder='Búsqueda']")

    time.sleep(3)

    # Introduce el número de pedido en el campo de búsqueda
    campo_busqueda.send_keys(numero_pedido)

    time.sleep(3)


    # Hacer click en el botón de imprimir boleta

    element = driver.find_element(By.CSS_SELECTOR, 'b[role="button"]')
    element.click()

    time.sleep(3)

    # Hacer click en el botón de imprimir
    elemento_imprimir = driver.find_element(By.CSS_SELECTOR, "div.svelte-1w9r7lo.content")
    elemento_imprimir.click()

    # time.sleep(3)

    # # Hacer click en el checkbox de pedido
    # checkbox = driver.find_element(By.CLASS_NAME, "ant-checkbox-input")
    # checkbox.click()



    # # Hacer click en el menu desplegable de acciones
    # boton = driver.find_element(By.CSS_SELECTOR, "button.ant-dropdown-trigger")
    # boton.click()


    # time.sleep(3)


    # # Esperar a que aparezca el elemento y luego hacer clic para enviar a entregas
    # enviar_btn = WebDriverWait(driver, 3).until(
    # EC.element_to_be_clickable((By.XPATH, "//span[text()='Enviar a entregas (1)']"))
    # )
    # enviar_btn.click()


    time.sleep(10)

