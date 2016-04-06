"""
Settings module for the JOTD email suite
"""

import datetime

TBLDEF = """\
CREATE TABLE jotd (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgDate DATETIME,
     msgSender VARCHAR(128),
     msgReceiver VARCHAR(128),
     msgSubject VARCHAR(128),
     msgEmailID VARCHAR(128),
     msgText LONGTEXT
) ENGINE = MYISAM"""

STARTTIME = None
DAYCOUNT = None
DAYCOUNT_RANGE = range(1, 10) # used to double the DAYCOUNT for each test run
WEEKDAYS = range(5)
TEST_JOKE = """Daffy Duck on a dirty weekend calls reception and asks for a condom.\n
    The reception says "shall I put it on your bill?"\n
    Daffy replies...\n
    "Don't be thucking thtupid... I'd thufficate"!"""
    
SENDER = ["Roger Rabbit", "rogerrabbit@toontown.com"]
SUBJECT = "Joke Of The Day for "

RECIPIENTS = [
            ("Beaky Buzzard", "beakybuzzard@looneytunes.com"),
            ("Beans Cat", "beanscat@looneytunes.com"),
            ("Blacque Jacque Shellacque", "blacquejacqueshellacque@looneytunes.com"),
            ("Bobo", "bobo@looneytunes.com"),
            ("Bookworm", "bookworm@looneytunes.com"),
            ("Bosko", "bosko@looneytunes.com"),
            ("Buddy", "buddy@looneytunes.com"),
            ("Bugs Bunny", "bugsbunny@looneytunes.com"),
            ("Canyon Kiddies", "canyonkiddies@looneytunes.com"),
            ("Cecil Turtle", "cecilturtle@looneytunes.com"),
            ("Charlie Dog", "charliedog@looneytunes.com"),
            ("Chester", "chester@looneytunes.com"),
            ("Claude Cat", "claudecat@looneytunes.com"),
            ("Claude Hopper", "claudehopper@looneytunes.com"),
            ("Conrad Cat", "conradcat@looneytunes.com"),
            ("Cookie", "cookie@looneytunes.com"),
            ("Cool Cat", "coolcat@looneytunes.com"),
            ("Daffy Duck", "daffyduck@looneytunes.com"),
            ("Egghead Jr", "eggheadjr@looneytunes.com"),
            ("Egghead", "egghead@looneytunes.com"),
            ("Elmer Fudd", "elmerfudd@looneytunes.com"),
            ("Foghorn Leghorn", "foghornleghorn@looneytunes.com"),
            ("Foxy", "foxy@looneytunes.com"),
            ("Frisky Puppy", "friskypuppy@looneytunes.com"),
            ("Goofy Gophers", "goofygophers@looneytunes.com"),
            ("Goopy Geer", "goopygeer@looneytunes.com"),
            ("Gossamer", "gossamer@looneytunes.com"),
            ("Granny", "granny@looneytunes.com"),
            ("Grover Groundhog", "grovergroundhog@looneytunes.com"),
            ("Ham and Ex", "hamandex@looneytunes.com"),
            ("Henery Hawk", "heneryhawk@looneytunes.com"),
            ("Hippety Hopper", "hippetyhopper@looneytunes.com"),
            ("Honey", "honey@looneytunes.com"),
            ("Hubie and Bertie", "hubieandbertie@looneytunes.com"),
            ("Hugo the abominable showman", "hugotheabominableshowman@looneytunes.com"),
            ("Inki", "inki@looneytunes.com"),
            ("Little Blabbermouse", "littleblabbermouse@looneytunes.com"),
            ("Marc Antony", "marcantony@looneytunes.com"),
            ("Marvin Martian", "marvinmartian@looneytunes.com"),
            ("Merlin The Magic Mouse", "merlinthemagicmouse@looneytunes.com"),
            ("Michigan J Frog", "michiganjfrog@looneytunes.com"),
            ("Miss Prissy", "missprissy@looneytunes.com"),
            ("Mugsy", "mugsy@looneytunes.com"),
            ("Penelope", "penelope@looneytunes.com"),
            ("Pepe' Le Pew", "pepelepew@looneytunes.com"),
            ("Pete Puma", "petepuma@looneytunes.com"),
            ("Petunia Pig", "petuniapig@looneytunes.com"),
            ("Piggy", "piggy@looneytunes.com"),
            ("Porky Pig", "porkypig@looneytunes.com"),
            ("Ralph Phillips", "ralphphillips@looneytunes.com"),
            ("Ralph Wolf", "ralphwolf@looneytunes.com"),
            ("Rapid Rabbit", "rapidrabbit@looneytunes.com"),
            ("Road Runner", "roadrunner@looneytunes.com"),
            ("Rocky", "rocky@looneytunes.com"),
            ("Sam Sheepdog", "samsheepdog@looneytunes.com"),
            ("Sniffles", "sniffles@looneytunes.com"),
            ("Speedy Gonzales", "speedygonzales@looneytunes.com"),
            ("Spike", "spike@looneytunes.com"),
            ("Sylvester Junior", "sylvesterjunior@looneytunes.com"),
            ("Sylvester", "sylvester@looneytunes.com"),
            ("Tazmanian Devil", "tazmaniandevil@looneytunes.com"),
            ("The Champ", "thechamp@looneytunes.com"),
            ("The Crusher", "thecrusher@looneytunes.com"),
            ("The Gremlin", "thegremlin@looneytunes.com"),
            ("The Honey-Mousers", "thehoney-mousers@looneytunes.com"),
            ("Three Bears", "threebears@looneytunes.com"),
            ("Tweety Pie", "tweetypie@looneytunes.com"),
            ("Wacky Worm", "wackyworm@looneytunes.com"),
            ("Wile E Coyote", "wileecoyote@looneytunes.com"),
            ("Witch Hazel", "witchhazel@looneytunes.com"),
            ("Yosemite Sam", "yosemitesam@looneytunes.com"),
              ]

def business_week(starttime=None, daycount=None):
    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(days=1)
    # default start is tomorrow 07:00am local time
    tomorrow = tomorrow.replace(hour=7, minute=0, second=0)
    # if tomorrow is not a week day, start on Monday
    if tomorrow.weekday() in WEEKDAYS:
        to_week_end = 5 - tomorrow.weekday()
    else:
        tomorrow = tomorrow + datetime.timedelta(days = 7 - tomorrow.weekday())
        to_week_end = 5
        
    global STARTTIME
    if starttime:
        starttime = starttime.replace(hour=7, minute=0, second=0)
        while starttime.weekday() not in WEEKDAYS:
            starttime = starttime + datetime.timedelta(days=1)
        STARTTIME = starttime
    else:
        STARTTIME = tomorrow
        
    global DAYCOUNT    
    if daycount:
        DAYCOUNT = daycount
    else:
        DAYCOUNT = to_week_end
        
if __name__ == "__main__":
    business_week()
    print(STARTTIME, DAYCOUNT)