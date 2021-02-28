from selenium.webdriver import Firefox

url = 'http://selenium.dunossauro.live/aula_05_b.html'

browser = Firefox()
browser.get(url)

topico = browser.find_element_by_class_name('topico')
linguagens = browser.find_element_by_class_name('linguagens')   

for linguagem in list(linguagens):
    print(
        (linguagem.find_element_by_tag_name('h2').text,
        linguagem.find_element_by_tag_name('p').text)
    )
