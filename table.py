import sqlite3

conn = sqlite3.connect("final.db")
c = conn.cursor()

def patient():
    b = c.execute("""
        CREATE TABLE PATIENT 
        ( 
        P_id INTEGER PRIMARY KEY,
        Name TEXT, 
        Contact INTEGER,
        Address TEXT,
        Age INTEGER,
        Gender TEXT,
        Insurance BOOLEAN, 
        CreatedOn DATETIME,
        CreatedBy INT,
        UpdatedOn DATETIME,
        UpdatedBy int)
        """)
    return b
def department():
    b = c.execute("""
        CREATE TABLE DEPARTMENT
        (
          `D_id` INT NOT NULL,
          `Name` TEXT,
          `Location` TEXT,
          `CreatedOn` DATETIME,
          `CreatedBy` INT,
          `UpdatedOn` DATETIME,
          `UpdatedBy` INT,
          `DeletedOn` DATETIME,
          `DeletedBy` INT,
          PRIMARY KEY(`D_id`))
        """)
    return b
def doctor():
    b = c.execute("""
    CREATE TABLE DOCTOR
    (
      `Doc_Id` INT NOT NULL,
      `Name` TEXT,
      `Contact` INT,
      `Department_id` INT NOT NULL,
      `Room` TEXT,
      `Availability` BOOLEAN NOT NULL,
      `CreatedOn` DATETIME,
      `CreatedBy` INT,
      `UpdatedOn` DATETIME,
      `UpdatedBy` INT,
      `DeletedOn` DATETIME ,
      `DeletedBy` INT,
       PRIMARY KEY(`Doc_Id`) 
    )
    """)
    return b
def nurse():
    b = c.execute("""
    CREATE TABLE NURSE
    (
      `N_id` INT NOT NULL,
      `Name` TEXT,
      `Contact` TEXT,
      `Department_id` INT NOT NULL,
      `CreatedOn` DATETIME,
      `CreatedBy` INT,
      `UpdatedOn` DATETIME,
      `UpdatedBy` INT,
      `DeletedOn` DATETIME,
      `DeletedBy` INT,
      PRIMARY KEY(`N_id`))
    """)
    return b
def out_appointment():
    b = c.execute("""
    CREATE TABLE OUT_APPOINTMENT
    (
        Out_app_id INTEGER PRIMARY KEY,
        P_id INT,
        Date_ DATE,
        Time_ TEXT,
        Dep_id INT,
        D_id INT,
        Purpose of visit TEXT,
        Price_full INTEGER,
        Price_discount INTEGER,
        Price_final INTEGER,
        Cancel BOOLEAN,
        CreatedOn DATETIME,
        CreatedBy INT,
        UpdatedOn DATETIME,
        UpdatedBy INT,
        DeletedOn DATETIME,
        DeletedBy INT
    )
    """)
    #        D_id   INTEGER NOT NULL, FOREIGN KEY (D_id) REFERENCES DOCTOR (D_id)
    #        ON UPDATE SET NULL
    #        ON DELETE SET NULL
    #P_id   INTEGER NOT NULL, FOREIGN KEY (P_id) REFERENCES PATIENT (P_id)
    return b
def app_prescrription():
    b = c.execute("""
        CREATE TABLE APP_PRESCRIPTION
        (
            App_p_d INT,
            Out_app_id INT,
            D_id INT,
            Medicine TEXT,
            Procedure TEXT,
            Inpatient_adm BOOLEAN,
            CreatedOn DATETIME,
            CreatedBy INT,
            UpdatedOn DATETIME,
            UpdatedBy INT
        )
        """)
    return b

def inpatient_stay():
    b = c.execute("""
        CREATE TABLE INPATIENT_STAY
        (
            S_id INT PRIMARY KEY,
            S_type TEXT,
            Appointment_id INT,
            Emerg_pr_id INT, 
            Patient_id INT,
            Doctor_id INT,
            Nurse_id INT,
            Room_id INT,
            S_start_day DATE,
            S_end_day DATE,
            Department_id INT,
            Inp_prescription_in_id INT,
            CreatedOn DATETIME,
            CreatedBy INT,
            UpdatedOn DATETIME,
            UpdatedBy INT,
            DeletedOn DATETIME,
            DeletedBy INT
        )
        """)
    return b
def emerg_prescription():
    b = c.execute("""
    CREATE TABLE EMERG_PRESCRIPTION(
      `Emerg_pr_id` INT NOT NULL,
      `Procedure_id` INT NOT NULL,
      `Emerg_doctor_id` INT NOT NULL,
      `Emerg_admission_id` INT NOT NULL,
      `Medicine` TEXT,
      `Inpatient_adm` BOOLEAN NOT NULL,
      `CreatedOn` DATETIME,
      `CreatedBy` INT,
      `UpdatedOn` DATETIME,
     `UpdatedBy` INT,
      PRIMARY KEY(`Emerg_pr_id`)
    )
        """)
    return b
