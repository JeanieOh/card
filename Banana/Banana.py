from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

app = Flask(__name__)





@app.route('/')
def featured():
    return render_template('featured.html')


@app.route('/debitcard')
def home():
    return render_template('DebitCard.html')


@app.route('/ocbcdc')
def ocbcdc():
    return render_template('ocbcdc.html')


@app.route('/uobdc')
def uobdc():
    return render_template('uobdc.html')

@app.route('/populardbsdc')
def populardbsdc():
    return render_template('populardbsdc.html')

@app.route('/shoppingdbsdc')
def shoppingdbsdc():
    return render_template('shoppingdbsdc.html')














class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)


class PublicationForm(Form):
    bank = RadioField('Bank', [validators.DataRequired()], choices=[('dbs', 'DBS'), ('ocbc', 'OCBC'), ('uob', 'UOB')],
                      default='dbs')
    card = RadioField('Debit Card or Credit Card',[validators.DataRequired()], choices= [('dc','Debit Card'),('cc','Credit Card')], default= 'dc')
    dbsdc = SelectField('Choice of Card', [RequiredIf(card='dc')],
                        choices=[('', 'Select'), ('visadebit', 'DBS Visa Debit Card'),
                                 ('passion', 'Passion POSB Debit Card'), ('safra', 'SAFRA DBS Debit Card'),
                                 ('unionpay', 'DBS UnionPay Platinum Debit Card'),
                                 ('taka', 'DBS Takashimaya Debit Card'),
                                 ('nussu', 'DBS NUSSU Debit Card')], default='')

    ocbcdc = SelectField('Choice of Card', [RequiredIf(card='dc')],
                         choices=[('', 'Select'), ('frank', 'FRANK Debit Card'), ('yes', 'OCBC YES! Debit Card'),
                                  ('plus', 'OCBC Plus! Visa Debit Card'), ('ntuc', 'NTUC Plus! Visa Debit Card')],
                         default='')

    uobdc = SelectField('Choice of Card', [RequiredIf(card='dc')],
                        choices=[('', 'Select'), ('uobd', 'UOB Debit Card'), ('delight', 'UOB Delight Debit Card'),
                                 ('direct', 'UOB Direct Visa Debit Card'),
                                 ('kris', 'KrisFlyer UOB Account'), ('lady', "UOB Lady's Debit Card")], default='')

    dbscc = SelectField('Choice of Card', [RequiredIf(card='cc')],
                        choices=[('', 'Select'), ('fresh', 'DBS Live Fresh Card'), ('every', 'POSB Everyday Card'),
                                 ('esso', 'DBS Esso Card'),
                                 ('black', 'DBS Black Card'), ('safra', 'SAFRA DBS Card'),
                                 ('takas', 'DBS Takashimaya Cards'),
                                 ('nusalumni', 'DBS NUS Alumni & DBS NUSS Cards'), ('woman', "DBS Woman's Card"),
                                 ('altitude', 'DBS Altitude Card'),
                                 ('student', 'DBS Live Fresh Student Card')], default='')
    ocbccc = SelectField('Choice of Card', [RequiredIf(card='cc')],
                         choices=[('', 'Select'), ('titanium', 'OCBC Titanium Rewards Credit Card'),
                                  ('365', 'OCBC 365 Credit Card'), ('cashflo', 'OCBC Cashflo Credit Card'),
                                  ('frankcc', 'FRANK Credit Card'), ('voyage', 'OCBC Voyage Card'),
                                  ('pluscc', 'OCBC Plus! Visa Credit Card'),
                                  ('ntuccc', 'NTUC Plus! Visa Credit Card'),
                                  ('robin', 'OCBC Robinsons Group Credit Card'), ('art', 'OCBC Arts Credit Card'),
                                  ('bestdenki', 'OCBC BEST Denki Credit Card'),
                                  ('platinum', 'OCBC Platinum Credit Card')], default='')
    uobcc = SelectField('Choice of Card', [RequiredIf(card='cc')],
                        choices=[('', 'Select'), ('prvi', 'UOB PRVI Miles Card'),
                                 ('signature', 'UOB Visa Signature Card'), ('yolo', 'UOB YOLO'),
                                 ('onecard', 'UOB One Card'),
                                 ('delightcc', 'UOB Delight Credit Card'), ('jcb', 'UOB JCB Card'),
                                 ('unioncc', 'UOB UnionPay Card'), ('singtel', 'Singet-UOB Card'),
                                 ('metro', 'Metro-UOB Card'),
                                 ('ladycc', "UOB Lady's Card"), ('platinumvisa', 'UOB Preferred Platinum Visa Card'),
                                 ('profess', 'UOB Professionals Platinum Card'),
                                 ('infinite', 'UOB Visa Infinite Card')], default='')

    title = SelectField('Title',[validators.DataRequired()], choices = [('','Select'),('mr','MR'),('mrs','MRS'),('ms','MS'),('mdm','MDM')], default = '')
    name = StringField('Name',[validators.Length(min=1, max=150), validators.DataRequired()])
    nameoncard = StringField('Name to appear on Card (max 19 characters)', [validators.Length(min=1, max=19), validators.DataRequired()])
    local = SelectField('Are you a Singaporean',[validators.DataRequired()], choices= [('', 'Select'), ('n','No'),('y','Yes')], default= '')
    nric = StringField('NRIC',[validators.Length(min=1, max=9), validators.DataRequired()])
    date_of_birth = StringField('Date Of Birth (DDMMYYYY)',[validators.Length(min=1, max=8), validators.DataRequired()])
    phone_no = StringField('Phone Number', [validators.Length(min=1, max=8), validators.DataRequired()])
    self_employed = SelectField('Self Employed',[validators.DataRequired()], choices=[('', 'Select'), ('n','No'),('y','Yes')], default= '')
    occupation = StringField('Occupation', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email Address',[validators.Length(min=1, max=150), validators.DataRequired()])
    address = TextAreaField('Address',[validators.DataRequired()])


    supplementary = SelectField('Any Supplementary card?',[validators.DataRequired()], choices=[('','Select'), ('n','No'),('y','Yes')], default= '')
    relationship = SelectField('Relationship',[validators.DataRequired()], choices=[('','Select'),('p','Parent'),('s','Spouse'),('c','Child'),('o','Others')], default= '')
    title1 = SelectField('Title',[validators.DataRequired()], choices=[('', 'Select'), ('mr', 'MR'), ('mrs', 'MRS'), ('ms', 'MS'), ('mdm', 'MDM')],
                        default='')
    name1 = StringField('Name',[validators.Length(min=1, max=150), validators.DataRequired()])
    nameoncard1 = StringField('Name to appear on Card (max 19 characters)',[validators.Length(min=1, max=19), validators.DataRequired()])
    local1 = SelectField('Are you a Singaporean',[validators.DataRequired()], choices=[('', 'Select'), ('n', 'No'), ('y', 'Yes')], default='')
    nric1 = StringField('NRIC',[validators.Length(min=1, max=9), validators.DataRequired()])
    date_of_birth1 = StringField('Date Of Birth (DDMMYYYY)',[validators.Length(min=1, max=8), validators.DataRequired()])
    phone_no1 = StringField('Phone Number',[validators.Length(min=1, max=8), validators.DataRequired()])
    self_employed1 = SelectField('Self Employed',[validators.DataRequired()], choices=[('', 'Select'), ('n', 'No'), ('y', 'Yes')], default='')
    occupation1 = StringField('Occupation',[validators.Length(min=1, max=150), validators.DataRequired()])
    email1 = StringField('Email Address',[validators.Length(min=1, max=150), validators.DataRequired()])
    address1 = TextAreaField('Address',[validators.DataRequired()])








@app.route('/application', methods=['GET', 'POST'])
def new():
    form = PublicationForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('create_application.html', form=form)

    return render_template('create_application.html', form=form)


""""""""""








    


class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)

"""""




















if __name__ == '__main__':
    app.run()


