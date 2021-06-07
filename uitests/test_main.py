#!/usr/bin/env python
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import pytest
from appium import webdriver
import os
import time

caps = {
    "platformName": "awtk",
    "a4aHost": "localhost",
    "a4aPort": 8000
}

app = "../bin/demo"

class Testcase1():
    driver = None

    def setup_class(self):
        os.system(app + " >/dev/null &")
        time.sleep(0.5)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        assert self.driver is not None

    def teardown_class(self):
        self.driver.quit()

    def test_set_edit(self):
        edit = self.driver.find_element_by_id("edit")
        edit.clear()
        assert edit.text == ""
        text = "123456"
        edit.send_keys(text)
        assert edit.text == text


if __name__ == "__main__":
    pytest.main(['-s', '-v'])
