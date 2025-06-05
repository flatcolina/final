import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def criar_liberacao_econdo(nome, data_checkin, data_checkout):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)

    wait = WebDriverWait(driver, 20)  # Até 20s para cada etapa

    try: 

        driver.get('https://app.econdos.com.br/')

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='login-username-input']"))).send_keys('tiagoddantas@me.com')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-password-input']").send_keys('W3b12345')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-sign-in-button']").click()

        # Aguarda o dashboard carregar e o botão ficar visível
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='feed-occurrence-gate-button']"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='feed-open-liberation-modal-button']"))).click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control[placeholder='Ex: Diarista, personal trainer, churrasco, etc']"))).send_keys(nome)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-start-date-input']").send_keys(data_checkin)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-end-date-input']").send_keys(data_checkout)

        # Aguarda o botão "Salvar" ficar clicável e clica
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='create-authorized-person-submit-button']"))).click()

        # Espera o link de liberação aparecer (pode levar alguns segundos)
        link_elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='share-link-target-link']")))
        link = link_elem.text.strip()
        return link
    except Exception as e:
        print("Erro no Selenium:", e)
        return None
    finally:
        driver.quit()
