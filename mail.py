"""
Run:
"""
from mailjet_rest import Client
import os
print("line 1")
my_secret = os.environ['MJ_APIKEY_PUBLIC']
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(my_secret, api_secret), version='v3.1')
data = {
  'Messages': [
				{
						"From": {
								"Email": "miarro70@yahoo.co.uk",
								"Name": "Me"
						},
						"To": [
								{
										"Email": "miarro70@yahoo.co.uk",
										"Name": "You"
								}
						],
						"Subject": "My first Mailjet Email!",
						"TextPart": "Greetings from Mailjet!",
						"HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
				}
		]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())