from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse

uri = 'https://curso-python-selenium.netlify.app/exercicio_03.html'

def find_a_by_href(browser, attr, val):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.get_attribute(attr) == val:
            return elemento

def find_a_by_content(browser, content):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.text == content:
            return elemento


browser = Firefox()
browser.get(uri)



# Pagina 1
sleep(10)
main = browser.find_element_by_tag_name("main")
main.find_element_by_tag_name('a').click()


# Pagina 2
sleep(20)
main = browser.find_element_by_tag_name("main")
find_a_by_href(main,'attr','errado').click()


# Pagina 3
sleep(30)
main = browser.find_element_by_tag_name("main")
find_a_by_content(main, browser.title).click()

# Pagina 4
sleep(40)
main = browser.find_element_by_tag_name('main')
parsed_url = urlparse(browser.current_url)
find_a_by_content(main, parsed_url.path[1:]).click()

# pagina 4
sleep(50)
browser.refresh()