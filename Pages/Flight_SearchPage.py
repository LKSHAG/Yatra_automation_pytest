from Pages.BasePage import BasePage
from WebConfig.webconfig import Test_data
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FlightSearch(BasePage):
    ONEWAY = (By.XPATH,"//a[@title='One Way']")
    ORIGIN = (By.XPATH,"//input[@id = 'BE_flight_origin_city']")
    DEST = (By.XPATH,"//input[@id = 'BE_flight_arrival_city']")
    DATE = (By.XPATH,"//input[@id='BE_flight_origin_date']")
    DATE_ID = (By.XPATH,"//td[@id='01/05/2023']")
    BOX = (By.XPATH,"//a[normalize-space()='Non Stop Flights']")
    SEARCH = (By.XPATH,"//input[@value = 'Search Flights']")

    def __init__(self, driver):
        super().__init__(driver)
        #Opening the URL
        self.driver.get(Test_data.BASE_URL)
    
    def do_enter_cities(self,origin_city,dest_city):

        self.do_click(self.ONEWAY)
        
        self.do_click(self.ORIGIN)

        self.do_send_keys(self.ORIGIN,origin_city)
        sleep(2)
        self.do_send_keys(self.ORIGIN,Keys.ENTER)
        sleep(2)
        self.do_click(self.DEST)

        self.do_send_keys(self.DEST,dest_city)
        sleep(2)
        self.do_send_keys(self.DEST,Keys.ENTER)
        sleep(2)
    def do_enter_date(self):

        self.do_click(self.DATE)

        self.do_click(self.DATE_ID)
        
    def do_check(self):

        self.do_click(self.BOX)
        
        self.do_click(self.SEARCH)
        
