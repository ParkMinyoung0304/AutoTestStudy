import pytest
from selenium import webdriver
from time import sleep, ctime
import os

options = webdriver.ChromeOptions()
# 这里时chrome浏览器可执行文件的地址
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
# 这里时浏览器驱动地址
chrome_driver_binary = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# 测试类
class TestCase():
    def setup_class(self):
        print("START")#执行一次
    def teardown_class(self):
        print("ENDING")#执行一次

    def setup_method(self):
        driver.get("http://www.baidu.com")
    def teardown_method(self):
        sleep(3)

    def test_selenium_text(self):
        driver.find_element_by_id("kw").send_keys("Test search")
        driver.find_element_by_id("su").click()

    def test_selenium_blank(self):
        driver.find_element_by_id("kw").send_keys("     ")
        driver.find_element_by_id("su").click()

    def test_selenium_none(self):
        driver.find_element_by_id("kw").send_keys("")
        driver.find_element_by_id("su").click()

    def test_selenium_characters(self):
        driver.find_element_by_id("kw").send_keys("***")
        driver.find_element_by_id("su").click()


    def test_selenium_number(self):
        driver.find_element_by_id("kw").send_keys("123")
        driver.find_element_by_id("su").click()

    def test_selenium_superchar(self):
        driver.find_element_by_id("kw").send_keys("111111111111111111111111111111111111111111111111111111111111111111111111111")
        driver.find_element_by_id("su").click()

        



