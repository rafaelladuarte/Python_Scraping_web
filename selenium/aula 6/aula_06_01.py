from selenium.webdriver import Firefox

uri = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()
b.get(uri)

b.find_element_by_css_selector(
    'input'
).send_keys('elladarte')