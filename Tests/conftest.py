import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="class")  
def setup(request):
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
    request.cls.driver = driver
    driver.implicitly_wait(50)
    yield
    print("\n Teardown")
    driver.close()