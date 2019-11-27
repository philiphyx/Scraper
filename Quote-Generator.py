# from twilio.rest import TwilioRestClient
import requests

# account_sid = " <Your sid> "
# auth_token = " <Your auth_token> "
#
# ourNumber = " <Your number> "
requestParams = {
    "method": "getQuote",
    "key": "457653",
    "format": "json",
    "lang": "en"
}
url = "http://api.forismatic.com/api/1.0/"

requestToApi = requests.post(url, params=requestParams)  # Requests the qoute from the API
json = requestToApi.json()  # This grabs the data from the response from API
print(json)
finishedQuote = json['quoteText'] + " -" + json['quoteAuthor']  # The finished quote!

print(finishedQuote)