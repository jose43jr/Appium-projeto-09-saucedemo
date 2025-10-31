import json, pathlib, time, pytest
from appium import webdriver

# ==== opções com fallback ====
try:
    # caminho preferido (clientes mais novos)
    from appium.options.android.uiautomator2 import UiAutomator2Options as Opts
except Exception:
    try:
        # alguns builds expõem direto em appium.options.android
        from appium.options.android import UiAutomator2Options as Opts
    except Exception:
        # fallback genérico
        from appium.options.common import AppiumOptions as Opts

@pytest.fixture(scope="session")
def caps():
    cfg = json.loads(pathlib.Path("config/appium.conf.json").read_text(encoding="utf-8"))
    return cfg["server"]["url"], cfg["caps"]

@pytest.fixture
def driver(caps):
    server_url, desired = caps
    opts = Opts()
    # carrega capacidades do JSON
    if hasattr(opts, "load_capabilities"):
        opts.load_capabilities(desired)
    else:
        for k, v in desired.items():
            try:
                opts.set_capability(k, v)
            except Exception:
                pass
    drv = webdriver.Remote(server_url, options=opts)
    time.sleep(1.0)
    yield drv
    drv.quit()
