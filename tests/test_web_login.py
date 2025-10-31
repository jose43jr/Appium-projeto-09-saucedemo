def test_saucedemo_home(driver):
    driver.get("https://www.saucedemo.com/")
    # CSS no contexto mobile (Chrome Android)
    user = driver.find_element("css selector", "#user-name")
    pwd  = driver.find_element("css selector", "#password")
    btn  = driver.find_element("css selector", "#login-button")
    assert user.is_displayed() and pwd.is_displayed() and btn.is_displayed()
