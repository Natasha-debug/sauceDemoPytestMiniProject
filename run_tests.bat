@echo off
echo =============================================
echo   Running SauceDemo Pytest Selenium Tests
echo =============================================

:: Install dependencies (only needed first time)
pip install -r requirement.txt

:: Run pytest and generate HTML report
pytest --html=reports/report.html --self-contained-html

echo =============================================
echo   Test execution completed. Check the report:
echo   reports\report.html
echo =============================================

pause
