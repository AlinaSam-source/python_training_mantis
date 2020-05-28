import random
import string
import os.path
import jsonpickle
import getopt
import sys
from models.project import Project

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ['number of groups', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = 'data/projects.json'


for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string_strings(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_status():
    statuses = ["10", "30", "50", "70"]
    return str(random.choice(statuses))


def random_visiability():
    visiability = ["10", "50"]
    return str(random.choice(visiability))


testdata = [
    Project(name=random_string_strings('name', 10), status=random_status(), visibility=random_visiability(), description=random_string_strings('description', 50))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))