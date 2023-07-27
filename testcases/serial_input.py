#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
v20230728
"""

import pytest
import os, sys
sys.path.append(os.path.dirname(__file__))
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
        pytest.driver = common_operation.open_browser()
        serial_input_operation.set_default_driver(pytest.driver)
        common_operation.click_if_possible(
            common_selector.accpet_all_cookies_but)

    @classmethod
    def teardown_class(cls):
        print("------ teardown after class ------")
        pytest.driver.close()

    #def setup_method(self, method):
    #    print("--- setup before each method ---")
    
    def teardown_method(self, method):
        print("--- teardown after each method ---")
        pytest.driver.refresh()

    @pytest.mark.high
    def test_input_valid_serial_number(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial)
        serial_input_operation.get_info_includes_wait()
        description = common_operation.check_element_is_existed(
            serial_input_selector.info_description_txt, timeout = 3)
        part_number = common_operation.check_element_is_existed(
            serial_input_selector.info_part_number_txt, timeout = 1)
        install_date = common_operation.check_element_is_existed(
            serial_input_selector.info_install_date_txt, timeout = 0.5)
        end_date = common_operation.check_element_is_existed(
            serial_input_selector.info_end_date_txt, timeout = 0.5)
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
        description_value = common_operation.get_text(
            serial_input_selector.info_description_value_txt,
            timeout = 1)
        part_number_value = common_operation.get_text(
            serial_input_selector.info_part_number_value_txt,
            timeout = 0.5)
        install_date_value = common_operation.get_text(
            serial_input_selector.info_install_date_value_txt,
            timeout = 0.5)
        end_date_value = common_operation.get_text(
            serial_input_selector.info_end_date_value_txt,
            timeout = 0.5)
        if (len(description_value) * len(part_number_value) * len(install_date_value) * len(end_date_value) == 0):
            if (len(description_value) == 0):
                print("Empty description value.")
            if (len(part_number_value) == 0):
                print("Empty part number value.")
            if (len(install_date_value) == 0):
                print("Empty install date value.")
            if (len(end_date_value) == 0):
                print("Empty end date value.")
            assert False

    @pytest.mark.middle
    def test_loading_status(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial)
        common_operation.click(
            serial_input_selector.get_info_but)
        assert common_operation.check_element_is_existed(
            serial_input_selector.loading_ico, timeout=3)

    @pytest.mark.high
    def test_input_invalid_serial_number_shorter(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.invalid_serial_shorter)
        serial_input_operation.get_info_includes_wait()
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico, timeout=3)

    @pytest.mark.middle
    def test_input_invalid_serial_numbers(self):
        for invalid_serial in serial_input_string.invalid_serial_numbers:
            serial_input_operation.input_serial_numvers(invalid_serial)
            serial_input_operation.get_info_includes_wait()
            assert common_operation.check_element_is_existed(
                serial_input_selector.error_on_input_ico, timeout=3)
            pytest.driver.refresh()

    @pytest.mark.middle
    def test_input_empty_serial(self):
        serial_input_operation.input_serial_numvers(
            "")
        serial_input_operation.get_info_includes_wait()
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico,
            timeout=3)

    @pytest.mark.low
    def test_input_special_char(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.special_char)
        serial_input_operation.get_info_includes_wait()
        assert common_operation.check_element_is_existed(
            serial_input_selector.error_on_input_ico, timeout=3)

    @pytest.mark.middle
    def test_input_again_after_getting_info(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial)
        serial_input_operation.get_info_includes_wait()
        install_date = common_operation.get_text(
            serial_input_selector.info_install_date_value_txt, timeout = 1)

        serial_input_operation.input_serial_numvers(
            serial_input_string.anoter_valid_serial)
        serial_input_operation.get_info_includes_wait()
        another_install_date = common_operation.get_text(
            serial_input_selector.info_install_date_value_txt, timeout = 1)

        if install_date == another_install_date:
            print("There info should be different", install_date)
            assert False

    @pytest.mark.middle
    def test_input_again_after_worng_input(self):
        serial_input_operation.input_serial_numvers(
            serial_input_string.invalid_serial_shorter)
        serial_input_operation.get_info_includes_wait()
        common_operation.get_element(
            serial_input_selector.error_on_input_ico, timeout=3)

        serial_input_operation.input_serial_numvers(
            serial_input_string.valid_serial)
        serial_input_operation.get_info_includes_wait()
        assert common_operation.check_element_is_existed(
            serial_input_selector.info_end_date_txt, timeout = 3)