def bill():
    b = c.execute("""
        CREATE TABLE BILL(
          `B_id`  CHAR(10) NOT NULL,
          `Medicine_id` INT,
          `Stay_room_id` INT,
          `Procedure_id` INT,
          `Procedure_price` INT,
          `Others_price` INT,
          `Total_price` INT,
          `CreatedOn` DATETIME,
          `CreatedBy` INT,
          `UpdatedOn` DATETIME,
          `UpdatedBy` INT,
          PRIMARY KEY(`B_id`));
        """)
    return b
def medicine():
    b = c.execute("""
        CREATE TABLE `MEDICINE`(
              `M_id` INT NOT NULL,
              `Name` TEXT,
              `Description` TEXT,
              `Manual` TEXT,
              `Price` INT,
              `CreatedOn` DATETIME,
              `CreatedBy` INT,
              `UpdatedOn` DATETIME,
              `UpdatedBy` INT,
              `DeletedOn` DATETIME,
              `DeletedBy` INT,
              PRIMARY KEY(`M_id`)
            );
        """)
    return b
def procedure():
    b = c.execute("""
        CREATE TABLE `PROCEDURE`(
              `Proc_id` CHAR(40) NOT NULL,
              `Name` TEXT,
              `Descritption` TEXT,
              `Nurse_id` INT,
              `CreatedOn` DATETIME,
              `CreatedBy` INT,
              `UpdatedOn` DATETIME,
              `UpdatedBy` INT,
              `DeletedOn` DATETIME,
              `DeletedBy` INT,
              PRIMARY KEY(`Proc_id`));
        """)
    return b

def emrg_doctor():
    b = c.execute("""
        CREATE TABLE `EMERG_DOCTOR`(
          `Emerg_d_id` INT NOT NULL,
          `Name` TEXT,
          `Contact` INT,
          `Room` TEXT,
          `Start_time` TIME,
          `End_time` TIME,
          `Shift_days` DATE,
          `Availability` BOOLEAN NOT NULL,
          PRIMARY KEY(`Emerg_d_id`));
        """)
    return b
def emrg_room():
    b = c.execute("""
        CREATE TABLE `EMERG_ROOM`(
          `ER_id` INT NOT NULL,
          `Facilities` TEXT,
          `Locatioon` TEXT,
          `Availability` BOOLEAN NOT NULL,
          `CreatedOn` DATETIME,
          `CreatedBy` INT,
          `UpdatedOn` DATETIME,
          `UpdatedBy` INT,
          `DeletedOn` DATETIME,
          `DeletedBy` INT,
          PRIMARY KEY(`ER_id`));
        """)
    return b
def emerg_addmission():
    b = c.execute("""
        CREATE TABLE `EMERG_ADMISSION`(
          `Em_adm_id` INT NOT NULL,
          `Patient_id` INT NOT NULL,
          `Emerg_Doctors_id` INT NOT NULL,
          `ERoom_id` INT NOT NULL,
          `Nurse_id` INT NOT NULL,
          `CallOn` DATETIME,
          `ArriveOn` DATETIME,
          `Reason` TEXT,
          `Condition` TEXT,
          `CreatedOn` DATETIME NOT NULL,
          `CreatedBy` INT,
          `UpdatedOn` DATETIME NOT NULL,
          `UpdatedBy` INT,
           PRIMARY KEY(`Em_adm_id`));
        """)
    return b
def stay_room():
    b = c.execute("""
        CREATE TABLE `STAY_ROOM`(
          `S_room_id` INT NOT NULL,
          `Facility` TEXT,
          `Location` TEXT,
          `Availability` BOOLEAN NOT NULL,
          `Price_per_day` INT,
          `CreatedOn` DATETIME NOT NULL,
          `CreatedBy` INT,
          `UpdatedOn` DATETIME NOT NULL,
          `UpdatedBy` INT,
          `DeletedOn` DATETIME NOT NULL,
          `DeletedBy` INT,
          PRIMARY KEY(`S_room_id`));
        """)
    return b
def in_prescription():
    b = c.execute("""
        CREATE TABLE `IN_PRESCRIPTION`(
          `In_pr_id` INT NOT NULL,
          `Procedure_id` INT NOT NULL,
          `Medicine_id` INT NOT NULL,
          `CreatedOn` DATETIME NOT NULL,
          `CreatedBy` INT,
          `UpdatedOn` DATETIME NOT NULL,
          `UpdatedBy` INT,
          PRIMARY KEY(`In_pr_id`));
        """)
    return b
#Calling Part

def creating_all():
  patient()
  department() 
  doctor() 
  nurse() 
  out_appointment()
  app_prescrription()
  inpatient_stay() 
  emerg_prescription()
  bill()
  medicine()
  procedure()
  emrg_doctor()
  emrg_room()
  emerg_addmission()
  stay_room()
  in_prescription()  

creating_all()

conn.close()