import time
import requests
import json
from utils.urlPage import Paginas
from abc import ABC
from selenium.webdriver import ActionChains
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (presence_of_element_located,
                                                            text_to_be_present_in_element,
                                                            element_to_be_clickable)
from selenium.webdriver.common.keys import Keys


class Comandos(ABC):
    def __init__(self, webdriver):
        self.driver = webdriver
        self.espera = WebDriverWait(self.driver, 5, poll_frequency=0.5)

    def navegar(self, url):
        self.driver.get(url)

    def clicar(self, locator):
        self.espera.until(presence_of_element_located(locator))
        elemento = self.espera.until(element_to_be_clickable(locator))
        try:
            elemento.click()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
            elemento.click()

    def capturar_url(self):
        return self.driver.current_url

    def obterTexto(self, locator):
        self.espera.until(presence_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def obterElemento(self, locator):
        try:
            self.espera.until(presence_of_element_located(locator))
            return self.driver.find_element(*locator)
        except(TimeoutException):
            raise TypeError("Não foi encontrado o elemento")

    def obterTextoDoElemento(self, elemento):
        return elemento.text

    def obterElementos(self, elemento, locator):
        return elemento.find_elements(*locator)

    def esperar_elemento(self, locator):
        self.espera.until(presence_of_element_located(locator))

    def esperarTexto(self, elemento, texto):
        self.espera.until(text_to_be_present_in_element(elemento, texto))

    def encontrarClassePrincipal(self, classe):
        locator = (By.XPATH, "//*[contains(@class," + classe + ")]")
        self.espera.until(presence_of_element_located(locator))

    def trocarAba(self, url):
        # janelaOriginal  = self.driver.current_window_handle()
        time.sleep(2)
        id_janelas = self.driver.window_handles
        for janela in id_janelas:
            self.driver.switch_to.window(janela)
            if url in self.capturar_url():
                break

    def elementoAtivo(self, locator):
        return self.obterElemento(locator).is_enabled()

    def inserirDado(self, locator, dado):
        elemento = self.espera.until(presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
        elemento.send_keys(dado)

    def apertarTAB(self, locator):
        self.clicar(locator)
        self.obterElemento(locator).send_keys(Keys.TAB)

    def scrolAteElemento(self, locator):
        elemento = self.obterElemento(locator)
        ActionChains(self.driver).scroll_to_element(elemento).perform()