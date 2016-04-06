"""
try:
        import cStringIO as StringIO
except ImportError:
        import StringIO
"""
from urllib.request import urlopen
from urllib.parse import urlencode
import json
 
def decodeAddressToCoordinates( address ):
    urlParams = {
            'address': address
    }  
    url = 'http://maps.google.com/maps/api/geocode/json?' + urlencode( urlParams )
    response = urlopen( url )
    responseBody = response.read()
    print(str(responseBody).find("ROOFTOP"))
#    result = json.load(responseBody)
 
#    body = StringIO.StringIO( responseBody )
#    result = json.load( responseBody )
"""
        if 'status' not in result or result['status'] != 'OK':
                return None
        else:
                return {
                        'lat': result['results'][0]['geometry']['location']['lat'],
                        'lng': result['results'][0]['geometry']['location']['lng']
                }  
""" 
if __name__ == '__main__':
#        print(decodeAddressToCoordinates('Buenos Aires, Argentina'))
        print(decodeAddressToCoordinates('3 coromandel street'))