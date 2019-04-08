import hashlib
import requests
import getpass

# Declaring a typed-object for api response
class PwnItem:
    def __init__(self, hashed, count):
        self.Hashed = hashed
        self.Count = count


def GetDataFromWebService(myParam):
    r = requests.get("https://api.pwnedpasswords.com/range/" + myParam)
    # Creating the PwnItem object from response
    result = [PwnItem(x.split(":")[0], x.split(":")[1])
              for x in r.text.split("\r\n")]
    return result


myPass = getpass.getpass('Password:')
hashedPass = hashlib.sha1(myPass.encode("utf-8")).hexdigest()

first5CharsOfHashed = hashedPass[:5]
restOfHashed = hashedPass[5:]

result = GetDataFromWebService(first5CharsOfHashed)
output = "You are safe... FOR NOW!"
for item in result:
    if(restOfHashed.upper() in item.Hashed):
        output = "You are PWNED "+item.Count+" TIMES!"

print(output)
