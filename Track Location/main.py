import phonenumbers
import opencage 

from myphone import number

from phonenumbers import geocoder 


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode


key = 'd010cd969df64c48a2a0b0560601da1d'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results) 

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
 
print(lat,lng)