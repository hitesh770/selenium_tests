from selenium.webdriver.common.by import By
from pages.common import CommonOps


class HomePage(CommonOps):
    HOME_PAGE_TITLE = (By.XPATH, "//header//following::a[@title='Finance']")
    HOME_PAGE_MENU = (By.XPATH, "//header//following::div[@aria-label='Main menu']")
    PORTFOLIOS_LBL = (By.XPATH, "//div[text()='Portfolios']")
    WATCHLISTS_LBL = (By.XPATH, "//div[text()='Watchlists']")
    SETTINGS_LBL = (By.XPATH, "//div[text()='Settings']")

    def validate_home_page_loading(self):
        self.wait_for(self.HOME_PAGE_TITLE)

    def check_home_page_title(self):
        return self.wait_for(self.HOME_PAGE_TITLE).get_attribute('title')

    def navigate_to_home_page_menu(self):
        self.wait_for(self.HOME_PAGE_MENU).click()

    def validate_home_page_menu(self):
        self.wait_for(self.PORTFOLIOS_LBL)
        self.wait_for(self.WATCHLISTS_LBL)
        self.wait_for(self.SETTINGS_LBL)
