"""
property_address.py: tests property addresses for valid (US) syntax.
"""
import os
import re
import logging
import inspect
import configparser
from optparse import OptionParser
parser = OptionParser()
cmdline = False

config = configparser.RawConfigParser()
config.read('property_address.cfg')

LOG_FILENAME = config.get('logfile', 'filename')
LOG_FORMAT = config.get('logfile', 'format')
DEFAULT_LOG_LEVEL = config.get('logfile', 'default_level')
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }
MODULE_NAME = __name__

NAME_VALIDATOR = config.get('validators', 'name')
CITY_VALIDATOR = config.get('validators', 'city')
STATES_VALIDATOR = config.get('validators', 'states')
ZIP_CODE_VALIDATOR = config.get('validators', 'zip_code')

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
    """
    Initialise attributes AND check them straight away
    """
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = sanitize_whitespace(name)
        self.name
        self.city = city
        self.city
        self.state = state
        self.state
        self.zip_code = zip_code
        self.zip_code
        self.street_address = street_address
        self.street_address
        msg = "Address instantiated"
        logging.info(msg)
        
    @property        
    def name(self):
        """
        A basic Name check - assumes Python 3 or above - thus unicode by default
        """
        regex = re.compile(NAME_VALIDATOR)
        if regex.match(self._name) is None:
            self.caller = inspect.stack()[1][3]
            msg = "'{0}' is an invalid name".format(self._name)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            global cmdline
            if cmdline:
                parser.error("option -n: '{0}'".format(msg))
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
        regex = re.compile(CITY_VALIDATOR)
        if regex.match(self._city) is None:
            if not hasattr(self, 'caller'):
                self.caller = inspect.stack()[1][3]
            msg = "'{0}' is an invalid City Name ".format(self._city)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            global cmdline
            if cmdline:
                parser.error("option -c: '{0}'".format(msg))
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
        regex = re.compile(STATES_VALIDATOR, re.IGNORECASE)
        if regex.match(self._state) is None:
            if not hasattr(self, 'caller'):
                self.caller = inspect.stack()[1][3]
            msg = "'{0}' is an invalid State Code".format(self._state)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            global cmdline
            if cmdline:
                parser.error("option -s: '{0}'".format(msg))
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
        US Postasl code validation allowing only the nine-digit (called ZIP+4) formats.
        """
        self._zip_code = sanitize_whitespace(zip_code)
        regex = re.compile(ZIP_CODE_VALIDATOR)
        if regex.match(self._zip_code) is None:
            if not hasattr(self, 'caller'):
                self.caller = inspect.stack()[1][3]
            msg = "'{0}' is an invalid ZIP code".format(self._zip_code)
            log_msg = "CALLER: {0} - {1}".format(self.caller, msg) 
            logging.error(log_msg)
            global cmdline
            if cmdline:
                parser.error("option -z: '{0}'".format(msg))
            raise ZipCodeError("004", msg)

def sanitize_whitespace(str):
    """
    sanitize string to the extent of stripping leading and trailing whitespace
    and replace all internal runs of whitespace by a single space.
    """
    return re.sub(r"[ ]+", " ", str.strip())
 
def stop_logging():
    msg = 10 * "*" + " " + __name__ + " RUN END " + 10 * "*"
    logging.info(msg)
    
def parse_cmdline():
    global cmdline
    cmdline = True
    parser.add_option('-l', '--level', dest="level", action="store",
                      help=config.get("option_help", "level"))
    
    parser.add_option('-n', '--name', dest="name", action="store",
                      help=config.get("option_help", "name"))
    
    parser.add_option('-a', '--address', dest="address", action="store",
                      help=config.get("option_help", "address"))
    
    parser.add_option('-c', '--city', dest="city", action="store",
                      help=config.get("option_help", "city"))
    
    parser.add_option('-s', '--state', dest="state", action="store",
                      help=config.get("option_help", "state"))
    
    parser.add_option('-z', '--zip_code', dest="zip_code", action="store",
                      help=config.get("option_help", "zip_code"))
    
    (options, args) = parser.parse_args()
    
    if set(options.__dict__.values()) == {None}:
        os.system("property_address.py -h")
        parser.error(config.get("option_help", "all_options"))

    # set log level to default if not provided or invalid    
    if options.level == "" or options.level is None or options.level not in LEVELS.keys():
        options.level = DEFAULT_LOG_LEVEL
        
    for option in options.__dict__:
        if options.__dict__[option] == "" or options.__dict__[option] is None:
            os.system("property_address.py -h")
            parser.error("Missing mandatory field: '{0}'.  See Help above.".format(option))
    
    return(options)
    
if __name__ == "__main__":
    options = parse_cmdline()
    start_logging(level=options.level)
    home = Address(name=options.name, street_address=options.address,
            city=options.city, state=options.state, zip_code=options.zip_code)
    stop_logging()

"""
Test command line:

property_address.py -l "info" -n  "Steve Holden" -a "5114 Ritchie Rd" -c "Bealeton"  -s "VAX" -z 22712-1234

"""
    
    