from tables import Sale,Clients,Houses,Rentedby,Rentalcontract,Ownedby,Soldto,Employee
from sqlalchemy import MetaData


#if you get an error here check the validity of the attributes values, foreign key constraint are checked automatically as well as CheckConstraint
def basic_tables(session):
   session.add_all([
    Clients(SSN='12844CBA3', Lastname='Amata',Firstname='Giovanni',Address='Via Giuseppe malibondi 56',City='Catania',State='Italy',Age=24,Phonenumber='+39 345884251'),
    Clients(SSN='124663124', Lastname='Xi',Firstname='Wuah',Address='Chan seng SU 12442',State='Hong Kong ',City='Hong Kong',Age=33,Phonenumber='+39 63421231'),
    Clients(SSN='123gsaf21', Lastname='Alberti',Firstname='Damiano',Address='Via Giuseppe Garibaldi 112',City='Hong Kong',State='Italy',Age=22,Phonenumber='+39 345884251'),
    Clients(SSN='5215dg612', Lastname='Diamanti',Firstname='Federico',City='Milano',State='Italy',Age=22,Phonenumber='+39 53252112'),
    Clients(SSN='636we242f', Lastname='Giordani',Firstname='Giovanni',Address='Via Giuseppe malibondi 56',City='Hong Kong',State='Italy',Age=29,Phonenumber='+39 345884251'),
    Clients(SSN='12465r345', Lastname='Franceschino',Firstname='Alessio',City='Napoli',State='Italy',Age=24,Phonenumber='+39 632421412'),
    Clients(SSN='237485443', Lastname='Ciccioli',Firstname='Giuseppe',City='Matera',State='Italy',Age=18,Phonenumber='+39 166452342'),
    Clients(SSN='192742111',Firstname='Leonardo',Lastname='Giobarti',City='Firenze',State='Italy',Phonenumber='+38 312312313',Age=24),
    Clients(SSN='122135211', Lastname='Misandro',Firstname='Alessio',City='Napoli',State='Italy',Age=29,Phonenumber='+39 125251123'),
    Clients(SSN='122131241', Lastname='Ciccioli',Firstname='Giuseppe',City='Bari',State='Italy',Age=18,Phonenumber='+39 1252324124'),
    Clients(SSN='124214123',Firstname='Giuseppe',Lastname='Cilibarti',City='Ancona',State='Italy',Phonenumber='+38 2155213112',Age=34),

    Employee(Idemployee='MAts1231',Lastname='Consuelo',Firstname='Ciccio',Phonenumber='+39 312321213'),
    Employee(Idemployee='21321412',Lastname='Consu',Firstname='Federico',Phonenumber='+39 214124124'),
    Employee(Idemployee='21421421',Lastname='Di Francesco',Firstname='Antonio',Phonenumber='+39 124124142'),
    Employee(Idemployee='52421421',Lastname='Alberti',Firstname='Giuseppe',Phonenumber='+39 214124124'),
    Employee(Idemployee='62355212',Lastname='Di Giovanni',Firstname='Harry',Phonenumber='+39 124214211'),
    Employee(Idemployee='56236322',Lastname='Anselmio',Firstname='Paolo',Phonenumber='+39 521525155'),
    Employee(Idemployee='73252342',Lastname='Anesi',Firstname='Paola',Phonenumber='+39 521562152'),

    Houses(Houseaddress='Via Gigi 12',Housecity='Catania',Sizesquaremeters=1200.00, Rooms=4),
    Houses(Houseaddress='XUAN JIN 11332',Housecity='Hong Kong',Sizesquaremeters=1400.00, Rooms=14),
    Houses(Houseaddress='Viale Europa 133',Housecity='Firenze',Sizesquaremeters=12300.00, Rooms=6),
    Houses(Houseaddress='Via Fumagalli 14',Housecity='Napoli',Sizesquaremeters=12050.00, Rooms=7),
    Houses(Houseaddress='Via Manzoni 12',Housecity='Genova',Sizesquaremeters=12040.00, Rooms=8),
    Houses(Houseaddress='Via Giglio 112',Housecity='Beverly Hills',Sizesquaremeters=12200.00, Rooms=9),
    Houses(Houseaddress='Via Pavinco 98',Housecity='Padova',Sizesquaremeters=19200.00, Rooms=10),
    Houses(Houseaddress='Via Gastro 25',Housecity='Pavia',Sizesquaremeters=1000.00, Rooms=24),
    Houses(Houseaddress='Via Giulii 12',Housecity='Bergamo',Sizesquaremeters=3200.00, Rooms=34),
    Houses(Houseaddress='Via Veneto 12',Housecity='Monza',Sizesquaremeters=2200.00, Rooms=44),
    Houses(Houseaddress='Via Ambolari 12',Housecity='Brescia',Sizesquaremeters=6200.00, Rooms=54),

    Sale(Idsalecontract='12522145',Houseaddress='Via Gigi 12', Housecity='Catania',Date='2007/03/12',Cost=1200.00,Idemployee='MAts1231'),
    Sale(Idsalecontract='21235555',Houseaddress='XUAN JIN 11332', Housecity='Hong Kong',Date='2007/03/12',Cost=1200.00,Idemployee='MAts1231'),
    Sale(Idsalecontract='21421424',Houseaddress='XUAN JIN 11332', Housecity='Hong Kong',Date='2003/03/12',Cost=1120.00,Idemployee='21321412'),
    Sale(Idsalecontract='21421214',Houseaddress='Viale Europa 133', Housecity='Firenze',Date='2010/03/12',Cost=15500.00,Idemployee='21321412'),
    Sale(Idsalecontract='21421415',Houseaddress='Via Manzoni 12', Housecity='Genova',Date='2012/03/12',Cost=1120.00,Idemployee='21421421'),
    Sale(Idsalecontract='25322155',Houseaddress='Via Ambolari 12', Housecity='Brescia',Date='2011/03/12',Cost=5400.00,Idemployee='52421421'),
    Sale(Idsalecontract='52363225',Houseaddress='Via Veneto 12', Housecity='Monza',Date='2011/03/12',Cost=6200.00,Idemployee='52421421'),
    Sale(Idsalecontract='62324125',Houseaddress='Via Giulii 12', Housecity='Bergamo',Date='2012/03/12',Cost=2200.00,Idemployee='62355212'),
    Sale(Idsalecontract='62321455',Houseaddress='Via Giulii 12', Housecity='Bergamo',Date='2009/03/21',Cost=31200.00,Idemployee='56236322'),
    Sale(Idsalecontract='52163255',Houseaddress='Via Giulii 12', Housecity='Bergamo',Date='2007/03/12',Cost=200.00,Idemployee='73252342'),

    Rentalcontract(Idrentalcontract='1s512ca',Houseaddress='Via Giulii 12',Housecity='Bergamo',Startdate='2007/12/12',Annualcost=4000,Idemployee='MAts1231',Enddate='2008/12/12'),
    Rentalcontract(Idrentalcontract='q42124',Houseaddress='Via Giulii 12',Housecity='Bergamo',Startdate='2007/12/12',Annualcost=4000,Idemployee='21321412',Enddate='2008/12/12'),
    Rentalcontract(Idrentalcontract='2152151',Houseaddress='Via Veneto 12',Housecity='Monza',Startdate='2007/12/12',Annualcost=4500,Idemployee='21321412',Enddate='2008/12/12'),
    Rentalcontract(Idrentalcontract='215asf12',Houseaddress='Via Ambolari 12',Housecity='Brescia',Startdate='2006/12/12',Annualcost=5000,Idemployee='62355212',Enddate='2007/12/12'),
    Rentalcontract(Idrentalcontract='215af213',Houseaddress='Via Manzoni 12',Housecity='Genova',Startdate='2007/12/12',Annualcost=3000,Idemployee='73252342',Enddate='2008/12/12'),
    Rentalcontract(Idrentalcontract='215fs123',Houseaddress='Via Giulii 12',Housecity='Bergamo',Startdate='2007/12/12',Annualcost=2000,Idemployee='52421421'),


])

