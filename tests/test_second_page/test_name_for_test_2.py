import pytest
import allure
from hamcrest import assert_that, not_

from journey_template.pages.second_page.SecondPage import SecondPage
from journey_template.steps.NavigateSteps import NavigateSteps


class TestName:
    """Name of test: ID or IDs for test"""

    @pytest.mark.smoke
    def test_name_for_test_2(self):

        with allure.step("Describe this step"):
            NavigateSteps.go_to_search_page()

        with allure.step("Describe this step"):
            second_page = SecondPage()
            second_page.get_count_of_home_results()

        with allure.step("Describe this step"):
            assert_that(not_(second_page.is_chosen_home_present()),  "Comment for assert")
            assert_that(second_page.is_chosen_home_present(), 'Comment for assert')

