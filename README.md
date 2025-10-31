# Projeto 09 — Appium (Web mobile – SauceDemo)

## Objetivo
Validar fluxo web **mobile** no Chrome do emulador Android (Login + Menu/Hamburger).

## Como rodar (local)
1) **Emulador** (headless):
2) **Appium**:
3) **Testes**:

## Dependências
- Appium 3.x + driver **uiautomator2**
- Android SDK (cmdline-tools, platform-tools, emulator, **API 34**)
- **Chromedriver 113** em `H:/Appium/drivers/chromedriver.exe`
- Python 3.11 + `pip install -r requirements.txt`

## Estrutura
- `tests/test_web_login.py`  → abre página inicial
- `tests/test_web_menu.py`   → login + valida itens do menu
- `config/appium.conf.json`  → caps (inclui `chromedriverExecutable`)
- `run.ps1`                  → executa suíte e salva JUnit

## Evidências
- JUnit em `.\reports\*.xml` (pronto para CI)
