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

    # 📄 Click en el botón de boleta
    driver.find_element(By.CSS_SELECTOR, 'b[role="button"]').click()


    time.sleep(5)

    # 🛑 Esperar a que cargue el contenido de la boleta (ajusta el selector si es necesario)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "print-preview-app"))
    )

    # 🧠 Esperar unos segundos extra para asegurar render completo
    time.sleep(3)

    # 🖨 Inyectar impresión retrasada manualmente (opcional si el sitio lanza window.print solo)
    driver.execute_script("""
        const originalPrint = window.print;
        window.print = function() {
            console.log("Esperando antes de imprimir...");
            setTimeout(() => {
                originalPrint();
            }, 2000); // 2 segundos de espera
        };
    """)

    # ✅ Si ya se lanza automáticamente, simplemente espera
    # Si no, puedes forzarlo con:
    driver.execute_script("window.print();")

    # Esperar impresión
    time.sleep(5)

    driver.quit()