import time
import unittest
from selenium import webdriver
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # def setUp(self):
        cls.driver = webdriver.Chrome(executable_path="././Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search001(self):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_name("q")
        search.send_keys("Automation Step By Step")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(10)
        print(" ############ 3")
        print(self.driver.title)

    def test_search002(self):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_name("q")
        search.send_keys("Coursera")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(10)
        print(" ############ 3")
        print(self.driver.title)

    def test_search003(self):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_name("q")
        search.send_keys("Udemy")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(10)
        print(" ############ 3")
        print(self.driver.title)

    def test_search004(self):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_name("q")
        search.send_keys("docker")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(10)
        print(" ############ 3")
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        # def tearDown(self):
        cls.driver.close()
        cls.driver.quit()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/SeleniumAutomation/TestReport'))
