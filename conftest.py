import pytest

def pytest_addoption(parser):
    parser.addoption('--browser',action='store',default='chrome',help='type in browser')


@pytest.fixture(scope='class')

def test_setup(request):

    from selenium import webdriver

    browser = request.config.getoption('--browser')
    if browser == 'chrome':

        driver = webdriver.Chrome(executable_path='C://Users/krish/PycharmProjects/automationselenium/driver/chromedriver.exe')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='')

    driver.implicitly_wait(5)

    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
    print('test is completed')