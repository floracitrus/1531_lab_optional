class Course:

    def __init__(self, name, abstract, date, venue, attendees, trainer):
        self._name = name
        self._abstract = abstract
        self._date = date
        self._venue = venue
        self._attendees = attendees
        self._trainer = trainer

    def add_attendee(self, attendee):
        if attendee not in self._attendees:
            self._attendees.append(attendee)

    def drop_attendee(self, attendee):
        self._attendees.remove(attendee)

    def change_trainer(self, trainer):
        self._trainer = trainer

    def __str__(self):
        string = ""
        string += ("Course Name: %s \n" \
               "Abstract: %s \n" \
               "Open Date: %s \n" \
               "Venue: %s \n"%(self._name, self._abstract, self._date, self._venue))
        string += (str(self._trainer))
        for student in self._attendees:
            string += str(student)
        return string

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self._name == other._name:
                return True
        return False


class ConferenceCentre:

    def __init__(self):
        self._courses = []

    def add_course(self, course):
        if course not in self._courses:
            self._courses.append(course)

    def delete_course(self, course):
        self._courses.remove(course)

    def __str__(self):
        string = ""
        for course in self._courses:
            string += (str(course) + "\n")
        return string


class Attendee:

    def __init__(self, name, address, phone, id):
        self._name = name
        self._address = address
        self._phone = phone
        self._id = id

    def change_address(self, address):
        self._address = address

    def change_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return ("Attendee Name: %s \n" \
               "Address: %s \n" \
               "Phone: %s \n"%(self._name,
                              self._address,
                              self._phone))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self._id == other._id:
                return True
        return False


class Trainer:
    def __init__(self, name, address, phone, id, field):
        self._name = name
        self._address = address
        self._phone = phone
        self._id = id
        self._field = field

    def change_address(self, address):
        self._address = address

    def change_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return ("Trainer Name: %s \n" \
                "Address: %s \n" \
                "Phone: %s \n" \
                "Field: %s \n"% (self._name,
                                  self._address,
                                  self._phone,
                                  self._field))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self._id == other._id:
                return True
        return False


system = ConferenceCentre()
comp1531 = Course("COMP1531", "Software Engineering Fundmental", "01/01/2017", "CSE", [], None)
jack = Attendee("Jack", "jack@unsw.edu.au", "+61 100100", "z100")
tom = Attendee("Tom", "tom@unsw.edu.au", "+61 100101", "z101")
aarthi = Trainer("Aarthi", "aarthi@unsw.edu.au", "+61 000001", "z001", "Software Engineering")
system.add_course(comp1531)
comp1531.add_attendee(jack)
comp1531.add_attendee(tom)
comp1531.change_trainer(aarthi)
print(system)

