# import requests
#
# url = "https://api.themoviedb.org/3/movie/545611?language=en-US"
#
# response = requests.get(url, params={"api_key": "d2af927feb2f6c6622b595803f47c41f"})
# data = response.json()
# title = data['original_title']
# print(title)

from datetime import date

now = date.today()
formatted_date = now.strftime("%B %d, %Y")
print(formatted_date)
