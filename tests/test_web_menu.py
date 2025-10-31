from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_menu(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # abrir menu (hamburger)
    driver.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn").click()

    wait = WebDriverWait(driver, 10)
    # aguarda wrapper do menu abrir (evita animação/overlay)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bm-menu-wrap")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bm-item-list")))

    # validar itens (via CSS)
    selectors = [
        "#inventory_sidebar_link",
        "#about_sidebar_link",
        "#logout_sidebar_link",
        "#reset_sidebar_link",
    ]
    for sel in selectors:
        el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, sel)))
        assert el.is_displayed(), f"Item {sel} não visível"
