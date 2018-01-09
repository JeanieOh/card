import application as a

class Debit(a.Application):
    def __init__(self, title, name, nric, dob, phone_no, address, occupation, noc, email, local, employed):
        a.Application.__init__(self, title, name, nric, dob, phone_no, address, occupation, noc, email, local, employed)
