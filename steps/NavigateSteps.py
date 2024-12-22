import allure

from journey_template.pages.HomePage import HomePage

# Class where need to describe common navigation steps for your journey

class NavigateSteps:
    """Navigate methods"""

    @staticmethod
    def go_to_select_home_page():  # just for example
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_select_home_btn()

    @staticmethod
    def go_to_select_home_page_local_user():  # just for example
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_select_home_btn()

        with allure.step("Select 'Buy a home' button"):
            home_page.click_buy_home_btn()  # just for example

    @staticmethod
    def go_to_search_page():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()
            home_page.click_select_home_btn()

        with allure.step("Select 'Search' Button on 'Select Home' Page"):
            home_page = HomePage()  # just for example

        with allure.step("Check that 'Apply' Button is displayed on 'Search Home' page"):
            home_page = HomePage()  # just for example

    @staticmethod
    def go_to_home_grant_page_local_user():
        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()  # just for example

        with allure.step("Select 'Apply for ready home grant' button"):
            home_page = HomePage()  # just for example

    @staticmethod
    def go_to_search_results_page():
        with allure.step("Select 'Apartment' and 'Villa' checkboxes"):
            home_page = HomePage()  # just for example

        with allure.step("Select 'Apply' Button for going to Search results page"):
            home_page = HomePage()  # just for example

    @staticmethod
    def go_to_saved_properties_page():
        with allure.step("Go to Home Page"):
            home_page = HomePage()  # just for example

        with allure.step("Select 'Select Home' Page"):
            home_page = HomePage()  # just for example

        with allure.step("Select 'Saved properties' Button on 'Select Home' Page"):
            home_page = HomePage()  # just for example
