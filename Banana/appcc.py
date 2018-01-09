import application as a

class Credit(a.Application):
    def __init__(self, title, name, nric, dob, phone_no, address, occupation, noc, email, local, employed,
                 sup, relationship, title1, name1, nric1, dob1, phone_no1, address1, occupation1, noc1, email1, local1):
        a.Application.__init__(self, title, name, nric, dob, phone_no, address, occupation, noc, email, local, employed)
        self.__supplementary = sup
        self.__relationship = relationship
        self.__title1 = title1
        self.__name1 = name1
        self.__nric1 = nric1
        self.__date_of_birth1 = dob1
        self.__phone_no1 = phone_no1
        self.__address1 = address1
        self.__occupation1 = occupation1
        self.__nameoncard1 = noc1
        self.__email1 = email1
        self.__local1 = local1


    def get_supplementary(self):
        return self.__supplementary

    def get_title1(self):
        return self.__title1

    def get_name1(self):
        return self.__name1

    def get_nric1(self):
        return self.__nric1

    def get_date_of_birth1(self):
        return self.__date_of_birth1

    def get_phone_no1(self):
        return self.__phone_no1

    def get_address1(self):
        return self.__address1

    def get_occupation1(self):
        return  self.__occupation1

    def get_nameoncard1(self):
        return self.__nameoncard1

    def get_email1(self):
        return self.__email1

    def get_local1(self):
        return self.__local1

    def get_relationship(self):
        return self.__relationship




    def set_title1(self, title1):
        self.__title1 = title1

    def set_name1(self, name1):
        self.__name1 = name1

    def set_nric1(self, nric1):
        self.__nric1 = nric1

    def set_date_of_birth1(self, dob1):
        self.__date_of_birth1 = dob1

    def set_phone_no1(self, phone_no1):
        self.__phone_no1 = phone_no1

    def set_address1(self, address1):
        self.__address1 = address1

    def set_occupation1(self, occupation1):
        self.__occupation1 = occupation1

    def set_nameoncard1(self, noc1):
        self.__nameoncard1 = noc1

    def set_email1(self, email1):
        self.__email1 = email1

    def set_local1(self, local1):
        self.__local1 = local1

    def set_supplementary(self, sup):
        self.__supplementary = sup

    def set_relationship(self, relationship):
        self.__relationship = relationship
