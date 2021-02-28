from selenium.webdriver import Selenium

url = 'http://selenium.dunossauro.live/aula_05_a.html'

firefox = Firefox()
firefox.get(url)

div_python = firefox.find_element_by_id('python')
div_haskell = firefox.find_element_by_id('haskell')
print(div_haskell.text)

firefox.quit()