import sqlite3
import table
conn = sqlite3.connect("final.db")
c = conn.cursor()
try:
    table.creating_all()
except Exception as e:
    "OperationalError"
    pass

c.execute("""
    INSERT INTO PATIENT
    VALUES
    (9090212, "Tim Martin", 756943432, "Gangnam Station Tower SM 707-Room",25,"Male", True,2021-10-07, 7007,null,null),
    (9090101,"Bruce Lee", 234124514, "China Town", 34,"Male",True, 2022-12-05,7007,null,null ),
    (9090214, "Tim Martin", 756943432, "Gangnam Station Tower SM 707-Room",25,"Male", True,2021-10-07, 7007,null,null),
    (9090193, "Jack Wilson", 434327569, "City Hall BM 402-Room",21,"Male", True,2019-11-04, 7002,null,null),
    (9090283, "Mary Smith", 327543469, "Wangsimni MS 102-Room",22,"Female", False,2020-01-04, 7011,null,null),
    (9090454, "Paul Jane", 543463279, "Gyeyang KS 212-Room",24,"Male", False,2022-01-04, 7874,null,null),
    (9090984, "William James", 163254379, "Unyeon JL 217-Room",24,"Male", False,2019-07-11, 7874,null,null),
    (9090711, "Sophia Choe", 279543463, "Jeondae Everland FR 122-Room",22,"Female", False,2016-11-24, 6994,null,null),
    (9090272, "Isabella Ava", 632754349, "Moran Amsa LS 219-Room",24,"Female", True,2018-09-14, 7871,null,null),
    (9090763, "Rebecca Olivia ", 279543463, "Sinseol-dong BS 385-Room",23,"Female", False,2012-03-12, 5374,null,null),
    (9090874, "Oliver Lucas", 463254379, "Sinnae Eungnam HJ 256-Room",24,"Male", False,2022-09-17, 8734,null,null),
    (9090484, "Noah Richardson", 632754349, "Uncheon LK 316-Room",27,"Male", False,2022-02-05, 7724,null,null)
""")
c.execute("""
    INSERT INTO DEPARTMENT
    VALUES 
    (1,"Cardiology", "Bulding-A 4th floor", 2003-10-12,null,null,null,null,null),
    (2,"Orthopaedics", "Building-C 2nd floor", 2003-10-09,null,null,null,null,null),
    (3,"Neurology", "Building-B 1st floor", 2003-07-16,null,null,null,null,null),
    (4,"Gynaecology", "Building-A 3rd floor", 2003-03-11,null,null,null,null,null),
    (5,"Dermatology", "Building-E 5th floor", 2003-12-23,null,null,null,null,null),
    (6,"Ophthalmology", "Building-F 1st floor", 2003-04-17,null,null,null,null,null),
    (7,"Oncology", "Building-E 4th floor", 2003-12-05,null,null,null,null,null),
    (8,"Pediatrics", "Building-E Basement-2", 2003-12-05,null,null,null,null,null),
    (9,"Emergency Medicine", "Building-H 1st floor", 2003-12-05,null,null,null,null,null)
    """)
c.execute("""
    INSERT INTO DOCTOR
    VALUES
    (11101,"Antonio De Paullo",944662121,1,"Bulding-A 404-room", True,2019-04-2,7007,2021-11-11,7004,null,null),
    (11102," Jamas Khang",073519776,2,"Bulding-C 204-room", True,2007-08-22,7004,2029-12-13,7004,null,null),
    (11103," Roberto Martis",564663321,3,"Bulding-B 123-room", True,2002-04-12,7007,2008-01-15,7004,null,null),
    (11104," Sarah Smith",987661131,4,"Bulding-A 304-room", True,2011-04-12,7004,2018-01-21,7007,null,null),
    (11105," Kim Navang",987664521,5,"Bulding-E 516-room", True,2009-09-08,7007,2019-01-21,7004,null,null),
    (11106," Minsu Kim",276662322,6,"Bulding-F 111-room", True,2009-11-02,7004,2017-11-21,7004,null,null),
    (11107," Son Hyong Minh",884666743,7,"Bulding-E 424-room", True,2016-04-12,7007,2020-11-21,7007,null,null),
    (11108," Kim Sang Hwa",044663161,8,"Bulding-E B2", False,2015-04-21,7004,2020-10-21,7004,null,null),
    (11109," Jane Park",874666711,9,"Bulding-H 120-room", True,2010-03-17,7004,2018-01-30,7007,null,null)
    """)
