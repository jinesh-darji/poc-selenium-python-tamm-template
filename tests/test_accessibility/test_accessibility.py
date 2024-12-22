import pytest
import allure

from journey_template.pages.HomePage import HomePage
from journey_template.pages.second_page.SecondPage import SecondPage


class TestPropertyDetailsSavedProperties:
    """Name of test: ID of test"""

    @pytest.mark.accessibility
    def test_accessibility(self):
        with allure.step("Describe this step"):
            home_page = HomePage()
            home_page.click_select_home_btn()

        with allure.step("Describe this step"):
            second_page = SecondPage()
            second_page.get_count_of_home_results()
