from framework.elements.Label import Label
from framework.utils.LocatorReader import LocatorReader
from journey_template.pages.base_page_journey.BasePageJourney import BasePageJourney


class SecondPage(BasePageJourney):
    page_name = "Second Page"
    locator_reader = LocatorReader(page_name)
    page_element = Label(locator_reader, "second_page_locator")

    def __init__(self):
        super(SecondPage, self).__init__(self.page_element)