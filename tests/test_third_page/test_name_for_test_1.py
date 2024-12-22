import pytest
import allure
from hamcrest import assert_that

from journey_template.pages.second_page.SecondPage import SecondPage
from journey_template.pages.third_page.ThirdPage import ThirdPage
from journey_template.steps.NavigateSteps import NavigateSteps

constant_1 = 4.0  # comment for constant 1
constant_2 = 10  # comment for constant 2
constant_3 = 100  # comment for constant 3


class TestName:
    """Name of test: ID for test"""

    @pytest.mark.regression
    def test_name_for_test_1(self):
        with allure.step("Describe this step"):
            NavigateSteps.go_to_search_page()

        with allure.step("Describe this step"):
            second_page = SecondPage()
            second_page.is_chosen_home_present()

        with allure.step("Describe this step"):
            third_page = ThirdPage()
            third_page.click_name_btn()

        with allure.step("Describe this step"):
            self.compare_mounthly_payment_and_data_from_PMT_formula(data_1[0], data_2[1])

        with allure.step("Describe this step"):
            self.compare_mounthly_payment_and_data_from_PMT_formula(data_1[0], data_2[1])

    def compare_mounthly_payment_and_data_from_PMT_formula(self, data_1, data_2):
        with allure.step("Describe this step"):
            assert_that(data_1 == data_2, "Comment for assert")
