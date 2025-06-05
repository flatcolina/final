import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def criar_liberacao_econdo(nome, data_checkin, data_checkout):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)  # <<<<<< CORRIGIDO AQUI

    try:
        driver.get('https://app.econdos.com.br/')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-username-input']").send_keys('tiagoddantas@me.com')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-password-input']").send_keys('W3b12345')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-sign-in-button']").click()
        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-occurrence-gate-button']").click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-open-liberation-modal-button']").click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, ".form-control[placeholder='Ex: Diarista, personal trainer, churrasco, etc']").send_keys(nome)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-start-date-input']").send_keys(data_checkin)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-end-date-input']").send_keys(data_checkout)

        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-submit-button']").click()
        time.sleep(10)

        # Pega o link de liberação na tela final (ajuste o seletor se necessário)
        link_elem = driver.find_element(By.CSS_SELECTOR, "[data-testid='share-link-target-link']")
        link = link_elem.text.strip()
        return link
    except Exception as e:
        print("Erro no Selenium:", e)
        return None
    finally:
        driver.quit()
