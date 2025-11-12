@echo off
start "" cmd /c "uv run webui.py"
echo Waiting for web server to start...

:waitloop
timeout /t 2 /nobreak >nul
powershell -Command "try { iwr -UseBasicParsing http://127.0.0.1:7860/ >$null; exit 0 } catch { exit 1 }"
if errorlevel 1 goto waitloop

start "" "http://127.0.0.1:7860/"