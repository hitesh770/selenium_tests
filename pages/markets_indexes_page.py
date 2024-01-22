from selenium.webdriver.common.by import By
from pages.common import CommonOps


class MarketIndexPage(CommonOps):
    MARKET_INDEXES_LABEL_LINK = (By.XPATH, "//span/span[text()='Market indexes']")
    EXPLORE_MARKET_TRENDS_LBL = (By.XPATH, "//div[text()='Explore market trends']")
    AMERICAS_LBL = (By.XPATH, "//span[text()='Americas']")
    SHARE_BTN = (By.XPATH, "//button//span[text()='Share']")
    SHARE_LBL = (By.XPATH, "//div[text()='Share']")

    def navigate_to_market_indexes_page(self):
        self.action_click(self.find(self.MARKET_INDEXES_LABEL_LINK)).perform()
        self.wait_for(self.EXPLORE_MARKET_TRENDS_LBL)

    def validate_markets_index_page(self):
        self.wait_for(self.AMERICAS_LBL)

    def navigate_to_market_indexes_share_page(self):
        self.wait_for(self.SHARE_BTN)
        self.action_click(self.find(self.SHARE_BTN)).perform()

    def validate_markets_index_share_page(self):
        try:
            self.wait_for(self.SHARE_LBL)
        except Exception:
            self.action_click(self.find(self.SHARE_BTN)).perform()
        finally:
            self.wait_for(self.SHARE_LBL)
