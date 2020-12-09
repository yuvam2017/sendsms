
import requests
url = "https://www.fast2sms.com/dev/bulk"
message = "YOUR MESSAGE HERE"
number = "+911234567890" # Enter your Registered mobile number on the FAST2SMS It gives you 50rupees as credit on registering
payload = f"sender_id=FastWP&message={message}&language=english&route=p&numbers={number[3:]}"
headers = {
'authorization': "YOUR API HERE",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text) # TO check whether your code run correctly
