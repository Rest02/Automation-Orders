from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


# Carpeta fija donde se guardan las boletas
RUTA_BOLETAS = os.path.abspath("boletas_pdf")


# Función para renombrar PDF generado
def renombrar_pdf(numero_pedido):
    archivos = os.listdir(RUTA_BOLETAS)
    archivos_pdf = [f for f in archivos if f.endswith('.pdf')]

    if not archivos_pdf:
        print("❌ No se encontró ningún PDF.")
        return

    archivo_pdf = max([os.path.join(RUTA_BOLETAS, f) for f in archivos_pdf], key=os.path.getctime)
    nuevo_path = os.path.join(RUTA_BOLETAS, f"boleta_{numero_pedido}.pdf")

    if os.path.exists(nuevo_path):
        os.remove(nuevo_path)

    os.rename(archivo_pdf, nuevo_path)
    print(f"✅ PDF renombrado a: boleta_{numero_pedido}.pdf")

def imprimir_boleta(driver, numero_pedido):
    # Crear carpeta donde se guardarán las boletas
    ruta_descarga = os.path.abspath("boletas_pdf")
    os.makedirs(ruta_descarga, exist_ok=True)

    # service = Service('./chromedriver.exe')
    # options = Options()

    # # Activar impresión automática
    # options.add_argument('--kiosk-printing')

    # prefs = {
    #     'printing.print_preview_sticky_settings.appState': """
    #         {
    #             "recentDestinations": [{
    #                 "id": "Save as PDF",
    #                 "origin": "local",
    #                 "account": "",
    #                 "name": "Save as PDF"
    #             }],
    #             "selectedDestinationId": "Save as PDF",
    #             "version": 2,
    #             "isHeaderFooterEnabled": false,
    #             "mediaSize": {
    #                 "height_microns": 297000,
    #                 "width_microns": 210000,
    #                 "name": "ISO_A4"
    #             },
    #             "marginsType": 1,
    #             "scalingType": 3
    #         }
    #     """,
    #     'savefile.default_directory': ruta_descarga,
    #     'download.prompt_for_download': False,
    #     'download.directory_upgrade': True
    # }

    # options.add_experimental_option('prefs', prefs)

    # driver = webdriver.Chrome(service=service, options=options)
    # driver.get('https://v2.be-flow.com/login')

    # Inicio de sesión
    # driver.find_element(By.NAME, "email").send_keys(os.getenv("BEFLOW_EMAIL"))
    # driver.find_element(By.NAME, "password").send_keys(os.getenv("BEFLOW_PASSWORD"))
    # botonIniciarSesion = driver.find_element(By.CSS_SELECTOR, ".sc-dwalKd.ewKcxc.amplify-button.secondary")
    # botonIniciarSesion.click()

    # time.sleep(5)

    # Ir a la pestaña de Preparación
    preparacion_link = driver.find_element(By.XPATH, "//a[span[text()='Preparación']]")
    preparacion_link.click()
    time.sleep(3)

    # Buscar el pedido
    campo_busqueda = driver.find_element(By.CSS_SELECTOR, "input.ant-input[placeholder='Búsqueda']")
    time.sleep(3)
    campo_busqueda.send_keys(numero_pedido)
    time.sleep(3)

    # Click en el botón de boleta
    driver.find_element(By.CSS_SELECTOR, 'b[role="button"]').click()
    time.sleep(3)


    driver.quit()

    # Renombrar el archivo PDF con el número de pedido
    renombrar_pdf(numero_pedido)

