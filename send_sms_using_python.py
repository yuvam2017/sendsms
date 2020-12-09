
import requests
url = "https://www.fast2sms.com/dev/bulk"
message = " Welcome to delhi"
number = "+919450524879"
payload = f"sender_id=FastWP&message={message}&language=english&route=p&numbers={number[3:]}"
headers = {
'authorization': "BqUAVMIgdW4oZs7zkNfPbwcv3HQ6EexCS9FmX1DulTyLiJGr5KotVqHTSc01Onh4kGaURwfuB5Qg893l",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
