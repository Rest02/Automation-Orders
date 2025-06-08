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
from inicio_sesion import Iniciar_sesion
from prepr_and_boleta import imprimir_boleta
from enviar_entregas import enviar_entregas



# Cargar variables de entorno
load_dotenv()

def Preparar_pedido(numero_de_pedido):



    driver = Iniciar_sesion()

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

    imprimir_boleta(driver, numero_de_pedido)

    time.sleep(5)

    enviar_entregas(driver)

    time.sleep(10)

    driver.quit()




