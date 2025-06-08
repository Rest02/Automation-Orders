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
from selenium.webdriver.common.action_chains import ActionChains


# Cargar variables de entorno
load_dotenv()




def enviar_entregas(driver):
    time.sleep(5)


    # Hacer click en el checkbox de pedido
    checkbox = driver.find_element(By.CSS_SELECTOR, 'input.ant-checkbox-input')
    checkbox.click()
    time.sleep(3)

    # Hacer click en el botón de acciones
    boton_acciones = driver.find_element(By.XPATH, "//button[div[contains(text(), 'Acciones')]]")
    boton_acciones.click()
    time.sleep(3)

    opcion_enviar_entregas = driver.find_element(
        By.XPATH,
        "//span[@class='ant-dropdown-menu-title-content']/span[text()='Enviar a entregas (1)']"
    )
    opcion_enviar_entregas.click()
    time.sleep(3)

    # ===== HACER CLIC EN EL BOTÓN "CONFIRMAR" =====
    # Este es el paso más complejo porque el botón tiene elementos superpuestos
    wait = WebDriverWait(driver, 15)

    try:
        # 1. Encontrar el botón que contiene el texto "Confirmar"
        boton_confirmar = wait.until(EC.presence_of_element_located((By.XPATH, '//button[.//b[text()="Confirmar"]]')))
        
        # 2. Hacer scroll para que el botón esté visible en pantalla
        driver.execute_script("arguments[0].scrollIntoView(true);", boton_confirmar)
        time.sleep(2)  # Esperar a que termine el scroll
        
        # 3. Usar JavaScript para hacer clic (evita problemas de elementos superpuestos)
        # Simula eventos de mouse reales: mousedown -> mouseup -> click
        driver.execute_script("""
            var button = arguments[0];
            button.focus();
            button.dispatchEvent(new MouseEvent('mousedown', {bubbles: true}));
            button.dispatchEvent(new MouseEvent('mouseup', {bubbles: true}));
            button.dispatchEvent(new MouseEvent('click', {bubbles: true}));
        """, boton_confirmar)
        
        time.sleep(2)
        
        # 4. Verificar que el clic funcionó esperando a que desaparezca el modal
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//b[text()="¿Confirma que imprimió y pegó las etiquetas de couriers para las órdenes seleccionadas?"]')))
        print("✅ Botón Confirmar clickeado exitosamente - Modal cerrado")

    except Exception as e:
        # 5. Si el método principal falla, usar método de respaldo con ActionChains
        print(f"⚠️ Método principal falló, usando método alternativo: {e}")
        try:
            # Encontrar botón por su clase CSS específica
            boton_confirmar_alt = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="sc-iHGNWf dKhWKq"]')))
            
            # Mover cursor al botón y hacer clic
            actions = ActionChains(driver)
            actions.move_to_element(boton_confirmar_alt).click().perform()
            time.sleep(2)
            
            # Verificar que funcionó
            wait.until(EC.invisibility_of_element_located((By.XPATH, '//b[text()="¿Confirma que imprimió y pegó las etiquetas de couriers para las órdenes seleccionadas?"]')))
            print("✅ Método alternativo funcionó - Modal cerrado")
            
        except Exception as e2:
            print(f"❌ Error: No se pudo hacer clic en el botón Confirmar: {e2}")


    time.sleep(10)



