#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
v20230726
"""

import pytest
import os
from selenium import webdriver
from time import sleep
pytest.driver = None

class TestClass:

    @classmethod
    def setup_class(cls):
        print("------ setup before class ------")
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        pytest.driver = webdriver.Chrome(options=options)
        pytest.driver.get('https://google.com')
        pytest.driver.maximize_window()
        sleep(3)

    @classmethod
    def teardown_class(cls):
        pytest.driver.close()
        #sleep(1)
        print("------ teardown after class ------")

    def setup_method(self, method):

        print("--- setup before each method ---")
    
    def teardown_method(self, method):

        print("--- teardown after each method ---")

    @pytest.mark.webtest
    def test_method(self):
        print("Browser")
        pytest.driver.get('https://yahoo.com')
        #assert 1==2
