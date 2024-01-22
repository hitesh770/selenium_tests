from selenium.webdriver.common.by import By
from pages.common import CommonOps


class SettingsPage(CommonOps):
    SETTINGS_OPT = (By.XPATH, "//div[text()='Settings']")
    SETTINGS_LBL = (By.XPATH, "//span[contains(text(),'Settings')]")
    HIDDEN_SOURCES = (By.XPATH, "//div[contains(text(),'Hidden sources')]")
    MANAGE_BTN = (By.XPATH, "//a[@aria-label='Manage hidden sources']")
    HIDDEN_SOURCES_ERROR_LBL = (By.XPATH, "//*[text()='You have not hidden any news sources']")
    PRIVACY_LIN = (By.XPATH, "//a[text()='Privacy']")
    PRIVACY_LBL = (By.XPATH, "//span[text()='Privacy Policy']")
    TERMS_LIN = (By.XPATH, "//a[text()='Terms']")
    TERMS_LBL = (By.XPATH, "(//span[text()='Privacy & Terms'])[1]")

    def navigate_to_settings_page(self):
        self.action_click(self.find(self.SETTINGS_OPT)).perform()

    def validate_settings_page(self):
        self.wait_for(self.SETTINGS_LBL)
        self.wait_for(self.HIDDEN_SOURCES)
        self.wait_for(self.MANAGE_BTN)

    def navigate_to_settings_page_hidden_sources(self):
        self.action_click(self.find(self.MANAGE_BTN)).perform()

    def validate_hidden_sources_error_text(self):
        self.wait_for(self.HIDDEN_SOURCES_ERROR_LBL)

    def navigate_to_privacy_policy_page(self):
        self.wait_for(self.PRIVACY_LIN).click()

    def validate_privacy_policy_page(self):
        self.wait_for(self.PRIVACY_LBL)

    def navigate_to_terms_of_policy_page(self):
        self.wait_for(self.TERMS_LIN).click()

    def validate_terms_of_policy_page(self):
        self.wait_for(self.TERMS_LBL)
