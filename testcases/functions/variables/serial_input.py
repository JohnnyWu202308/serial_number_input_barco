class serial_input_selector:
	def get_info_but():
		return "xpath: //button[(normalize-space(text())='Get info')]"
	def loading_ico():
		return "xpath://*[contains(@class, 'is-loading')]"
	def serial_input_tb():
		return "id:serial"
	def error_on_input_ico():
		return "xpath://*[(@id='serial') and contains(@class, 'is-invalid')]"
	def info_description_txt():
		return "xpath://*[(normalize-space(text())='Description')]"
	def info_description_value_txt():
		return "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[1]"
	def info_part_number_txt():
		return "xpath://*[(normalize-space(text())='Part number')]"
	def info_part_number_value_txt():
		return "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[2]"
	def info_install_date_txt():
		return "xpath://*[(normalize-space(text())='Installation date')]"
	def info_install_date_value_txt():
		return "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[3]"
	def info_end_date_txt():
		return "xpath://*[(normalize-space(text())='Warranty end date')]"
	def info_end_date_value_txt():
		return "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[4]"
	
class serial_input_string:
	def valid_serial():
		return "1863552437"
	def anoter_valid_serial(): #just take it for test, can replace to any other valid input
		return "1863552438"
	def invalid_serial_shorter():
		return "186355243"
	def invalid_serial_longer():
		return "18635524370"
	def special_char():
		return "~!@#$%^&*()_+|./\\[]{}'\",.<>"
