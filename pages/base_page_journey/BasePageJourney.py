from framework.elements.Button import Button
from framework.elements.InputDropdown import InputDropdown
from framework.elements.Label import Label
from framework.elements.Link import Link
from framework.elements.List import List
from framework.elements.Slider import Slider
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class BasePageJourney(BasePage):
    page_name = "Base Page Journey"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "base_page_journey_locator")

    lbl_price_home = Label(locator_reader, "price_selected_home")

    lnk_chosen_home = Link(locator_reader, "lnk_chosen_home")

    sld_tenure_slider = Slider(locator_reader, "tenure_slider")

    btn_filter_icon_search_results = Button(locator_reader, 'btn_filter_icon_search_results')

    lst_of_results_quick_search = List(locator_reader, "list_of_results_price")

    drd_area_result_page = InputDropdown(locator_reader, "area_dropdown_result_page",
                                         "area_arrow_dropdown_result_page", "area_input_dropdown_result_page")

    def is_price_present(self, price):  # just for example
        """
        Method to check that home from with specific price from previous page are displayed on current page
        """
        return self.lbl_price_home.format(price).is_present()

    def is_chosen_home_present(self):  # just for example
        """
        Chosen home is present
        :return: bool: chosen home is present
        """
        return self.lnk_chosen_home.is_present()

    def is_chbx_desabled_or_enabled(self, checkbox_locator):  # just for example
        """
        Return "true" if checkbox is selected or is deselected
        """
        checkbox_locator.wait_until_location_stable()
        return checkbox_locator.is_present()

    def get_count_of_home_results(self):  # just for example
        """
        Get count of homes by search results
        :return: int: count of homes
        """
        self.lst_of_results_quick_search.wait_until_location_stable()
        return self.lst_of_results_quick_search.get_elements_count()
