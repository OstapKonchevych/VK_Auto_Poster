

$PYTHON_FILE_URL = "https://raw.githubusercontent.com/OstapKonchevych/VK_Auto_Poster/main/_vkap.py"

$RUN_PATH = split-path -parent $MyInvocation.MyCommand.Definition

$DOWNLOAD_PATH = "$RUN_PATH\_vkap.py"

if (Test-Path $DOWNLOAD_PATH -PathType leaf)
{
    Remove-Item $DOWNLOAD_PATH
}

Write-Output "[INFO] Downloading file..."

Invoke-WebRequest -URI $PYTHON_FILE_URL -OutFile $DOWNLOAD_PATH

Write-Output "[OK] Download complete"
Write-Output "[INFO] Running program"

python3.10.exe .\_vkap.py | Out-File -FilePath .\_log.txt

Write-Host "Press any key to continue..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")