def auxiliary_tables_population(engine):
   conn = engine.connect()
   conn.execute(Ownedby.insert(),[
      {'Houseaddress':'Via Gigi 12','Housecity':'Catania','ClientSSN':'5215dg612'},
      {'Houseaddress':'Via Gigi 12','Housecity':'Catania','ClientSSN':'123gsaf21'},
      {'Houseaddress':'Via Veneto 12','Housecity':'Monza','ClientSSN':'123gsaf21'},
      {'Houseaddress':'Via Ambolari 12','Housecity':'Brescia','ClientSSN':'5215dg612'},
      {'Houseaddress':'Via Ambolari 12','Housecity':'Brescia','ClientSSN':'192742111'},
      {'Houseaddress':'Via Ambolari 12','Housecity':'Brescia','ClientSSN':'122131241'},
      {'Houseaddress':'Via Manzoni 12','Housecity':'Genova','ClientSSN':'12465r345'},
      {'Houseaddress':'Via Giglio 112','Housecity':'Beverly Hills','ClientSSN':'192742111'},
      {'Houseaddress':'Via Gastro 25','Housecity':'Pavia','ClientSSN':'192742111'},
      {'Houseaddress':'Via Pavinco 98','Housecity':'Padova','ClientSSN':'122131241'},
      {'Houseaddress':'XUAN JIN 11332','Housecity':'Hong Kong','ClientSSN':'124214123'}
         ])

   conn.execute(Soldto.insert(),[
      {'Idsalecontract':'12522145','ClientSSN':'12844CBA3'},
      {'Idsalecontract':'52363225','ClientSSN':'5215dg612'},
      {'Idsalecontract':'25322155','ClientSSN':'122131241'},
      {'Idsalecontract':'62321455','ClientSSN':'12465r345'},
      {'Idsalecontract':'25322155','ClientSSN':'122135211'},
      {'Idsalecontract':'21421415','ClientSSN':'124663124'},
      {'Idsalecontract':'62324125','ClientSSN':'5215dg612'},
      {'Idsalecontract':'52363225','ClientSSN':'192742111'},
      {'Idsalecontract':'21421214','ClientSSN':'237485443'},
      {'Idsalecontract':'52363225','ClientSSN':'5215dg612'},
      {'Idsalecontract':'21235555','ClientSSN':'124663124'}
         ])

   conn.execute(Rentedby.insert(),[
      {'Idrentalcontract':'1s512ca','ClientSSN':'12844CBA3'},
      {'Idrentalcontract':'q42124','ClientSSN':'124663124'},
      {'Idrentalcontract':'2152151','ClientSSN':'5215dg612'},
      {'Idrentalcontract':'215asf12','ClientSSN':'636we242f'},
      {'Idrentalcontract':'215fs123','ClientSSN':'192742111'},
      {'Idrentalcontract':'215af213','ClientSSN':'122131241'},
      {'Idrentalcontract':'1s512ca','ClientSSN':'12465r345'},
      {'Idrentalcontract':'q42124','ClientSSN':'5215dg612'},
      {'Idrentalcontract':'215asf12','ClientSSN':'124663124'}
         ])
