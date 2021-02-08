"""Exemplo de PO no google.com."""
from selenium import webdriver


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        # id
        self.search_bar = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
        # name
        self.btn_search = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'
        # name
        self.btn_lucky = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[2]'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_xpath(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(
            self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_id(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_xpath(
            self.btn_lucky).click()


ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
g.search('Live de Python')
ff.quit()
