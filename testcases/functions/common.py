from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os, sys
sys.path.append(os.path.dirname(__file__))
from variables.common import *

class common_operation:
	default_driver = None

	@staticmethod
	def open_browser(url=common_string.serial_number_url(), set_to_default=True):
		options = webdriver.ChromeOptions()
		options.add_argument("--log-level=3")
		driver = webdriver.Chrome(options=options)
		driver.get(common_string.serial_number_url())
		driver.maximize_window()
		if set_to_default:
			common_operation.set_default_driver(driver)
		return driver

	def close_browser(driver=None, clean_default=True):
		if driver == None:
			driver = common_operation.default_driver
		driver.close()
		if clean_default:
			default_driver = None

	@staticmethod
	def set_default_driver(driver):
		common_operation.default_driver = driver

	@staticmethod
	def get_element(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		xpath_format = "xpath:"
		id_format = "id:"
		wait = WebDriverWait(timeout=timeout, driver=driver)
		
		if xpath_format in selector:
			first_index = selector.index(xpath_format)
			selector = selector[first_index + len(xpath_format):]
			return wait.until(EC.presence_of_element_located((By.XPATH, selector)))
		else:
			if id_format in selector:
				selector = selector[selector.index(id_format) + len(id_format):]
			return wait.until(EC.presence_of_element_located((By.ID, selector)))
	
	def wait_until_element_invisible(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		xpath_format = "xpath:"
		id_format = "id:"
		wait = WebDriverWait(timeout=timeout, driver=driver)
		
		if xpath_format in selector:
			first_index = selector.index(xpath_format)
			selector = selector[first_index + len(xpath_format):]
			return wait.until(EC.invisibility_of_element_located((By.XPATH, selector)))
		else:
			if id_format in selector:
				selector = selector[selector.index(id_format) + len(id_format):]
			return wait.until(EC.invisibility_of_element_located((By.ID, selector)))

	@staticmethod
	def click(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		common_operation.get_element(selector, timeout=timeout, driver=driver).click()

	def move_to(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		element = common_operation.get_element(selector, timeout=timeout, driver=driver)
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()

	def click_if_possible(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		common_operation.click(selector, timeout=timeout, driver=driver)
		try:
			common_operation.click(selector, timeout=timeout, driver=driver)
		except:
			print("No targeted selector:", selector)

	def check_element_is_existed(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		try:
			common_operation.get_element(selector, timeout=timeout, driver=driver)
			return True
		except:
			return False

	def get_text(selector, timeout=10, driver=None):
		if driver == None:
			driver = common_operation.default_driver
		return common_operation.get_element(selector, timeout=timeout, driver=driver).text

