from datetime import datetime,timedelta
import logging

CURRENT_DATE_DETAILS=datetime.today()

class Date_And_Time():
    def __init__(self):
        try:
            self.date_yesterday=self.get_yesterday_date()
            self.date_day_before_yesterday=self.get_day_before_yesterday_date()
        except Exception as err:
            logging.error(f"An error occured: {err}")
    
    def get_yesterday_date(self):
        try:
            yesterday_date_details=CURRENT_DATE_DETAILS-timedelta(days=1)
            date_yesterday=yesterday_date_details.date().strftime("%Y-%m-%d")
            return date_yesterday
        except Exception as err:
            logging.error(f"Error in get_yesterday_date: {err}")
    
    def get_day_before_yesterday_date(self):
        try:
            day_before_yesterday_date_details=CURRENT_DATE_DETAILS-timedelta(days=2)
            date_day_before_yesterday=day_before_yesterday_date_details.date().strftime("%Y-%m-%d")
            return date_day_before_yesterday
        except Exception as err:
            logging.error(f"Error in get_day_before_yesterday: {err}")