from framework.elements.Button import Button
from framework.elements.Label import Label
from framework.pages.BasePage import BasePage
from framework.utils.LocatorReader import LocatorReader


class ThirdPage(BasePage):
    page_name = "Third Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "third_page_locator")

    btn_name = Button(locator_reader, "btn_name")

    def __init__(self):
        super(ThirdPage, self).__init__(self.page_element)

    def click_name_btn(self):  # just for example
        """
        Click to "Name" button
        """
        self.btn_name.click()
