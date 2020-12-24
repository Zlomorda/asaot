
from asaotdata import data
from bs4 import BeautifulSoup
import requests


url = "http://yit.maya-tour.co.il/yit-pass/Drop_Report.aspx?client_code=2660&coordinator_code=2669"
destination = 'יבנה'

destination_list = []
for i in range(1, 21):
    data["__EVENTARGUMENT"] = 'Page$' + str(i)

    x = requests.post(url, data=data)
    if x.status_code == 500:
        break
    else:
        soup = BeautifulSoup(x.content, 'lxml')

        table = soup.find("table")
        for tr in table.findChildren('tr'):
            x = tr.get_text()
            if x.find(destination) != -1 and x.find(destination) < 60:
                all_td = tr.findAll("td")
                for temp in all_td:
                    if 'A' in temp.text or 'B' in temp.text or 'C' in temp.text or ':' in temp.text:
                        destination_list.append(temp.text)
                    else:
                        destination_list.append(temp.text[::-1])

for i in range(0, len(destination_list)):
    print(destination_list[i])