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

def Preparar_pedido(numero_de_pedido):

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


    # Ir a la página de pedidos en proceso
    boton = driver.find_element(By.XPATH, "//button[span[text()='En proceso']]")
    boton.click()


    time.sleep(3)


    # Introducir el número de pedido en el campo de búsqueda
    campo_busqueda = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Búsqueda"]')
    campo_busqueda.send_keys(numero_de_pedido)


    time.sleep(5)

    # Hacer click en el enlace del pedido
    enlace = driver.find_element(By.LINK_TEXT, numero_de_pedido)
    enlace.click()

    time.sleep(3)

    # Hacer click en el enlace del pedido para preparar
    enlace = driver.find_element(By.XPATH, "//a[contains(@href, '/fulfillments/') and u[text()='"+numero_de_pedido+"-"+"F1"+"']]")
    enlace.click()


    time.sleep(3)
    # Hacer click en el botón de confirmar pickup up
    boton_si = driver.find_element(By.ID, "confirm-pickup")
    boton_si.click()

    time.sleep(3)

    # Hacer click en boton preparación rapida  
    boton_preparacion = driver.find_element(By.XPATH, "//button[.//span[text()='Preparación rápida']]")
    boton_preparacion.click()

    time.sleep(3)

    # Hacer click en boton confirmar
    boton_confirmar = driver.find_element(By.XPATH, "//button[span[text()='Confirmar']]")
    boton_confirmar.click() 

    time.sleep(10)

    # Refrescar la página en caso de que no se actualice para la boleta
    driver.refresh()
    driver.refresh()
    driver.refresh()



    time.sleep(3)

    # Encuentra el campo de búsqueda
    campo_busqueda = driver.find_element(By.CSS_SELECTOR, "input.ant-input[placeholder='Búsqueda']")

    # Introduce el número de pedido en el campo de búsqueda
    campo_busqueda.send_keys(numero_de_pedido)

    time.sleep(3)


    # Hacer click en el botón de imprimir boleta
    svg_element = driver.find_element(By.XPATH, "//svg[contains(@viewBox, '0 0 24 24')]")
    svg_element.click()

    time.sleep(3)

    # Hacer click en el botón de imprimir
    elemento_imprimir = driver.find_element(By.CSS_SELECTOR, "div.svelte-1w9r7lo.content")
    elemento_imprimir.click()

    time.sleep(3)

    # Hacer click en el checkbox de pedido
    checkbox = driver.find_element(By.CLASS_NAME, "ant-checkbox-input")
    checkbox.click()



    # Hacer click en el menu desplegable de acciones
    boton = driver.find_element(By.CSS_SELECTOR, "button.ant-dropdown-trigger")
    boton.click()


    time.sleep(3)


    # Esperar a que aparezca el elemento y luego hacer clic para enviar a entregas
    enviar_btn = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Enviar a entregas (1)']"))
    )
    enviar_btn.click()






    # Configuración de pruebas para imprimir boleta



    time.sleep(10)
    
    






