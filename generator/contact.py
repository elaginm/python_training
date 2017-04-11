from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_day():
    return random.randint(1, 31)


def random_string_month():
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    return random.choice(month)


def random_string_year():
    return random.randint(0, 2030)


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", email="",
                    birthdayday="", birthdaymonth="-", birthdayyear="")] + [
            Contact(firstname=random_string("firstname", 10),
                    lastname=random_string("lastname", 10),
                    address=random_string("address", 20),
                    homephone=random_string("", 9),
                    mobilephone=random_string("", 9),
                    email=random_string("email@", 15),
                    birthdayday=str(random_string_day()),
                    birthdaymonth=random_string_month(),
                    birthdayyear=str(random_string_year()))
            for i in range(2)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
