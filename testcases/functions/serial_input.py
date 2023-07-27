import os, sys
sys.path.append(os.path.dirname(__file__))
from common import *
from variables.serial_input import *

class serial_input_operation:
	default_driver = None

	def set_default_driver(driver):
		serial_input_operation.default_driver = driver

	def get_info_includes_wait(timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		common_operation.click(
            serial_input_selector.get_info_but(), timeout=timeout, driver=driver)
		common_operation.wait_until_element_invisible(
			serial_input_selector.loading_ico(), driver=driver)
			
	def input_serial_numvers(serial_numbers, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		targeted = common_operation.get_element(
            serial_input_selector.serial_input_tb(), driver=driver)
		targeted.clear()
		targeted.send_keys(serial_numbers)

