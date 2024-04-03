from typing import List
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuoetesPage:
    def __init__(self,browser):
        self.browser =  browser
        
    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        return [QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, locator)]
    @property
    def author_dropdown(self) -> Select:
        locator = QuotesPageLocators.AUTHOR_DROPDOWN
        elem = self.browser.find_element(By.CSS_SELECTOR, locator)
        return Select(elem)
    @property
    def tags_dropdown(self) -> Select:
        locator = QuotesPageLocators.TAG_DROPDOWN
        elem = self.browser.find_element(By.CSS_SELECTOR, locator )
        return Select(elem)
    @property
    def search_button(self):
        locator = QuotesPageLocators.SEARCH_BUTTON
        return self.browser.find_element(By.CSS_SELECTOR,locator)
    
    def select_author(self,author_name='Albert Einstein'):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_avaliable_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]
    

    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)
