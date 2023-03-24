from WebConfig.webconfig import Test_data
from Tests.test_base import BaseTest
import pytest
from Pages.Flight_SearchPage import FlightSearch
from time import sleep

class Test_flight_search(BaseTest):
    def test_inputbox(self):
        fpage = FlightSearch(self.driver)
        fpage.do_enter_cities(Test_data.ORIGIN_CITY,Test_data.DEST_CITY)
        sleep(2)
        fpage.do_enter_date()
        sleep(2)
        fpage.do_check()
        sleep(2)
        