import requests
from datetime import datetime
#----------------------------------------------------------------

class holiday:
    def __init__(self,url):
        self.response=requests.get(url)


    def search(self,mounth,day):
        if self.response.status_code==200:
            for holiday in self.response.json():
                api_date=datetime.strptime(holiday["date"],'%Y-%m-%d')
                api_mounth=api_date.month
                api_day=api_date.day
                if api_mounth==mounth and api_day==day:
                    return holiday["name"]
            return "Not Found...!"
           


