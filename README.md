# sktb_automation

### import pack  
```python  
from selenium import webdriver
from bs4 import BeautifulSoup
```  
  
### use phantomjs
```python  
driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
```  
  
### use chrome
```python  
driver = webdriver.Chrome()
```  
  
pyinstaller -i main.ico -F __init__.py
