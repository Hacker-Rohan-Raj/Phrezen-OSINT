import phonenumbers
from phonenumbers import geocoder

ch_number = phonenumbers.parse("+911234567890", "CH")
num = geocoder.description_for_number(ch_number, "en")
print(num)
