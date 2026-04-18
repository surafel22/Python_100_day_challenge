import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STOCK_PARAMS = {
#     "apiKey": "36L4RDD6SHQ2SZR6",
#     "symbol": STOCK_NAME,
#     "function": "TIME_SERIES_DAILY",
#     # "news_apiKey": "b6b3edb0e7b94d30865417ad5b6c1ca4",
#}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get("https://www.alphavantage.co/query?"
                        "function=TIME_SERIES_DAILY&symbol=TSLA&apikey=S1FDZSEFVDOZ84K7")
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing = float(data_list[0]['4. close'])
print(yesterday_closing)
#TODO 2. - Get the day before yesterday's closing stock price
data_before = response.json()["Time Series (Daily)"]
data_before_list = [value for (key, value) in data.items()]
yesterday_before_closing = float(data_list[1]['4. close'])
print(yesterday_before_closing)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing - yesterday_before_closing)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / yesterday_closing) * 100
print(diff_percent)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 4:
    news = requests.get(
        "https://newsapi.org/v2/everything?q=tesla&from=2026-03-17&sortBy=publishedAt&apiKey=c87c55448b834f7ab0db607997493f62")
    news.raise_for_status()
    news_data = news.json()["articles"]
    three_articles = news_data[:3]
    print(news_data)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted = [f"Headline:{articles['title']}. \nBrief:{articles['description']} " for articles in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

