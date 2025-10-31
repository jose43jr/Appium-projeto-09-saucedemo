param(
  [string]$JUnit = "$(Get-Date -Format yyyyMMdd-HHmmss)-report-junit.xml"
)

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

if (-not (Test-Path ".\reports")) { New-Item -ItemType Directory -Force ".\reports" | Out-Null }

# Checagem rápida: emulador online
$adb = (& adb devices) -join "`n"
if ($adb -notmatch "emulator-.*device") {
  Write-Warning "Nenhum emulador online. Inicie o AVD Pixel_6_API_34 antes de rodar."
}

# Checagem rápida: Appium ativo
try {
  (Invoke-WebRequest -Uri "http://127.0.0.1:4723/status" -UseBasicParsing -TimeoutSec 2) | Out-Null
} catch {
  Write-Warning "Appium não parece rodando em 127.0.0.1:4723. Suba com: appium -p 4723"
}

# Executa testes + JUnit
pytest -q --junitxml ".\reports\$JUnit"
Write-Host "Relatório: $((Resolve-Path ".\reports\$JUnit").Path)"
