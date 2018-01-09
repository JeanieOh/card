import datetime


class Application:

    def __init__(self, title, name, nric, dob, phone_no, address, occupation, noc, email, local, employed):
        self.__title = title
        self.__name = name
        self.__nric = nric
        self.__date_of_birth = dob
        self.__phone_no = phone_no
        self.__address = address
        self.__occupation = occupation
        self.__nameoncard = noc
        self.__email = email
        self.__local = local
        self.__self_employed = employed

        currentdatetime = datetime.datetime.now()
        create_date = str(currentdatetime.day) + "-" + str(currentdatetime.month) + "-" + str(
            currentdatetime.year)  # DD-MM-YYYY format
        self.__create_date = create_date


    def get_title(self):
        return self.__title

    def get_name(self):
        return self.__name

    def get_nric(self):
        return self.__nric

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_phone_no(self):
        return self.__phone_no

    def get_created_date(self):
        return self.__created_date

    def get_address(self):
        return self.__address

    def get_occupation(self):
        return  self.__occupation

    def get_nameoncard(self):
        return self.__nameoncard

    def get_email(self):
        return self.__email

    def get_local(self):
        return self.__local

    def get_self_employed(self):
        return self.__self_employed




    def set_title(self, title):
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def set_nric(self, nric):
        self.__nric = nric

    def set_date_of_birth(self, dob):
        self.__date_of_birth = dob

    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def set_created_date(self, create_date):
        self.__created_date = create_date

    def set_address(self, address):
        self.__address = address

    def set_occupation(self, occupation):
        self.__occupation = occupation

    def set_nameoncard(self, noc):
        self.__nameoncard = noc

    def set_email(self, email):
        self.__email = email

    def set_local(self, local):
        self.__local = local

    def set_self_employed(self, employed):
        self.__self_employed = employed
