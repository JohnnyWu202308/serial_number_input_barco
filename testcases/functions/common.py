#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
default_driver = ""

class common_operation:
	@staticmethod
	def get_element(selector, timeout=10, driver=default_driver):
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
	
	def wait_until_element_invisible(selector, timeout=10, driver=default_driver):
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
	def click(selector, timeout=10, driver=default_driver):
		common_operation.get_element(selector, timeout=timeout, driver=driver).click()

	def move_to(selector, timeout=10, driver=default_driver):
		element = common_operation.get_element(selector, timeout=timeout, driver=driver)
		actions = ActionChains(driver)
		actions.move_to_element(element).perform()

	def click_if_possible(selector, timeout=10, driver=default_driver):
		try:
			common_operation.click(selector, timeout=timeout, driver=driver)
		except:
			print("No targeted selector:", selector)

	def check_element_is_existed(selector, timeout=10, driver=default_driver):
		try:
			common_operation.get_element(selector, timeout=timeout, driver=driver)
			return True
		except:
			return False
	def get_text(selector, timeout=10, driver=default_driver):
		return common_operation.get_element(selector, timeout=timeout, driver=driver).text

