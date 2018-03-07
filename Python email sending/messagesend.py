import urllib
import urllib3
import sendotp

authkey="194576AO2xKl76y5a659d18"
mobile="8114465928"
message="Test python message"
sender="611332"

route="default"
details={
    'authkey':authkey,
    'mobiles':mobile,
    'message':message,
    'sender':sender,
    'route':route
}
url="http://api.msg91.com/api/sendhttp.php"
postdata=urllib.parse.urlencode(details)
print(postdata)
http=urllib3.PoolManager()
print(http)
req=http.request('GET',url+"?"+postdata)
print(req.read())
res=http.urlopen('GET',url+"?"+postdata)
print(res.read())

otpobj=sendotp('authkey','my message is {{otp}} keep otp with you.')
print(otpobj.send(918114465928,'msgind',3245))



