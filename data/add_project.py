from model.project import Project
import random
import string

constant = Project(name="Lovely", status='development',
           inherit_global="checked", description='ttt')

def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])

# testdata = [
#     Project(name=name, status=status, inherit_global=inherit_global, description=description)
#     for name in ["Obligatory", random_string("name", 10)]
#     for status in ["", random.choice(['development', 'release', 'stable', 'obsolete'])]
#     for inherit_global in ['', random.choice(["checked", ''])]
#     for description in ['', random_string("description", 20)]
# ]

project = [Project(name=random_string("name", 10), status=random.choice(['development', 'release', 'stable', 'obsolete']),
           inherit_global=random.choice(["checked", '']), description=random_string("description", 20))
            for i in range(1)]