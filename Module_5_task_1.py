import faker

from faker import Faker
from faker.providers import company
from faker.providers import person
from faker.providers import internet
from faker.providers import job

fake = Faker()
fake_f_name = fake.first_name()
fake_l_name = fake.last_name()
fake_company = fake.company()
fake_job = fake.job()
fake_email = fake.ascii_company_email()
fake_phone = fake.phone_number()
fake_bphone = fake.phone_number()

class BaseContact:
    _registry = []
    def __init__(self, first_name, last_name, email, phone):
        self._registry.append(self)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

        self._label_length = 0

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def __repr__(self):
        return str((self.first_name, self.last_name, self.email))

    def contact(self):
        return print("Wybieram nr {} i dzwonię do {}, {}.".format(self.phone, self.first_name, self.last_name))

    @property
    def label_length(self):
        return self._label_length
    
    @label_length.setter
    def label_length(self,value):
        value = len(self.first_name)+len(self.last_name)+1
        self._label_length = value

Aamos = BaseContact("Aamos","Suutari-Jääskö","asj.huawei.com","+48 123456789")
Robin = BaseContact("Robin","Strand","rstrand.bp.com","+48 234567890")
Ulpiano = BaseContact("Ulpiano","Murillo Olivas","UlpianoMurilloOlivas@armyspy.com","+48 345678901")
Matthew = BaseContact("Matthew","Heerschop","MatthewHeerschop@teleworm.us","+48 456789012")
Delit = BaseContact("Delit","Labonté","DelitLabonte@armyspy.com","+48 567890123")
NewOC = BaseContact(fake_f_name, fake_l_name, fake_email, fake_phone)


people = [Aamos, Robin, Ulpiano, Matthew, Delit, NewOC]   
by_first_name = sorted(people, key=lambda person: person.first_name)
by_last_name = sorted(people, key=lambda person: person.last_name)
by_email = sorted(people, key=lambda person: person.email)

for p in BaseContact._registry:
    person_dict = vars(p)
    print(person_dict)


print(by_first_name)
print(by_last_name)
print(by_email)

class BusinessContact(BaseContact):
    def __init__(self, company, job_title, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.company_phone = company_phone

    def bcontact(self):
        return print("Wybieram nr {} i dzwonię do {}, {}, {} w {}.".format(self.company_phone, self.first_name, self.last_name, self.job_title, self.company))

Aamos = BusinessContact("Huawei","Accountant","+48 134526708","Aamos","Suutari-Jääskö","asj.huawei.com","+48 123456789")
Robin = BusinessContact("BP","HR Partner","+48 249753980","Robin","Strand","rstrand.bp.com","+48 234567890")
Ulpiano = BusinessContact("Pioneer Chicken","Title abstractor","+48729659550","Ulpiano","Murillo Olivas","UlpianoMurilloOlivas@armyspy.com","+48 345678901")
Matthew = BusinessContact("K's Merchandise","EMT","+4871036541","Matthew","Heerschop","MatthewHeerschop@teleworm.us","+48 456789012")
Delit = BusinessContact("Solid Future","Certified pest control applicator","+48736990457","Delit","Labonté","DelitLabonte@armyspy.com","+48 567890123")
NewBC = BusinessContact(fake_company, fake_job, fake_bphone,fake_f_name, fake_l_name, fake_email, fake_phone)

card_type = input("Wybierz typ wizytówki: 1 - biznesowa, 2 - zwykła.")

def create_contacts(card_type):
    if card_type == 1:
        return print(NewBC)
    elif card_type == 2:
        return print(NewOC)

card = create_contacts(card_type)
print(card)

