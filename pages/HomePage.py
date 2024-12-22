from journey_template.pages.base_page_journey.BasePageJourney import BasePageJourney
from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from framework.elements.Button import Button


class HomePage(BasePageJourney):

    page_name = "Home Page"  # just for example
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "home_page_locator")
    btn_select_home = Button(locator_reader, "btn_select_home")
    btn_buy_home = Button(locator_reader, "btn_buy_home")
    btn_apply_for_ready_home_grant = Button(locator_reader, "btn_apply_for_ready_home_grant")
    btn_financing = Button(locator_reader, "btn_financing")
    btn_deed_transfer = Button(locator_reader, "btn_deed_transfer")
    btn_get_utilities = Button(locator_reader, "btn_get_utilities")
    btn_get_insurance = Button(locator_reader, "btn_get_insurance")
    btn_move_new_home = Button(locator_reader, "btn_move_new_home")

    def __init__(self):
        super(HomePage, self).__init__(self.page_element)

    def is_select_home_step_present(self):  # just for example
        """
        Return "true" if "Select home" step is present
        :return: bool: "Select home" step is existed
        """
        self.btn_select_home.wait_until_location_stable()
        return self.btn_select_home.is_present()

    def click_select_home_btn(self):  # just for example
        """
        Method clicks on "Select home" button
        """
        self.btn_select_home.wait_until_location_stable()
        self.scroll_to_element(self.btn_select_home)
        self.btn_select_home.click()

    def click_financing_btn(self):  # just for example
        """
        Method clicks on "financing" button
        """
        self.btn_financing.wait_until_location_stable()
        self.btn_financing.click()

    def click_deed_transfer_btn(self):  # just for example
        """
        Method clicks on "Deed Transfer" button
        """
        self.btn_deed_transfer.wait_until_location_stable()
        self.btn_deed_transfer.click()

    def click_get_utilities_btn(self):  # just for example
        """
        Method clicks on "Get Utilities" button
        """
        self.btn_get_utilities.wait_until_location_stable()
        self.btn_get_utilities.wait_for_is_present()
        self.btn_get_utilities.click()

    def click_get_insurance_btn(self):  # just for example
        """
        Method clicks on "Get Insurance" button
        """
        self.btn_get_insurance.wait_until_location_stable()
        self.btn_get_insurance.click()

    def click_move_new_home_btn(self):  # just for example
        """
        Method clicks on "Move to New Home" button
        """
        self.btn_move_new_home.wait_until_location_stable()
        self.btn_move_new_home.click()

    def click_buy_home_btn(self):  # just for example
        """
        Method clicks "Buy a new home" button
        """
        self.btn_buy_home.wait_until_location_stable()
        self.btn_buy_home.click()

    def click_apply_for_ready_nome_grant_btn(self):  # just for example
        """
        Method clicks "Apply for ready home grant" button
        """
        self.btn_apply_for_ready_home_grant.wait_until_location_stable()
        self.btn_apply_for_ready_home_grant.click()