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
    service = Service('./chromedriver.exe')
    options = webdriver.ChromeOptions()

    # ✅ Activar impresión sin diálogo
    options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://v2.be-flow.com/login')

    driver.find_element(By.NAME, "email").send_keys(os.getenv("BEFLOW_EMAIL"))
    driver.find_element(By.NAME, "password").send_keys(os.getenv("BEFLOW_PASSWORD"))
    botonIniciarSesion = driver.find_element(By.CSS_SELECTOR, ".sc-dwalKd.ewKcxc.amplify-button.secondary")
    botonIniciarSesion.click()

    time.sleep(10)

    preparacion_link = driver.find_element(By.XPATH, "//a[span[text()='Preparación']]")
    preparacion_link.click()
    time.sleep(3)

    campo_busqueda = driver.find_element(By.CSS_SELECTOR, "input.ant-input[placeholder='Búsqueda']")
    time.sleep(3)
    campo_busqueda.send_keys(numero_pedido)
    time.sleep(3)

    # 🔽 Aquí haces clic en la boleta
    element = driver.find_element(By.CSS_SELECTOR, 'b[role="button"]')
    element.click()
    time.sleep(3)

    # ⛔️ Este selector parece incorrecto: "cr-button.action-button[size='small']"
    # Solo ejecuta click si esto realmente corresponde al botón que dispara la impresión
    element_imprimir = driver.find_element(By.CSS_SELECTOR, 'cr-button.action-button[size="small"]')
    element_imprimir.click()

    # Espera unos segundos para que la impresión se procese
    time.sleep(10)

    driver.quit()


