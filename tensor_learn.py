from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class CityAgentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://192.168.0.234:8080/CityAgent/#/")

    def test_login(self):
        driver = self.driver
        username = driver.find_element_by_id('userid')
        password = driver.find_element_by_id('userpassword')
        submit = driver.find_element_by_id('signmein')
        username.clear()
        username.send_keys('10000000')
        password.clear()
        password.send_keys('asdf12')
        submit.click()
        #btn_click = driver.find_element(By.CLASS_NAME, 'btn.btn-info.ng-binding')
        #btn_click.click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
