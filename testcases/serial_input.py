#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
v20230727
"""

import pytest
import os, sys
sys.path.append(os.path.dirname(__file__))
#from testcases.variables.common import *
#from testcases.functions.common import *
from functions.common import *
from functions.variables.common import *
from functions.serial_input import *
from functions.variables.serial_input import *
from time import sleep
from selenium import webdriver
pytest.driver = None

class TestSuiteSerialInput:

    @classmethod
    def setup_class(cls):
        print("------ setup before class ------")
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        pytest.driver = webdriver.Chrome(options=options)
        pytest.driver.get(common_string.serial_number_url())
        pytest.driver.maximize_window()
        common_operation.click_if_possible(
            common_selector.accpet_all_cookies_but(), driver=pytest.driver)

    @classmethod
    def teardown_class(cls):
        pytest.driver.close()
        print("------ teardown after class ------")

    def setup_method(self, method):
        print("--- setup before each method ---")
    
    def teardown_method(self, method):
        print("--- teardown after each method ---")
        pytest.driver.refresh()

    @pytest.mark.high
    def test_input_valid_serial_number(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        description = common_operation.check_element_is_existed(
            serial_input_selector.info_description_txt(),
            timeout = 3, driver=pytest.driver)
        part_number = common_operation.check_element_is_existed(
            serial_input_selector.info_part_number_txt(),
            timeout = 1, driver=pytest.driver)
        install_date = common_operation.check_element_is_existed(
            serial_input_selector.info_install_date_txt(),
            timeout = 0.5, driver=pytest.driver)
        end_date = common_operation.check_element_is_existed(
            serial_input_selector.info_end_date_txt(),
            timeout = 0.5, driver=pytest.driver)
        if (description and part_number and install_date and end_date) == False:
            if description == False:
                print("No description info.")
            if part_number == False:
                print("No part number info.")
            if install_date == False:
                print("No install date info.")
            if end_date == False:
                print("No end date info.")
            assert False

    @pytest.mark.middle
    def test_loading_status(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial(), driver=pytest.driver)
        common_operation.click(
            serial_input_selector.get_info_but(), driver=pytest.driver)
        description = common_operation.check_element_is_existed(
            serial_input_selector.info_description_txt(),
            timeout = 0.5, driver=pytest.driver)
        if description == False:
            assert common_operation.check_element_is_existed(
            serial_input_selector.loading_ico(), timeout=0.5, driver=pytest.driver)

    @pytest.mark.high
    def test_input_invalid_serial_number_shorter(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.invalid_serial_shorter(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico(),
            timeout=3, driver=pytest.driver)

    @pytest.mark.middle
    def test_input_invalid_serial_number_longer(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.invalid_serial_longer(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico(),
            timeout=3, driver=pytest.driver)

    @pytest.mark.middle
    def test_input_empty_serial(self):
        serial_input_operation.input_serial_numvers(
            "", driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico(),
            timeout=3, driver=pytest.driver)

    @pytest.mark.low
    def test_input_special_char(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.special_char(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico(),
            timeout=3, driver=pytest.driver)

    @pytest.mark.middle
    def test_input_again_after_getting_info(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        part_number = common_operation.get_text(
            serial_input_selector.info_part_number_value_txt(),
            timeout = 1, driver=pytest.driver)

        serial_input_operation.input_serial_numvers(
            serial_input_string.anoter_valid_serial(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        another_part_number = common_operation.get_text(
            serial_input_selector.info_part_number_value_txt(),
            timeout = 1, driver=pytest.driver)

        if part_number == another_part_number:
            print("There info should be different",
                  part_number, another_part_number)
            assert False

    @pytest.mark.middle
    def test_input_again_after_worng_input(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.invalid_serial_shorter(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        common_operation.get_element(
            serial_input_selector.error_on_input_ico(),
            timeout=3, driver=pytest.driver)

        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial(), driver=pytest.driver)
        serial_input_operation.get_info_includes_wait(driver=pytest.driver)
        assert common_operation.check_element_is_existed(
            serial_input_selector.info_end_date_txt(),
            timeout = 3, driver=pytest.driver)
