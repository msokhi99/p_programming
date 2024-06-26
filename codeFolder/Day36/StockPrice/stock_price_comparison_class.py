import logging

class Compare_Stock():
    def __init__(self,yesterday_stock_price,day_before_yesterday_stock_price):
        try:
            self.yesterday_stock_price=yesterday_stock_price
            self.day_before_yesterday_stock_price=day_before_yesterday_stock_price
            self.stock_difference=self.get_stock_difference()
            self.abs_stock_difference=self.get_abs_stock_difference()
            self.stock_percentage=self.get_stock_percentage()
        except Exception as err:
            logging.error(f"An error occured: {err}")
            
    def get_stock_difference(self):
        try:
            s_difference=self.yesterday_stock_price-self.day_before_yesterday_stock_price
            return s_difference
        except Exception as err:
            logging.error(f"Error in get_stock_difference: {err}")
    
    def get_abs_stock_difference(self):
        try:
            s_difference=self.get_stock_difference()
            abs_s_difference=abs(s_difference)
            return abs_s_difference
        except Exception as err:
            logging.error(f"Error in get_abs_stock_difference: {err}")
    
    def get_stock_percentage(self):
        try:
            abs_stock_difference=self.get_abs_stock_difference()
            s_percentage=(abs_stock_difference/self.day_before_yesterday_stock_price)*100
            return s_percentage
        except Exception as err:
            logging.error(f"Error in get_stock_percentage: {err}")