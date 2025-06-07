from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime


# Configura el driver (asegúrate de que el chromedriver esté en el PATH o indica la ruta)
service = Service('./chromedriver.exe')  # Ej: 'chromedriver.exe' si está en la misma carpeta
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# URL objetivo
url = 'https://v2.be-flow.com/login'
driver.get(url)


# Buscar campos de login y completar e iniciar sesión
driver.find_element(By.NAME, "email").send_keys("superzoo_andalue")
driver.find_element(By.NAME, "password").send_keys("Beflow123$")
botonIniciarSesion = driver.find_element(By.CSS_SELECTOR, ".sc-dwalKd.ewKcxc.amplify-button.secondary")
botonIniciarSesion.click()




# Esperar a que cargue el contenido dinámico
time.sleep(10)


# Ir a la página de pedidos en proceso
boton = driver.find_element(By.XPATH, "//button[span[text()='En proceso']]")
boton.click()
time.sleep(10)


# Recorrer toda la tabla de pedidos de la web en proceso


fecha_hoy = "02/06/2025"
contador_total = 0
contador_hoy = 0

filas = driver.find_elements(By.CSS_SELECTOR, 'tr.ant-table-row.ant-table-row-level-0')
contador = 0  # Contador de pedidos
for fila in filas:
    try:
        # Extraer ID del pedido
        enlace = fila.find_element(By.CSS_SELECTOR, "a.sc-blFMiU.cwbamp")
        id_pedido = enlace.text.strip()
        url_pedido = enlace.get_attribute("href")

        # Extraer fecha y hora
        span_fechahora = fila.find_element(By.CSS_SELECTOR, "div.sc-iGgWBj.gjgoDx")
        spans = span_fechahora.find_elements(By.TAG_NAME, "span")

        if len(spans) >= 2:
            fecha = spans[0].text.strip()
            hora = spans[1].text.strip()
        else:
            fecha = hora = "No encontrada"

        contador_total += 1

        # Validación por fecha
        if fecha == fecha_hoy:
            contador_hoy += 1
            print(f"{contador_hoy}. ID Pedido: {id_pedido}")
            print(f"   URL Pedido: {url_pedido}")
            print(f"   Fecha: {fecha}  Hora: {hora}")
            print("-" * 50)

    except Exception as e:
        print(f"❌ Error en fila {contador_total + 1}: {e}")
        continue

print(f"\n✅ Total de pedidos encontrados con fecha {fecha_hoy}: {contador_hoy}")

