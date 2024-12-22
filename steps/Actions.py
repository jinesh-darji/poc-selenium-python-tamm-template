import random

from framework.browser.Browser import Browser
from framework.utils.EnvReader import EnvReader

fake_user = "fake-login?userNumber={}".format(random.randint(14 ** 15, 14 ** 16 - 1))

# Class where need to describe common actions in your journey

class Actions:

    @staticmethod
    def login_local_not_verified_user():
        Browser.set_url(EnvReader().get_env_config()['start_url'] + fake_user)  # just for example

    @staticmethod
    def close_log_in_pop_up(page_locator):
        """
        Close log in pop up
        :param page_locator: page locator where need to use this method
        """
        page_locator.click_close_login_popup_btn()  # just for example
