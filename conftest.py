import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language ru/en')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser_lang = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = chrome_options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        print(f"\nsetting browser language as {browser_lang}")
        print("\nstarting chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstarting firefox browser for test...")
        options = firefox_options()
        options.set_preference("intl.accept_languages", browser_lang)
        print(f"\nsetting browser language as {browser_lang}")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()