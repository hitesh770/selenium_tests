from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from pages.europe_markets import EuropeMarketsPage
from pages.markets_indexes_page import MarketIndexPage
from pages.search_page import SearchPage
import pytest


def test_home_page_drawer_menu(driver):
    home_page = HomePage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    home_page.navigate_to_home_page_menu()
    home_page.validate_home_page_menu()


@pytest.mark.smoke
def test_home_page_menu_settings(driver):
    home_page = HomePage(driver)
    settings_page = SettingsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    home_page.navigate_to_home_page_menu()
    home_page.validate_home_page_menu()
    settings_page.navigate_to_settings_page()
    settings_page.validate_settings_page()
    settings_page.navigate_to_settings_page_hidden_sources()
    settings_page.validate_hidden_sources_error_text()


# Negative case
def test_dax_market_for_europe_markets(driver):
    home_page = HomePage(driver)
    europe_markets_page = EuropeMarketsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    europe_markets_page.navigate_to_europe_markets_page()
    assert 0 == len(europe_markets_page.validate_dow_jones_not_exists())


def test_all_listed_index_for_europe_markets(driver):
    home_page = HomePage(driver)
    compare_europe_markets_page_ob = EuropeMarketsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    compare_europe_markets_page_ob.navigate_to_europe_markets_page()
    compare_europe_markets_page_ob.validate_all_europe_markets_exists()


def test_europe_listed_dax_markets(driver):
    home_page = HomePage(driver)
    compare_europe_markets_page_ob = EuropeMarketsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    compare_europe_markets_page_ob.navigate_to_europe_markets_page()
    compare_europe_markets_page_ob.navigate_to_europe_dax_markets()
    compare_europe_markets_page_ob.validate_dax_performance_index_option()


@pytest.mark.smoke
def test_europe_listed_dax_markets_follow_features(driver):
    home_page = HomePage(driver)
    compare_europe_markets_page_ob = EuropeMarketsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    compare_europe_markets_page_ob.navigate_to_europe_markets_page()
    compare_europe_markets_page_ob.navigate_to_europe_dax_markets()
    compare_europe_markets_page_ob.validate_dax_performance_index_option()
    compare_europe_markets_page_ob.navigate_to_follow_features_page()
    compare_europe_markets_page_ob.validate_follow_features_page()


def test_various_markets_indexes(driver):
    home_page = HomePage(driver)
    markets_index_page = MarketIndexPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    markets_index_page.navigate_to_market_indexes_page()
    markets_index_page.validate_markets_index_page()


@pytest.mark.smoke
def test_markets_indexes_share_features(driver):
    home_page = HomePage(driver)
    markets_index_page = MarketIndexPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    markets_index_page.navigate_to_market_indexes_page()
    markets_index_page.validate_markets_index_page()
    markets_index_page.navigate_to_market_indexes_share_page()
    markets_index_page.validate_markets_index_share_page()


def test_search_markets_features(driver):
    home_page = HomePage(driver)
    search_page_ob = SearchPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    search_page_ob.enter_search_result('dollar industries')
    assert 0 < len(search_page_ob.count_search_result())


# negative test
def test_search_markets_no_matches_result_features(driver):
    home_page = HomePage(driver)
    search_page_ob = SearchPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    search_page_ob.enter_search_result('hitesh test')
    assert 1 == len(search_page_ob.count_no_search_result())


def test_privacy_page_menu(driver):
    home_page = HomePage(driver)
    settings_page = SettingsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    settings_page.navigate_to_privacy_policy_page()
    settings_page.validate_privacy_policy_page()


def test_terms_of_service_page(driver):
    home_page = HomePage(driver)
    settings_page = SettingsPage(driver)
    home_page.validate_home_page_loading()
    assert "Finance" in home_page.check_home_page_title()
    settings_page.navigate_to_terms_of_policy_page()
    settings_page.validate_terms_of_policy_page()
