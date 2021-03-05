from selenium.webdriver import Firefox

url = 'https://selenium.dunossauro.live/keyboard'

b = Firefox()
b.get(url)

html = b.find_element_by_tag_name('html')

html.send_keys('selenium')