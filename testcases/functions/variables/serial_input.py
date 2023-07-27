class serial_input_selector:
	get_info_but = "xpath: //button[(normalize-space(text())='Get info')]"
	loading_ico = "xpath://*[contains(@class, 'is-loading')]"
	serial_input_tb = "id:serial"
	error_on_input_ico = "xpath://*[(@id='serial') and contains(@class, 'is-invalid')]"
	info_description_txt = "xpath://*[(normalize-space(text())='Description')]"
	info_description_value_txt = "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[1]"
	info_part_number_txt = "xpath://*[(normalize-space(text())='Part number')]"
	info_part_number_value_txt = "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[2]"
	info_install_date_txt = "xpath://*[(normalize-space(text())='Installation date')]"
	info_install_date_value_txt = "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[3]"
	info_end_date_txt = "xpath://*[(normalize-space(text())='Warranty end date')]"
	info_end_date_value_txt = "xpath://*[contains(@class, 'cmp-product-warranty__list')]/dd[4]"
	
class serial_input_string:
	valid_serial = "1863552437"
	anoter_valid_serial = "1863552438" #just take it for test, can replace to any other valid input
	invalid_serial_shorter = "186355243"
	invalid_serial_numbers = ["18635524370", "123", "中文測試字串中文測試字串", "qaz123456", "中文andEnglish", "中文&English"]
	special_char = "~!@#$%^&*()_+|./\\[]{}'\",.<>"
