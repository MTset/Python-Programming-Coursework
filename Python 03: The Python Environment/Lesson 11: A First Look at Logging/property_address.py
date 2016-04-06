"""
property_address.py: tests property addresses for valid (US) syntax.
"""
import re
from urllib.request import urlopen
from urllib.parse import urlencode
# import the logging module
import logging
import inspect
LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
MODULE_NAME = __name__

DEFAULT_LOG_LEVEL = "error" # default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    msg = 10 * "*" + " " + __name__ + " RUN START " + 10 * "*" + "\n" + 26 * " " +\
     "CALLING MODULE: " + inspect.stack()[1][1]
    logging.info(msg)
    
class ValidationError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg
        
class StateError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg
        
class ZipCodeError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg
        
class Address(object):
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = sanitize_whitespace(name)
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.street_address = street_address
        msg = "Address instantiated"
        logging.info(msg)
        
    @property        
    def name(self):
        """
        A basic Name check - assumes Python 3 or above - thus unicode by default
        """
        regex = re.compile(r"^[^\W\d_]+([ \-'‧][^\W\d_]+)*?\Z")
        if regex.match(self._name) is None:
            self.caller = inspect.stack()[1][3]
            msg = "'{0}' is an invalid name".format(self._name)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            raise ValidationError("001", msg)
        logging.info("OK")
        return self._name

    @property    
    def city(self):
        """
        Get already sanitized and checked city
        """
        self.caller = inspect.stack()[1][3]
        logging.info("OK")
        return self._city
    
    @city.setter
    def city(self, city):
        """
        A basic City Name check - assumes Python 3 or above - thus unicode by default
        """
        self._city = sanitize_whitespace(city)
        regex = re.compile(r"^([a-zA-Z\u0080-\u024F]{1}[a-zA-Z\u0080-\u024F\. |\-| |']*[a-zA-Z\u0080-\u024F\.']{1})$")
        if regex.match(self._city) is None:
            msg = "'{0}' is an invalid City Name ".format(self._city)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            raise ValidationError("002", msg)

    @property    
    def state(self):
        """
        Get already sanitized and checked US State
        """
        self.caller = inspect.stack()[1][3]
        logging.info("OK")
        return self._state
    
    @state.setter
    def state(self, state):
        """
        US State abbreviation
        """
        self._state = sanitize_whitespace(state)
        states = ['IA', 'KS', 'UT', 'VA', 'NC', 'NE', 'SD', 'AL', 'ID', 'FM',
                  'DE', 'AK', 'CT', 'PR', 'NM', 'MS', 'PW', 'CO', 'NJ', 'FL',
                  'MN', 'VI', 'NV', 'AZ', 'WI', 'ND', 'PA', 'OK', 'KY', 'RI',
                  'NH', 'MO', 'ME', 'VT', 'GA', 'GU', 'AS', 'NY', 'CA', 'HI',
                  'IL', 'TN', 'MA', 'OH', 'MD', 'MI', 'WY', 'WA', 'OR', 'MH',
                  'SC', 'IN', 'LA', 'MP', 'DC', 'MT', 'AR', 'WV', 'TX']
        regex = re.compile("|".join(states), re.IGNORECASE)
        if regex.match(self._state) is None:
            msg = "'{0}' is an invalid State Code".format(self._state)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            raise StateError("003", msg)

    @property    
    def zip_code(self):
        """
        Get already sanitized and checked ZIP code
        """
        self.caller = inspect.stack()[1][3]
        logging.info("OK")
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, zip_code):
        """
        US Postasl code validation allowing both the five-digit and nine-digit
        (called ZIP+4) formats.
        """
        self._zip_code = sanitize_whitespace(zip_code)
        regex = re.compile(r"^[0-9]{5}(?:-[0-9]{4})?$")
        if regex.match(self._zip_code) is None:
            msg = "'{0}' is an invalid ZIP code".format(self._zip_code)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            raise ZipCodeError("004", msg)
    
    @property    
    def street_address(self):
        """
        Get already sanitized and checked Street Address
        """
        self.caller = inspect.stack()[1][3]
        logging.info("OK")
        return self._street_address
    
    @street_address.setter
    def street_address(self, street_address):
        self._street_address = sanitize_whitespace(street_address)
        if (address_exists(r"{0}, {1}, {2} {3}".format(self._street_address, 
            self._city, self._state, self._zip_code))) is None:
            msg = "'{0}, {1}, {2} {3}' is an invalid Street Address".format(
                self._street_address, self._city, self._state, self._zip_code)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            raise ValidationError("005", msg)
    
def sanitize_whitespace(str):
    """
    sanitize string to the extent of stripping leading and trailing whitespace
    and replace all internal runs of whitespace by a single space.
    """
    return re.sub(r"[ ]+", " ", str.strip())

def address_exists(addr):
    """
    a very basic check if such an (exact) address exists anywhere as per google maps. 
    """
    urlParams = {'address': (addr)}  
    url = 'http://maps.google.com/maps/api/geocode/json?' + urlencode(urlParams)
    response = urlopen(url)
    responseBody = response.read()
    if str(responseBody).find("ROOFTOP") != -1 and str(responseBody).find(addr) != -1:
        return True
    
def stop_logging():
    msg = 10 * "*" + " " + __name__ + " RUN END " + 10 * "*"
    logging.info(msg)
    
    
    