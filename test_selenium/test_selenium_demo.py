import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTestbaidu():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    # def teardown_method(self):
    #     self.driver.quit()

    def test_cookie(self):

        cookies = self.driver.get_cookies()

        with open("cookie.json", "w") as f:

            json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()

