import pytest
from pages.home import HomePage
from pages.marketing import MarketingPage


# @pytest.mark.skip
class TestMaketing():
    """营销页面"""

    def test_Send_ticket_center(self,login_web):
        driver = login_web
        self.home_page = HomePage(driver)
        self.home_page.marketing()

        self.marketing_page = MarketingPage(driver)

        self.marketing_page.click_tt()


