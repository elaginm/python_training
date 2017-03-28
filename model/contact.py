from sys import maxsize

class Contact:
    def __init__(self, Firstname=None, Lastname=None, Nickname=None, Title=None, Company=None, Address=None,
                 Homephone=None, Mobilephone=None, Email=None, Homepage=None, BirthdayDay="0", BirthdayMonth="-",
                 BirthdayYear=None, Address2=None, id=None):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Nickname = Nickname
        self.Title = Title
        self.Company = Company
        self.Address = Address
        self.Homephone = Homephone
        self.Mobilephone = Mobilephone
        self.Email = Email
        self.Homepage = Homepage
        self.BirthdayDay = BirthdayDay
        self.BirthdayMonth = BirthdayMonth
        self.BirthdayYear = BirthdayYear
        self.Address2 = Address2
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.Firstname, self.Lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.Firstname == other.Firstname and self.Lastname == other.Lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize