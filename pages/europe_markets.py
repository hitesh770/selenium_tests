from selenium.webdriver.common.by import By
from pages.common import CommonOps


class EuropeMarketsPage(CommonOps):
    DOWJONES_LABEL = (By.XPATH, "//a//following::div[text()='Dow Jones'][1]")
    EUROPE_TAB = (By.XPATH, "//div[text()='Europe']")
    DAX_LBL = (By.XPATH, "//div[text()='DAX']")
    FTSE_LBL = (By.XPATH, "//div[text()='FTSE 100']")
    CAC_LBL = (By.XPATH, " //div[text()='CAC 40']")
    IBEX_LBL = (By.XPATH, "//div[text()='IBEX 35']")
    STOXX_LBL = (By.XPATH, "//div[text()='STOXX 50']")
    DAX_PERFORMANCE_INDEX_LBL = (By.XPATH, "//div[text()='DAX PERFORMANCE-INDEX']")
    FOLLOW_BTN = (By.XPATH, "//div[text()='Follow']")
    SIGNIN_BTN = (By.XPATH, "//span[text()='Sign in']")

    def validate_all_europe_markets_exists(self):
        self.wait_for(self.DAX_LBL)
        self.wait_for(self.FTSE_LBL)
        self.wait_for(self.CAC_LBL)
        self.wait_for(self.IBEX_LBL)
        self.wait_for(self.STOXX_LBL)

    def navigate_to_europe_markets_page(self):
        self.wait_for(self.EUROPE_TAB).click()
        self.wait_for(self.DAX_LBL)

    # negative case
    def validate_dow_jones_not_exists(self):
        return self.find_elements(self.DOWJONES_LABEL)

    def navigate_to_europe_dax_markets(self):
        self.wait_for(self.DAX_LBL).click()

    def validate_dax_performance_index_option(self):
        self.wait_for(self.DAX_PERFORMANCE_INDEX_LBL)

    def navigate_to_follow_features_page(self):
        self.wait_for(self.FOLLOW_BTN)
        self.action_click(self.find(self.FOLLOW_BTN)).perform()

    def validate_follow_features_page(self):
        self.wait_for(self.SIGNIN_BTN)
