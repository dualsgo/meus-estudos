import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Caminho para o ChromeDriver
driver_path = "C:/Users/mdbsi/OneDrive/Área de Trabalho/meus-estudos/testes/chromedriver.exe"
service = Service(driver_path)

def login(driver, username, password):
    """
    Realiza o login em uma página usando Selenium.
    :param driver: Instância do WebDriver.
    :param username: Nome de usuário para login.
    :param password: Senha para login.
    """
    try:
        logging.info("Abrindo a URL de login...")
        driver.get("https://accounts.linxoms.com.br/realms/rihappy/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Finstore.linxoms.com.br%2Frihappy%2Fauth%2Fcallback&client_id=rihappy-client")
        
        # Localizar campos de login
        logging.info("Aguardando campo de usuário...")
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        # Preencher os campos
        logging.info("Preenchendo dados de login...")
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Clicar no botão de login
        logging.info("Clicando no botão de login...")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "kc-login"))
        )
        login_button.click()

        # Aguardar a próxima página carregar (ajustar conforme necessário)
        logging.info("Aguardando carregamento da página pós-login...")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        logging.info("Login realizado com sucesso!")

    except NoSuchElementException as e:
        logging.error(f"Elemento não encontrado: {e}")
        raise
    except TimeoutException as e:
        logging.error(f"Tempo de espera excedido: {e}")
        raise
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        raise

def process_packing_lists(driver):
    """
    Localiza e interage aleatoriamente com os elementos na página de lista de romaneios.
    """
    try:
        logging.info("Navegando para a página de lista de romaneios...")
        driver.get("https://instore.linxoms.com.br/rihappy/packing-lists")

        # Localizar todas as linhas que contêm o botão de envio de declaração de romaneio
        logging.info("Procurando linhas com botões 'Enviar declaração de romaneio'...")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "tr[ng-repeat*='itemPack']")
            )
        )

        if not rows:
            logging.warning("Nenhuma linha com o botão desejado foi encontrada.")
            return

        # Escolher uma linha aleatória
        random_row = random.choice(rows)

        # Localizar o botão de envio de declaração de romaneio na linha escolhida
        send_button = random_row.find_element(
            By.CSS_SELECTOR, "button[ng-click='showDocumentModal(itemPack)']"
        )

        # Verificar se o botão está visível e clicável
        if send_button.is_displayed():
            logging.info("Clicando no botão 'Enviar declaração de romaneio' de uma linha aleatória...")
            send_button.click()

            # Confirmar sem anexo
            logging.info("Aguardando botão 'Confirmar sem anexo'...")
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[ng-click='confirmWithoutDocument()']")
                )
            )
            confirm_button.click()

            # Verificar mensagem de sucesso e clicar em "Ok"
            logging.info("Aguardando mensagem de sucesso...")
            success_modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.modal-body p.ng-binding")
                )
            )
            if "Enviado para despacho com sucesso!" in success_modal.text:
                logging.info("Mensagem de sucesso encontrada, clicando em 'Ok'...")
                ok_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button[ng-click='close()']")
                    )
                )
                ok_button.click()
                time.sleep(.5)  # Esperar 3 segundos antes de encerrar

        else:
            logging.warning("O botão 'Enviar declaração de romaneio' não está visível ou não é clicável.")

    except TimeoutException as e:
        logging.warning(f"Timeout em um dos passos do processo: {e}")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        raise

if __name__ == "__main__":
    logging.info("Iniciando o WebDriver...")
    driver = webdriver.Chrome(service=service)

    try:
        # Dados de login
        username = "1187"
        password = "Rih@ppy2019"

        # Realizar login
        login(driver, username, password)

        # Repetir o envio de romaneios 50 vezes
        for i in range(5000):
            logging.info(f"Iniciando envio {i + 1} de 5000...")
            process_packing_lists(driver)

    finally:
        logging.info("Encerrando o navegador.")
        driver.quit()
