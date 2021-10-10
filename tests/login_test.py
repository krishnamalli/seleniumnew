import pytest
from pages.loginpage import Loginpage
from pages.homepage import Homepage
from utiles import utile1 as u1
import allure
import moment
@pytest.mark.usefixtures('test_setup')

class TestLogin():

    def test_login(self):


        driver = self.driver
        driver.get(u1.URL)
        login = Loginpage(driver)
        login.enter_username(u1.username)
        login.enter_password(u1.password)
        login.click_login()



    def test_logout(self):
        try:

            driver = self.driver
            home = Homepage(driver)
            home.click_welcome()
            home.click_logout()
            x = driver.title
            assert  x == 'abc'
        except AssertionError as error:
            print('assertion error occured')
            print(error)
            currtime = moment.now().strftime('%d-%m-%Y_%H:%M:%S')#(%d-%m-%Y_%H-%M-%S)
            #screenshotName = 'screenshot_'+currtime
            allure.attach(self.driver.get_screenshot_as_png(),name='screenshot '+currtime,attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print('there was an exception')
            raise

        else:
            print('no exception error')
            raise
        finally:
            print('i am inside finally block')



# command for html report is >>python -m pytest --html=directory/filenamne

