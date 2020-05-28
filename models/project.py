from sys import maxsize

class Project:
    def __init__(self, name=None, status=None, visibility=None, description=None):
        self.name = name
        self.status = status
        self.visibility = visibility
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.name, self.status, self.visibility, self.description, self.id)


    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.description == other.description and self.visibility == other.visibility


    def __hash__(self):
        return hash((self.id, self.name))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def name(self):
        return str(self.name)
