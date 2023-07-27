# Environment
	- Python 3.7.2
	- Python Library(you can use command "pip3 install -r requirement.txt")
		- pytest==7.4.0
		- selenium==4.10.0
		- urllib3==1.26.6
	- Chromedriver mactch your chrome version.(download link : https://chromedriver.chromium.org/downloads )
		And put this chromerdriver on path(in general, you can put on python install path or same level path of pytest command executed)
		
# Execute Command
	"pytest -v interface.py"
	Suggest execute on same level of interface.py
	(you can also try "pytest -v -m high interface.py" or middle, low for test cases with targeted mark)
	
# How to Modify Test Cases
	go to \testcases
	
# How to Modify Functions
	go to \testcases\functions
	
# How to Modify Selector Or String
	go to \testcases\functions\variables

# Basic Structure Introduce
	Try to separate string, seletor, functions and test cases into different parts.
	(although test cases still in programic structure)
	At least we can more easier to modify selector or string if we want.
	(however if behavior changed, still need deeper knowledge to adjust)
