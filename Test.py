class Person:
    

    def __str__(self):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job_title = job_title
        self.email = email
        self.name_len = len(self.first_name)+1+len(self.last_name)
    

Aamos = Person("Aamos","Suutari-Jääskö","Huawei","Accountant","asj.huawei.com")
Robin = Person("Robin","Strand","BP","Sr Data Engineer","rstrand.bp.com")
Ulpiano = Person("Ulpiano","Murillo Olivas","Pioneer Chicken","Title abstractor","UlpianoMurilloOlivas@armyspy.com")
Matthew = Person("Matthew","Heerschop","K's Merchandise","EMT","MatthewHeerschop@teleworm.us")
Delit = Person("Delit","Labonté","Solid Future","Certified pest control applicator","DelitLabonte@armyspy.com")

print(name_len())
 