c.execute("""
    INSERT INTO NURSE
    VALUES
    (22201,"Anh Kim",40314432,1,2012-11-23,7007,null,null,null,null),    
    (22202,"Sandra Kang",88902334,2,2013-10-18,7004,null,null,null,null),
    (22203," Aisha Umar",56902554,3,2016-04-28,7004,null,null,null,null),
    (22204," Matilda Wick",66900990,4,2017-06-22,7007,null,null,null,null),
    (22205," Sebo David",98222244,5,2018-03-19,7004,null,null,null,null),
    (22206," Fazilet Akhmat",32902366,6,2019-05-25,7007,null,null,null,null),
    (22207," Li Mei",32901277,7,2011-05-15,7007,null,null,null,null),
    (22208," Sandy Jim",32902332,8,2012-09-05,7007,null,null,null,null),
    (22209," Samta Jonas",32982375,9,2016-07-22,7004,null,null,null,null),
    (22210," Hanu Kanib",32102736,10,2018-05-20,7004,null,null,null,null),
    (22211," Sally Jim",32909378,11,2016-01-29,7007,null,null,null,null),
    (22212," Zara Sancho",82903477,12,2019-10-25,7004,null,null,null,null),
    (22213," Shani Nur",85902246,13,2018-08-20,7004,null,null,null,null),
    (22214," Khang Jay",52902216,14,2015-05-15,7007,null,null,null,null),
    (22215," Hana Lei",90902786,15,2016-10-29,7007,null,null,null,null),
    (22216," Nam Park",09902316,16,2015-11-05,7004,null,null,null,null),
    (22217," Kyong Bok Lee",42902186,17,2016-11-14,7007,null,null,null,null),
    (22218," Sania John",87932726,18,2017-02-27,7004,null,null,null,null)
    """)
c.execute("""
    INSERT INTO OUT_APPOINTMENT
    VALUES 
    (8085101,1,2022-12-13,'13:5:00',9090212,"Medical Check-up",12,7,12-7, False, 2022-12-06,7004,null,null,null,null,null)
    """) 

c.execute("""
    INSERT INTO APP_PRESCRIPTION
    VALUES
    (430070,8085101,11101,"Acnutrol", "Once a day", False, 2022-12-17, 7007, null, null)
""")
c.execute("""
    INSERT INTO 
    INPATIENT_STAY
    VALUES
    (900901,"Out Patient",8085102,null,9090101,11103,22203,1101,2022-12-25,2022-01-22,3,1,2022-12-15,11103,null,null,null,null)
    """)
c.execute(""" INSERT INTO PROCEDURE
    VALUES
    ("AB-12","Healing","Three times injection and physiotherapy",11108,2019-11-11,7001,null,null,2020-01-04,7004)
    """) 

c.execute(""" INSERT INTO MEDICINE 
    VALUES
    (111012345, "Aspirin", "Antiinfflammatory drugs", "Once a day" ,200,2022-11-30, 6001, null, null,null,null),
    (111012346, "Metformin", "Diabetes drugs"," Once a day before lunch" ,13000, 2022-11-30, 6001, null, null,null,null ),
    (111012347, "Hydrocodone", "Painkiller", "Twice a day",5400, 2022-11-30,6001,null, null,null,null  ),
    (111012348, "Ketotifen", "Antihistamines","After each meal" ,2600, 2022-11-30, 6001, null, null,null,null),
    (111012349, "Losartan", "High blood pressure relief"," Before sleeping " ,12200, 2022-11-30, 6001, null, null,null,null )
    """)

c.execute(""" INSERT INTO BILL
    VALUES 
    ("B1234", 111012345, 101, "AB12", 13000, 3000, 16000,2022-11-11,7007,null,null),
    ("B1235", 111012346, 102, "AB13", 13400, -4400, 9000, 2022-04-19 ,7007, null,null)
    """)
#Change int to string

print("Patient")
pa = c.execute("SELECT * FROM PATIENT")
for i in pa:
    print(i)
doc = c.execute("SELECT * FROM  DOCTOR")
print("Doctor")
for i in doc:
    print(i)

nu = c.execute("SELECT * FROM NURSE")
print("Nurse")
for i in nu: 
    print(i)

out_ap = c.execute("SELECT * FROM OUT_APPOINTMENT")

print("Out Patient Appointment")

for i in out_ap: 
    print(i)

app = c.execute("SELECT *FROM APP_PRESCRIPTION")

print("APP PRESCRIPTION")

for i in app:
    print(i)

dep = c.execute("SELECT *FROM DEPARTMENT")

for i in dep:
    print(i)

inpt_stay = c.execute("SELECT *FROM INPATIENT_STAY")

print("INPATIENT STAY")
for i in inpt_stay:
    print(i)


pro = c.execute("SELECT * FROM PROCEDURE")

print("PROCEDURE")

for i in pro:
    print(i)


med = c.execute("SELECT * FROM MEDICINE")

for i in  med:
    print(i)

b_ill = c.execute("SELECT * FROM BILL") 
for i in b_ill:
    print(i)


conn.close()




#Procudure to Char(40)