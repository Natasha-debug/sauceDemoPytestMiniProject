@echo off
echo =============================================
echo   Running SauceDemo Pytest Selenium Tests
echo =============================================

:: Install dependencies (only needed first time)
pip install -r requirement.txt

:: Run pytest and generate HTML report
pytest --html=reports/report.html --self-contained-html

:: Step 3 — Run Behave feature tests
echo =============================================
echo   Running BEHAVE (BDD) tests...
echo =============================================
behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html -f pretty

echo =============================================
echo   Test execution completed successfully!
echo   PYTEST Report: reports\pytest_report.html
echo   BEHAVE Report: reports\behave_report.html
echo =============================================

pause

