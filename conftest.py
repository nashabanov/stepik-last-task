import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_language',
                     action='store',
                     default=None,
                     help="Choose user language: en, ru, es etc...")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("user_language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path=r'C:\Users\shna\selenium_env\Scripts\chromedriver.exe', options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=r"C:\Users\shna\selenium_env\Scripts\geckodriver.exe", firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


