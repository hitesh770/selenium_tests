from selenium.webdriver.common.by import By
from pages.common import CommonOps


class SearchPage(CommonOps):
    SEARCH_TXT = (By.XPATH, "(//input[@aria-label='Search for stocks, ETFs & more'])[2]")
    SEARCH_RESULT_OPT = (By.XPATH, "//span[text()='Dollar Industries']")
    SEARCH_RESULT_OPT2 = (By.XPATH, "//div[text()='No matches...']")
    ALL_LBL = (By.XPATH, "//div[text()='All']")
    SHARE_BTN = (By.XPATH, "//button/span[text()='Share']")
    SHARE_BTN = (By.XPATH, "//div[text()='Share']")

    def enter_search_result(self, search):
        self.wait_for(self.SEARCH_TXT).send_keys(search)

    def count_search_result(self):
        self.wait_for(self.ALL_LBL)
        return self.find_elements(self.SEARCH_RESULT_OPT)

    def count_no_search_result(self):
        self.wait_for(self.SEARCH_RESULT_OPT2)
        return self.find_elements(self.SEARCH_RESULT_OPT2)
