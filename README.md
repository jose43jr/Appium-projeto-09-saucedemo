![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Appium](https://img.shields.io/badge/Appium-3.x-success)
![Android](https://img.shields.io/badge/Android-API_34-brightgreen)
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

## Limitações conhecidas
- Chrome do emulador (v113) exige Chromedriver 113 apontado em `config/appium.conf.json`.
- Testes cobrem navegação básica (login + menu). Não há mocks nem cobertura offline.

## Roadmap curto (próximas iterações)
- ✅ (feito) Login + Menu
- ⬜ Checkout simples (validar fluxo até o resumo)
- ⬜ Pipeline CI (GitHub Actions) com AVD headless
- ⬜ Captura automática de screenshot ao falhar (`pytest --maxfail=1 -q` + hook)

## Como eu trabalhei
- Priorizei rodar de ponta a ponta antes de “embelezar”.
- Documentei só o essencial e gerei JUnit para CI desde o começo.

## Créditos & contato
Autor: José Feitosa Jr — feitosa34jr@gmail.com
