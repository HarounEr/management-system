import sqlite3
from tkinter import *					
from tkinter import ttk 
import tkinter.font as tkFont
import random

#To save the users data on the database when condition is met
def save(uName, uPass, uType):
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='users' ''')

        result = StringVar()
        label = Label(tab2,textvariable=result)
        label.grid(row=6,column=1)
        #Create a users table if there is no users table created
        if cur.fetchone()[0]!=1:
            cur.execute('''create table IF NOT EXISTS users (userid INTEGER PRIMARY KEY AUTOINCREMENT,uname TEXT NOT NULL, passwd TEXT NOT NULL, usertype TEXT NOT NULL,
            UNIQUE (userid,uname) ON CONFLICT ABORT)''')
        #Find if the username and userid already exists in the database, It will fail if it already exists
        cur.execute('''SELECT * FROM users WHERE uname = ? OR userid = ?''',(uName.get(),uid.get()))
        if cur.fetchone() or uName.get() == '' or uid.get() == '':
            #Show a failed label with color red
            result.set("Register failed!\nUser or User id already exist!")
            label.config(fg='red')
            print("Register Failed!")
        #If it doesn't exist yet, it will save the data to the databasess
        else:
            #Show a success label with color green
            result.set("Register successful! \n User Information Registered ")
            label.config(fg='green')
            cur.execute('insert into users values(?,?,?,?)', (uid.get(),uName.get(), uPass.get(), uType.get()))
            print(uid.get(),uName.get())
            print("Register Successfull!")
            con.commit()

    #If there is an error
    except con.Error as err:
        print("Failed to create table, Table already exist", err)

    finally:
        if con:
            #Closing the connection to the database
            con.close()
            print("Connection closed")
#Creating a table called users and inserting multiple data inside   -Omar's Work
def createUsersTable():
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='users' ''')

        if cur.fetchone()[0]!=1:
            cur.execute('''create table IF NOT EXISTS users (userid INTEGER PRIMARY KEY AUTOINCREMENT,uname TEXT NOT NULL, passwd TEXT NOT NULL, usertype TEXT NOT NULL,
            UNIQUE (userid,uname) ON CONFLICT ABORT)''')
            
        cur.execute('''INSERT INTO 'users' ('userid', 'uname', 'passwd', 'usertype') VALUES
            ('1000', 'omar', 'omar', 'All'),
            ('1001', 'suleima', 'suleima', 'All'),
            ('1002', 'haroun', 'haroun', 'All'),
            ('1003', 'user1', 'user1', 'Manager'),
            ('1004 ', 'user2', 'user2', 'Warden')''')
        con.commit()

    #If there is an error
    except con.Error as err:
        print("Failed to create table, Table already exist", err)

    finally:
        if con:
            ##Closing the connection to the database
            con.close()
            print("Connection closed")
#Creating a table called lease and inserting multiple data inside  -Omar's Work
def createLeaseTable():
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='lease' ''')

        if cur.fetchone()[0]!=1:
            cur.execute('''create table IF NOT EXISTS lease (leaseid INTEGER PRIMARY KEY , leaseno int DEFAULT "",leaseduration int,hallid int, roomid int , studentid int DEFAULT " ",
            UNIQUE (leaseid) ON CONFLICT ABORT,
            FOREIGN KEY(hallid) 
                REFERENCES hall(hallid),
            FOREIGN KEY(roomid) 
                REFERENCES room(roomid),
            FOREIGN KEY(studentid)  
                REFERENCES student(studentid))''')

        cur.execute('''INSERT INTO 'lease' ('leaseid', 'leaseno', 'leaseduration', 'hallid', 'roomid', 'studentid') VALUES
            ('100', '', '12','100', '1', ' '), ('101', '1001', '12','100', '2', '10'), ('102', '1002', '12','100', '3', '11'),
            ('103', '','12', '100', '4', ' '), ('104', '1003', '12','101', '2', '12'), ('105', '1004', '12','101', '3', '13'),
            ('106', '', '12','102', '5', ' '), ('107', '','12', '102', '5', ' '), ('108', '','12', '103', '6', ' '),
            ('109', '', '12','103', '6', ' '), ('110', '', '12','104', '7', ' '), ('111', '', '12','104', '7', ' ')''')

        con.commit()

    #If there is an error
    except con.Error as err:
        print("Failed to create table, Table already exist", err)
    finally:
        if con:
            #Closing the connection to the database
            con.close()
            print("Connection closed")

#Creating a table called room and inserting multiple data inside -Omar's Work
def createRoomTable():
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='room' ''')

        if cur.fetchone()[0]!=1:
            cur.execute('''create table IF NOT EXISTS room (roomid INTEGER PRIMARY KEY AUTOINCREMENT,roomno int NOT NULL, occupancystatus TEXT DEFAULT "Unoccupied" , cleaningstatus TEXT DEFAULT "Off-line" NOT NULL,
            studentid int,hallid int, UNIQUE (roomid) ON CONFLICT ABORT,
            FOREIGN KEY(studentid) 
                REFERENCES student(studentid),
            FOREIGN KEY(hallid) 
                REFERENCES hall(hallid))''')
    
        cur.execute('''INSERT INTO 'room' ('roomid', 'roomno', 'occupancystatus', 'cleaningstatus','studentid', 'hallid') VALUES
            ('1', '100', 'Unoccupied', 'Off-line','','100'), ('2', '101', 'Occupied', 'Clean', '10', '100'),
            ('3', '102', 'Occupied', 'Dirty', '11', '100'), ('4', '103', 'Unoccupied', 'Off-line','', '100'),
            ('5', '104', 'Unoccupied', 'Off-line','', '101'), ('6', '105', 'Unoccupied', 'Off-line','', '101'),
            ('7', '106', 'Unoccupied', 'Off-line','', '101')''')

        con.commit()
    
    #If there is an error
    except con.Error as err:
        print("Failed to create table, Table already exist", err)
    finally:
        if con:
            #Closing the connection to the database
            con.close()
            print("Connection closed")
#Creating a table called hall and inserting multiple data inside  -Omar's Work
def createHalltable():
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='hall' ''')

        if cur.fetchone()[0]!=1:
            cur.execute('''create table IF NOT EXISTS hall (hallid INTEGER PRIMARY KEY AUTOINCREMENT,hallno int , hallname TEXT,
                UNIQUE (hallid) ON CONFLICT ABORT)''')
    
        cur.execute('''INSERT INTO 'hall' ('hallid', 'hallno', 'hallname' ) VALUES
            ('100', '9', 'UWEH1'), ('101', '10', 'UWEH2'), ('102', '11', 'UWEH3'), ('103', '12', 'UWEH4'),
            ('104', '13', 'UWEH5'), ('105', '14', 'UWEH6'), ('106', '15', 'UWEH7')''')

        con.commit()
    except con.Error as err:
        print("Failed to create table, Table already exist", err)
    finally:
        if con:
            con.close()
            print("Connection closed")
#Creating a table called student and inserting multiple data inside -Omar's Work
def createStudentTable():
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='student' ''')

        if cur.fetchone()[0]!=1:
            cur.execute('''create table IF NOT EXISTS student (studentid INTEGER PRIMARY KEY AUTOINCREMENT,studentno int 
            ,studentname text DEFAULT "",
                UNIQUE (studentid,studentno,studentname) ON CONFLICT ABORT)''')
    
        cur.execute('''INSERT INTO 'student' ('studentid', 'studentno', 'studentname') VALUES ('10', '123456', 'Thomas Maul'), 
        ('11', '123577', 'Chris Roadknight'), ('12', '434535', 'Nadeem Khan'), ('13', '123123', 'Max Miller')''')

        con.commit()

    #If there is an error
    except con.Error as err:
        print("Failed to create table, Table already exist", err)
    finally:
        if con:
            #Closing the connection to the database
            con.close()
            print("Connection closed")

#To refresh the table
def refreshTable(t):
    #Delete existing data
    for item in t.get_children():
        t.delete(item)

    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
      
        cur.execute('''SELECT lease.leaseno AS lease_number, hall.hallname AS hall_name, hall.hallno AS hall_number, 
        room.roomno AS room_number, student.studentname AS student_name, room.occupancystatus AS occupancy_status, 
        room.cleaningstatus AS cleaning_status,lease.leaseduration as lease_duration, lease.leaseid as lease_id, lease.hallid as hall_id, lease.roomid as room_id,
        lease.studentid as student_id FROM lease LEFT JOIN hall ON hall.hallid = lease.hallid
        LEFT JOIN room ON room.roomid = lease.roomid LEFT JOIN student ON student.studentid = lease.studentid  
        WHERE lease.leaseid IS NOT NULL''')

        #Inserting data from database into the table
        rows = cur.fetchall()

        for row in rows:
            t.insert("", END, values=row)
            # table.insert("", END, values=row,tags = ('gray'))
            # table.tag_configure('gray', background = 'light gray')
        
        con.close()

    except con.Error as err:
        print("Operation is failed", err)

    finally:
        if con:
            con.close()
            print("Connection closed")

    return t

def viewApplication():
    w4 = Toplevel(w) 
    w4.title("Application")
    w4.geometry('405x200')

    #Creating the table
    applicationTable = ttk.Treeview(w4,selectmode="browse")
    applicationTable.grid(row=0,column=1)

    #Scrollbar
    tableScroll5 = ttk.Scrollbar(w4,orient ="vertical", command = trv.yview)
    tableScroll5.grid(row=0,column=2)

    applicationTable.configure(xscrollcommand = tableScroll5.set)
    
    #Defining number of columns
    applicationTable["columns"] = ("1", "2", "3")
    
    #Defining heading
    applicationTable['show'] = 'headings'
    
    #Assigning the width and anchor to the respective columns
    applicationTable.column("1", width = 120, anchor ='c')
    applicationTable.column("2", width = 120, anchor ='c')
    applicationTable.column("3", width = 150, anchor ='c')

    #Assigning the heading names to the respective columns
    applicationTable.heading("1", text ="Student ID")
    applicationTable.heading("2", text ="Student Name")
    applicationTable.heading("3", text ="Duration Requested")

    applicationList = [(132131, "James Bond" ,"12"), (123412, "Lebron Bryant", "12")]
    index = iid = 0
    for row in applicationList:
        applicationTable.insert("", index, iid, values=row)
        index = iid = index + 1



def systemWindow():  
    

    #To delete lease row when the delete button is pressed for Manager user
    def deleteLease():
        try:
            con = sqlite3.connect('staff.db')
            cur = con.cursor()
            cur.execute('''select count(name) from sqlite_master where type='table' and name='lease' ''')
        
            for selectedRow in table.selection():
                cur.execute('''DELETE FROM lease WHERE leaseid = ?''', [leaseIdEntry.get()],)
                con.commit()
                table.delete(selectedRow)

        except con.Error as err:
            print("Failed to connect to database", err)

        finally:
            if con:
                con.close()
                print("Connection closed")

    #To delete a row from the lease and the table for All usertype
    def deleteLeaseForAll():

        try:
            con = sqlite3.connect('staff.db')
            cur = con.cursor()
            cur.execute('''select count(name) from sqlite_master where type='table' and name='lease' ''')
            #To delete selected row from the database and the treeview table
            for selectedRow3 in table3.selection():
                cur.execute('''DELETE FROM lease WHERE leaseid = ?''', [leaseIdEntry3.get()],)
                con.commit()

                table3.delete(selectedRow3)

        except con.Error as err:
            print("Failed to connect to database", err)

        finally:
            if con:
                con.close()
                print("Connection closed")

            
    #To update lease when update button is pressed
    def updateLease():

        #To identify what row is being click in the table
        selected = table.focus()
        
        #To create random id number for new student added to the database
        randomNo = random.randrange(100000, 500000, 6)

        try:
            con = sqlite3.connect('staff.db')
            cur = con.cursor()
            cur.execute('''select count(name) from sqlite_master where type='table' and name='lease' ''')
            
            #To insert item into the table so we can get specific item inside from all the entry button
            table.item(selected, text="", values=(leaseNumberEntry.get(), hallNameEntry.get(), hallNumberEntry.get(), \
                roomNumberEntry.get(), studentNameEntry.get(), variable.get(), cleaningStatusEntry.get(),leaseDurationEntry.get(), leaseIdEntry.get() \
                    ,hallIdEntry.get(), roomIdEntry.get(), studentIdEntry.get()))
            
            #To check if the username entered into the entry box exist in the database if not exist, it will be added with randomise student number
            cur.execute('''SELECT rowid FROM student WHERE studentname = ?''',(studentNameEntry.get(),))
            data = cur.fetchall()
            if len(data) == 0 and studentNameEntry.get() != '' and studentNameEntry.get() != 'None':
                cur.execute('''INSERT INTO 'student' ('studentno','studentname') VALUES
                (?,?)''',(randomNo,studentNameEntry.get()), ) 
                 
            #To update the lease number with the data in the lease number entry button
            cur.execute('''UPDATE lease SET
            leaseno = :leaseNumber,  leaseduration = :leaseDuration,
            studentid = (SELECT student.studentid FROM student WHERE student.studentname = :studentName)
            WHERE leaseid = :leaseId''', 
            {
                'leaseNumber': leaseNumberEntry.get(),'studentName': studentNameEntry.get(),'leaseId': leaseIdEntry.get(),
                'leaseDuration': leaseDurationEntry.get()
		    })

            #To update the occupancy status of the room with the data in the drop down button
            cur.execute('''UPDATE room SET
            occupancystatus = :occupancy
            WHERE roomno = :roomNo''', 
            {
                'roomNo': roomNumberEntry.get(),'occupancy': variable.get(),
		    })
        
            con.commit()

        except con.Error as err:
            print("Failed to connect to database", err)

        finally:
            if con:
                con.close()
                print("Connection closed")
                
    
    #To update the lease for all user tab           
    def updateLeaseForAll():

        #To identify what row is being click in the table
        selected4 = table3.focus()
        #To create random id number for new student added to the database
        randomNo2 = random.randrange(100000, 500000, 6)

        try:
            con = sqlite3.connect('staff.db')
            cur = con.cursor()
            cur.execute('''select count(name) from sqlite_master where type='table' and name='room' ''')
            #To insert item into the table so we can get specific item inside from all the entry button
            table3.item(selected4, text="", values=(leaseNumberEntry3.get(), hallNameEntry3.get(), hallNumberEntry3.get(), \
                roomNumberEntry3.get(), studentNameEntry3.get(), variable3.get(), variable4.get(), leaseDurationEntry3.get(), leaseIdEntry3.get() \
                    ,hallIdEntry3.get(), roomIdEntry3.get(), studentIdEntry3.get()))
            
            #To check if the username entered into the entry box exist in the database if not exist, it will be added with randomise student number
            cur.execute('''SELECT rowid FROM student WHERE studentname = ?''',(studentNameEntry3.get(),))
            data = cur.fetchall()
            if len(data) == 0 and studentNameEntry3.get() != '' and studentNameEntry3.get() != 'None':
                cur.execute('''INSERT INTO 'student' ('studentno','studentname') VALUES
                (?,?)''',(randomNo2,studentNameEntry3.get()), ) 

                 
            #To update the lease number with the data in the lease number entry button
            cur.execute('''UPDATE lease SET
            leaseno = :leaseNumber, leaseduration = :leaseDuration, 
            studentid = (SELECT student.studentid FROM student WHERE student.studentname = :studentName)
            WHERE leaseid = :leaseId''', 
            {
                'leaseNumber': leaseNumberEntry3.get(),'studentName': studentNameEntry3.get(),'leaseId': leaseIdEntry3.get(),
                'leaseDuration': leaseDurationEntry3.get()
		    })

            #To update the occupancy status of the room with the data in the drop down button
            cur.execute('''UPDATE room SET
            occupancystatus = :occupancy
            WHERE roomno = :roomNo''', 
            {
                'roomNo': roomNumberEntry3.get(),
                'occupancy': variable3.get(),
		    })

            #Update the room cleaning status
            cur.execute('''UPDATE room SET
            cleaningstatus = :cleaningStatus
            WHERE roomno = :roomno''', 
            {
                'roomno': roomNumberEntry3.get(),
                'cleaningStatus': variable4.get(),
		    })

            con.commit()

        except con.Error as err:
            print("Failed to connect to database", err)

        finally:
            if con:
                con.close()
                print("Connection closed")                   
                
    #To update cleaning status when the apply button is pressed
    def updateCleaningStatus():
        selected5 = table2.focus()
        try:
            con = sqlite3.connect('staff.db')
            cur = con.cursor()
            cur.execute('''select count(name) from sqlite_master where type='table' and name='room' ''')
            table2.item(selected5, text="", values=(leaseNumberEntry2.get(), hallNameEntry2.get(), hallNumberEntry2.get(), \
                roomNumberEntry2.get(), studentNameEntry2.get(), occupancyEntry2.get(), variable2.get(), leaseDurationEntry2.get()))
            
            #Update the cleaning status of a room
            cur.execute('''UPDATE room SET
            cleaningstatus = :cleaningStatus
            WHERE roomno = :roomno''', 
            {
                'roomno': roomNumberEntry2.get(),
                'cleaningStatus': variable2.get(),
		    })

            con.commit()

        except con.Error as err:
            print("Failed to connect to database", err)

        finally:
            if con:
                con.close()
                print("Connection closed")

    #When a row is pressed or selected in the manager tab    
    def managerSelect(event):
        
        #clear the entry boxes
        hallNameEntry.delete(0,END)
        hallNumberEntry.delete(0,END)
        roomNumberEntry.delete(0,END)
        leaseNumberEntry.delete(0,END)
        leaseDurationEntry.delete(0,END)
        studentNameEntry.delete(0,END)
        leaseIdEntry.delete(0,END)
        hallIdEntry.delete(0,END)
        roomIdEntry.delete(0,END)
        studentIdEntry.delete(0,END)
        cleaningStatusEntry.delete(0,END)
        #Checking what is selected by the mouse
        selected = table.focus()
        #Putting all the values of the selected row inside the table as item
        values = table.item(selected, 'values')
        #Putting the data into the entry boxes to show what is selected
        hallNameEntry.insert(0, values[1])
        hallNumberEntry.insert(0, values[2])
        roomNumberEntry.insert(0, values[3])
        leaseNumberEntry.insert(0, values[0])
        studentNameEntry.insert(0, values[4])
        variable.set(values[5])
        cleaningStatusEntry.insert(0,values[6])
        leaseDurationEntry.insert(0, values[7])
        leaseIdEntry.insert(0,values[8])
        hallIdEntry.insert(0,values[9])
        roomIdEntry.insert(0,values[10])
        studentIdEntry.insert(0,values[11])
        
    #When a row is pressed or selected in the warden tab 
    def wardenSelect(event):
        
        #clear the entry boxes
        hallNameEntry2.delete(0,END)
        hallNumberEntry2.delete(0,END)
        roomNumberEntry2.delete(0,END)
        leaseNumberEntry2.delete(0,END)
        studentNameEntry2.delete(0,END)
        occupancyEntry2.delete(0,END)
        leaseDurationEntry2.delete(0,END)
    
        #Checking what is selected by the mouse
        selected2 = table2.focus()
        #Putting all the values of the selected row inside the table as item
        values2 = table2.item(selected2, 'values')

        #Putting the data into the entry boxes to show what is selected
        hallNameEntry2.insert(0, values2[1])
        hallNumberEntry2.insert(0, values2[2])
        roomNumberEntry2.insert(0, values2[3])
        leaseNumberEntry2.insert(0, values2[0])
        studentNameEntry2.insert(0, values2[4])
        occupancyEntry2.insert(0, values2[5])
        variable2.set(values2[6])
        leaseDurationEntry2.insert(0, values2[7])
        
    #When a row is pressed or selected in the all tab 
    def allSelect(event):
        
        #clear the entry boxes
        hallNameEntry3.delete(0,END)
        hallNumberEntry3.delete(0,END)
        roomNumberEntry3.delete(0,END)
        leaseNumberEntry3.delete(0,END)
        studentNameEntry3.delete(0,END)
        leaseIdEntry3.delete(0,END)
        hallIdEntry3.delete(0,END)
        roomIdEntry3.delete(0,END)
        studentIdEntry3.delete(0,END)
        leaseDurationEntry3.delete(0,END)
        
        #Checking what is selected by the mouse
        selected3 = table3.focus()
        #Putting all the values of the selected row inside the table as item
        values3 = table3.item(selected3, 'values')
        #Putting the data into the entry boxes to show what is selected
        hallNameEntry3.insert(0, values3[1])
        hallNumberEntry3.insert(0, values3[2])
        roomNumberEntry3.insert(0, values3[3])
        leaseNumberEntry3.insert(0, values3[0])
        studentNameEntry3.insert(0, values3[4])
        variable3.set(values3[5])
        variable4.set(values3[6])
        leaseDurationEntry3.insert(0, values3[7])
        leaseIdEntry3.insert(0,values3[8])
        hallIdEntry3.insert(0,values3[9])
        roomIdEntry3.insert(0,values3[10])
        studentIdEntry3.insert(0,values3[11])

        
    #Third window where it shows the table
    w3 = Toplevel(w) 
    w3.title("UWE Bristol Accomodation System")
    w3.geometry('895x450')

    tabControl1 = ttk.Notebook(w3)
    #Tabs for Manager, Warden and All
    tab1 = ttk.Frame(tabControl1)
    tab2 = ttk.Frame(tabControl1)
    tab3 = ttk.Frame(tabControl1)

    tabControl1.add(tab1, text = 'Manager')
    tabControl1.add(tab2, text = 'Warden')
    tabControl1.add(tab3, text = 'All')
    tabControl1.pack(expand = 1, fill = "both")
    

    #Manager Tab
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        cur.execute('''select count(name) from sqlite_master where type='table' and name='users' ''')
        #Check the user type of the user logged in using their username and password in the database
        cur.execute('''SELECT usertype FROM users WHERE uname = ? AND passwd = ?''',(uName.get(),uPass.get(),))
        usertype = cur.fetchall()
        user = usertype[0][0]
        print(user)

        if user == "Manager" or user == "All":
            
            #To put 2 frames (top and bottom) inside this frame because you can only have 1 frame in 1 tab
            allframe = Frame(tab1, highlightbackground="gray",  highlightthickness=2,width=700,height=400)
            allframe.pack(side=TOP, fill = BOTH, expand = True, padx=2, pady=2)

            topframe = Frame(allframe, highlightbackground="gray",  highlightthickness=2,width=500,height=200)
            topframe.pack(side=TOP, fill = BOTH, expand = False, padx=5, pady=10)

            bottomframe = Frame(topframe,highlightbackground="gray", highlightthickness=2,width=200,height=100)
            bottomframe.pack(side=BOTTOM, fill = BOTH, expand = False, padx=5, pady=15)

            #Scrollbar for tab1 top frame
            tableScroll = Scrollbar(topframe)
            tableScroll.pack(side = RIGHT, fill = Y)

            #Top frame
            s = ttk.Style()
            ttk.Style().theme_use('default')


            # Configure the style of Heading in Treeview widget
            s.configure('Treeview.Heading', rowheight = 50, background="light gray", font=('Arial Bold', 10), fill = BOTH,highlightbackground="gray",  highlightthickness=2)
            # s.configure('Treeview',highlightbackground="gray",  highlightthickness=2)

            #Creating a table for tab1 Manager tab
            table = ttk.Treeview(topframe, yscrollcommand = tableScroll.set, height = 80)
            table['columns'] = ('lease_number', 'hall_name', 'hall_number', 'room_number', 'student_name', 'occupancy_status', 'cleaning_status', 'lease_duration')

            #Configuring the scroll
            tableScroll.config(command = table.yview)

            table.tag_configure('cleaningStatus', background='gray')

            #Setting tables
            table.column("#0", width = 0, stretch = NO)
            table.column("lease_number",anchor=CENTER, width=100)
            table.column("hall_name",anchor=CENTER, width=100)
            table.column("hall_number",anchor=CENTER, width=100)
            table.column("room_number",anchor=CENTER, width=100)
            table.column("student_name",anchor=CENTER, width=100)
            table.column("occupancy_status",anchor=CENTER, width=120)
            table.column("cleaning_status",anchor=CENTER, width=110)
            table.column("lease_duration",anchor=CENTER, width=110)

            #Setting the heading of the table
            table.heading("#0",text="",anchor=CENTER)
            table.heading("lease_number",text="Lease Number",anchor=CENTER)
            table.heading("hall_name",text="Hall Name",anchor=CENTER)
            table.heading("hall_number",text="Hall Number",anchor=CENTER)
            table.heading("room_number",text="Room Number",anchor=CENTER)
            table.heading("student_name",text="Student Name",anchor=CENTER)
            table.heading("occupancy_status",text="Occupancy Status",anchor=CENTER)
            table.heading("cleaning_status",text="Cleaning Status",anchor=CENTER)
            table.heading("lease_duration",text="Lease Duration",anchor=CENTER)
            
            #Connecting to database 
            con = sqlite3.connect('staff.db')
            cur = con.cursor()

            #Selecting specific data from different tables in the database
            cur.execute('''SELECT lease.leaseno AS lease_number, hall.hallname AS hall_name, hall.hallno AS hall_number, 
            room.roomno AS room_number, student.studentname AS student_name, room.occupancystatus AS occupancy_status, 
            room.cleaningstatus AS cleaning_status,lease.leaseduration AS lease_duration, lease.leaseid as lease_id, lease.hallid as hall_id, lease.roomid as room_id,
            lease.studentid as student_id FROM lease LEFT JOIN hall ON hall.hallid = lease.hallid
            LEFT JOIN room ON room.roomid = lease.roomid LEFT JOIN student ON student.studentid = lease.studentid  
            WHERE lease.leaseid IS NOT NULL''')

            #Inserting data from database into the table
            rows = cur.fetchall()
            
            for row in rows:
                table.insert("", END, values=row)
            con.close()
            #Setting the font
            fontStyle = tkFont.Font(family = "Lucida Grande", size = 10)
            table.pack()

            #Bottom Frame
            label = Label(bottomframe,text="Lease Information", font = fontStyle)
            label.grid(row=0)

            #Display when clicked released
            table.bind('<ButtonRelease-1>', managerSelect)

            #Hall name label and text entry box
            hallNameLabel = Label(bottomframe, text="Hall Name")
            hallNameLabel.grid(sticky = W, row=1, column=0)
            hallName = StringVar()
            hallNameEntry = Entry(bottomframe, textvariable=hallName)
            hallNameEntry.grid(row=1, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            hallNameEntry.bind("<Key>", lambda a: "break")
            hallNameEntry.config({"background": "light gray"})
            
            #Hall number label and text entry box
            hallNumberLabel = Label(bottomframe, text="Hall Number")
            hallNumberLabel.grid(sticky = W,row=2, column=0)
            hallNumber = StringVar()
            hallNumberEntry = Entry(bottomframe, textvariable=hallNumber)
            hallNumberEntry.grid(row=2, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            hallNumberEntry.bind("<Key>", lambda a: "break")
            hallNumberEntry.config({"background": "light gray"})

            #Room number label and text entry box
            roomNumberLabel = Label(bottomframe, text="Room Number")
            roomNumberLabel.grid(sticky = W,row=3, column=0)
            roomNumber = StringVar()
            roomNumberEntry = Entry(bottomframe, textvariable=roomNumber)
            roomNumberEntry.grid(row=3, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            roomNumberEntry.bind("<Key>", lambda a: "break")
            roomNumberEntry.config({"background": "light gray"})
            #Empty label for free space
            spacer1 = Label(bottomframe, text="")
            spacer1.grid(row=1, column=2)
            #Lease number label and text entry box
            leaseNumberLabel = Label(bottomframe, text="Lease Number")
            leaseNumberLabel.grid(sticky = W,row=1, column=3)
            leaseNumber = StringVar()
            leaseNumberEntry = Entry(bottomframe, textvariable=leaseNumber)
            leaseNumberEntry.grid(row=1, column=4)

            leaseDurationLabel = Label(bottomframe, text="Lease Duration")
            leaseDurationLabel.grid(sticky = W,row=1, column=5)
            leaseDuration = StringVar()
            leaseDurationEntry = Entry(bottomframe, textvariable=leaseDuration)
            leaseDurationEntry.grid(row=1, column=6)

            leaseId = StringVar()
            leaseIdEntry = Entry(bottomframe, textvariable=leaseId)
            #To hide lease id box entry on the window but still receives the lease id so it can be retrieved later
            leaseIdEntry.pack_forget()

            hallId = StringVar()
            hallIdEntry = Entry(bottomframe, textvariable=hallId)
            #To hide hall id box entry on the window but still receives the lease id so it can be retrieved later
            hallIdEntry.pack_forget()

            roomId = StringVar()
            roomIdEntry = Entry(bottomframe, textvariable=roomId)
            #To hide room id entry box on the window but still receives the lease id so it can be retrieved later
            roomIdEntry.pack_forget()

            studentId = StringVar()
            studentIdEntry = Entry(bottomframe, textvariable=studentId)
            #To hide student id entry box on the window but still receives the lease id so it can be retrieved later or make it invisible
            studentIdEntry.pack_forget()

            studentNameLabel = Label(bottomframe, text="Student Name")
            studentNameLabel.grid(sticky = W,row=2, column=3)
            studentName = StringVar()
            studentNameEntry = Entry(bottomframe, textvariable=studentName)
            studentNameEntry.grid(row=2, column=4)

            OccupancyList = [
            "Unoccupied",
            "Occupied",

            ] 
            variable = StringVar(bottomframe)
            variable.set(OccupancyList[0])

            occupancyLabel = Label(bottomframe, text="Occupancy").grid(row=3, column=3)
            option = OptionMenu(bottomframe, variable, *OccupancyList)
            option.grid(row=3, column=4)

            cleaningStatus = StringVar()
            cleaningStatusEntry = Entry(bottomframe, textvariable=cleaningStatus)
            cleaningStatusEntry.pack_forget()
            

            spacer2 = Label(bottomframe, text="")
            spacer2.grid(row=4, column=0)

            updateButton = Button(bottomframe, text="Update", command=updateLease)
            updateButton.grid(row=5, column=4)

            deleteButton = Button(bottomframe, text="Delete", command=deleteLease)
            deleteButton.grid(row=5, column=3)

            refreshButton = Button(bottomframe, text="Refresh", command=lambda:refreshTable(table))
            refreshButton.grid(row=5, column=5) 

            viewApplicationButton = Button(bottomframe, text="View Application", command=viewApplication)
            viewApplicationButton.grid(row=5, column=6) 

            spacer3 = Label(bottomframe, text="")
            spacer3.grid(row=6, column=3)
            
        if user == "Warden":
            #To put 2 frames (top and bottom) inside this frame because you can only have 1 frame in 1 tab
            allframe = Frame(tab1, highlightbackground="red",  highlightthickness=2,width=900,height=400)
            allframe.pack(side=TOP, fill = BOTH, expand = True, padx=2, pady=2)

            warningLabel = Label(allframe, text="You can't acess this tab! \n Only Manager and Superstaff\n can acess this tab!", font=("Arial", 40),fg='red')
            warningLabel.pack(pady=20)

        #-------------------------------------------------------------------------------------------------------------------------
    
        #Warden Tab
        if user == "Warden" or user == "All":
          
            #To put 2 frames (top and bottom) inside this frame because you can only have 1 frame in 1 tab
            allframe2 = Frame(tab2, highlightbackground="gray",  highlightthickness=2,width=900,height=400)
            allframe2.pack(side=TOP, fill = BOTH, expand = True, padx=2, pady=2)
            #Top frame inside all frame
            topframe2 = Frame(allframe2, highlightbackground="gray",  highlightthickness=2,width=500,height=300)
            topframe2.pack(side=TOP, fill = BOTH, padx=5, pady=10)
            #Bottom frame inside all frame
            bottomframe2 = Frame(topframe2,highlightbackground="gray", highlightthickness=2,width=400,height=100)
            bottomframe2.pack(side=BOTTOM, fill = BOTH, padx=5, pady=15)

            #scrollbar
            tableScroll2 = Scrollbar(topframe2)
            tableScroll2.pack(side = RIGHT, fill = Y)

            s2 = ttk.Style()
            ttk.Style().theme_use('default')

            # Configure the style of Heading in Treeview widget
            s2.configure('Treeview.Heading', rowheight = 50, background="light gray", font=('Arial Bold', 10), fill = BOTH,highlightbackground="gray",  highlightthickness=2)

            #Creating a table inside tab2 Warden table
            table2 = ttk.Treeview(topframe2, yscrollcommand = tableScroll2.set, height = 80)
            table2['columns'] = ('lease_number', 'hall_name', 'hall_number', 'room_number', 'student_name', 'occupancy_status', 'cleaning_status', 'lease_duration')

            #Configuring the scroll in the table
            tableScroll2.config(command = table2.yview)


            #Setting tables
            table2.column("#0", width = 0, stretch = NO)
            table2.column("lease_number",anchor=CENTER, width=100)
            table2.column("hall_name",anchor=CENTER, width=100)
            table2.column("hall_number",anchor=CENTER, width=100)
            table2.column("room_number",anchor=CENTER, width=100)
            table2.column("student_name",anchor=CENTER, width=100)
            table2.column("occupancy_status",anchor=CENTER, width=120)
            table2.column("cleaning_status",anchor=CENTER, width=110)
            table2.column("lease_duration",anchor=CENTER, width=110)
            
            #Setting the heading of the table
            table2.heading("#0",text="",anchor=CENTER)
            table2.heading("lease_number",text="Lease Number",anchor=CENTER)
            table2.heading("hall_name",text="Hall Name",anchor=CENTER)
            table2.heading("hall_number",text="Hall Number",anchor=CENTER)
            table2.heading("room_number",text="Room Number",anchor=CENTER)
            table2.heading("student_name",text="Student Name",anchor=CENTER)
            table2.heading("occupancy_status",text="Occupancy Status",anchor=CENTER)
            table2.heading("cleaning_status",text="Cleaning Status",anchor=CENTER)
            table2.heading("lease_duration",text="Lease Duration",anchor=CENTER)

            #connecting to database 
            con = sqlite3.connect('staff.db')
            cur = con.cursor()

            #Selecting specific data from different table in the database
            cur.execute('''SELECT lease.leaseno AS lease_number, hall.hallname AS hall_name, hall.hallno AS hall_number, 
            room.roomno AS room_number, student.studentname AS student_name, room.occupancystatus AS occupancy_status, 
            room.cleaningstatus AS cleaning_status, lease.leaseduration as lease_duration, lease.leaseid as lease_id, lease.hallid as hall_id, lease.roomid as room_id,
            lease.studentid as student_id FROM lease 
            LEFT JOIN hall ON hall.hallid = lease.hallid
            LEFT JOIN room ON room.roomid = lease.roomid
            LEFT JOIN student ON student.studentid = lease.studentid  
            WHERE lease.leaseid IS NOT NULL''')

            #Inserting data from database into the table
            rows = cur.fetchall()
            #Inserting the data from database selection to the table
            for row in rows:
                table2.insert("", END, values=row)

            #Display when clicked released
            table2.bind('<ButtonRelease-1>', wardenSelect)

            #Setting the font
            fontStyle = tkFont.Font(family = "Lucida Grande", size = 10)

            table2.pack()

            #Bottom Frame
            label2 = Label(bottomframe2,text="Cleaning Status", font = fontStyle)
            label2.grid(row=0)

            #Lease label and entry box
            leaseNumberLabel2 = Label(bottomframe2, text="Lease Number").grid(sticky = W, row=1, column=0)
            leaseNumber2 = StringVar()
            leaseNumberEntry2 = Entry(bottomframe2, textvariable=leaseNumber2)
            leaseNumberEntry2.grid(row=1, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            leaseNumberEntry2.bind("<Key>", lambda a: "break")
            leaseNumberEntry2.config({"background": "light gray"})

            #Hall label and entry box
            hallNameLabel2 = Label(bottomframe2, text="Hall Name").grid(sticky = W, row=2, column=0)
            hallName2 = StringVar()
            hallNameEntry2 = Entry(bottomframe2, textvariable=hallName2)
            hallNameEntry2.grid(row=2, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            hallNameEntry2.bind("<Key>", lambda a: "break")
            hallNameEntry2.config({"background": "light gray"})

            #Hall number label and entry box
            hallNumberLabel2 = Label(bottomframe2, text="Hall Number").grid(sticky = W,row=3, column=0)
            hallNumber2 = StringVar()
            hallNumberEntry2 = Entry(bottomframe2, textvariable=hallNumber2)
            hallNumberEntry2.grid(row=3, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            hallNumberEntry2.bind("<Key>", lambda a: "break")
            hallNumberEntry2.config({"background": "light gray"})

            #Room number label and entry box
            roomNumberLabel2 = Label(bottomframe2, text="Room Number").grid(sticky = W,row=4, column=0)
            roomNumber2 = StringVar()
            roomNumberEntry2 = Entry(bottomframe2, textvariable=roomNumber2)
            roomNumberEntry2.grid(row=4, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            roomNumberEntry2.bind("<Key>", lambda a: "break")
            roomNumberEntry2.config({"background": "light gray"})

            #Just to create an invisible label for space between labels
            spacer4 = Label(bottomframe2, text="")
            spacer4.grid(row=1, column=2)

            #Student name label and entry box
            studentNameLabel2 = Label(bottomframe2, text="Student Name").grid(sticky = W,row=1, column=3)
            studentName2 = StringVar()
            studentNameEntry2 = Entry(bottomframe2, textvariable=studentName2)
            studentNameEntry2.grid(row=1, column=4)
            #So it won't allow input on the entry box when pressed any key it break
            studentNameEntry2.bind("<Key>", lambda a: "break")
            studentNameEntry2.config({"background": "light gray"})

            #Room occupancy label and entry box
            occupancyLabel2 = Label(bottomframe2, text="Occupancy").grid(row=2, column=3)
            occupancy2 = StringVar()
            occupancyEntry2 = Entry(bottomframe2, textvariable=occupancy2)
            occupancyEntry2.grid(row=2, column=4)
            #So it won't allow input on the entry box when pressed any key it break
            occupancyEntry2.bind("<Key>", lambda a: "break")
            occupancyEntry2.config({"background": "light gray"})

            #Cleaning status choices for drop down menu
            CleaningStatusList = [
            "Off-line",
            "Clean",
            "Dirty",
            ] 
            #Declaring cleaning status variable as a string variable
            variable2 = StringVar(bottomframe2)
            variable2.set(CleaningStatusList[0])

            #Creating a label for cleaning status and a drop down menu
            cleaningStatusLabel = Label(bottomframe2, text="Cleaning Status").grid(row=3, column=3)
            option2 = OptionMenu(bottomframe2, variable2, *CleaningStatusList)
            option2.grid(row=3, column=4)

            leaseDurationLabel2 = Label(bottomframe2, text="Lease Duration")
            leaseDurationLabel2.grid(sticky = W,row=1, column=5)
            leaseDuration2 = StringVar()
            leaseDurationEntry2 = Entry(bottomframe2, textvariable=leaseDuration2)
            leaseDurationEntry2.grid(row=1, column=6)
            #So it won't allow input on the entry box when pressed any key it break
            leaseDurationEntry2.bind("<Key>", lambda a: "break")
            leaseDurationEntry2.config({"background": "light gray"})

            #Just to create an empty space between
            spacer5 = Label(bottomframe2, text="")
            spacer5.grid(row=4, column=0)

            #Applu button to appply the cleaning status
            applyButton2 = Button(bottomframe2, text="Apply", command=updateCleaningStatus)
            applyButton2.grid(row=5, column=4)

            #To refresh the table when click
            refreshButton2 = Button(bottomframe2, text="Refresh", command=lambda:refreshTable(table2))
            refreshButton2.grid(row=5, column=5) 
            #Just to create an empty space between
            spacer6 = Label(bottomframe2, text="")
            spacer6.grid(row=6, column=3)
        #If the usertype is manager this will display warning message
        if user == "Manager":
            #To put 2 frames (top and bottom) inside this frame because you can only have 1 frame in 1 tab
            allframe2 = Frame(tab2, highlightbackground="red",  highlightthickness=2,width=900,height=400)
            allframe2.pack(side=TOP, fill = BOTH, expand = True, padx=2, pady=2)

            warningLabel2 = Label(allframe2, text="You can't acess this tab! \n Only Warden and SuperStaff \n can acess this tab!", font=("Arial", 40),fg='red')
            warningLabel2.pack(pady=20)

        #-------------------------------------------------------------------------------------------------------------------------
        #All staff Tab
        #If the usertype is All this will show the interface inside the tab
        if user == "All":
            #To put 2 frames (top and bottom) inside this frame because you can only have 1 frame in 1 tab
            allframe3 = Frame(tab3, highlightbackground="gray",  highlightthickness=2,width=900,height=400)
            allframe3.pack(side=TOP, fill = BOTH, expand = True, padx=2, pady=2)
            #The top frame inside all frame
            topframe3 = Frame(allframe3, highlightbackground="gray",  highlightthickness=2,width=500,height=300)
            topframe3.pack(side=TOP, fill = BOTH, padx=5, pady=10)
            #The bottom frame inside all frame
            bottomframe3 = Frame(topframe3,highlightbackground="gray", highlightthickness=2,width=400,height=100)
            bottomframe3.pack(side=BOTTOM, fill = BOTH, padx=5, pady=15)

            #Scrollbar
            tableScroll3 = Scrollbar(topframe3)
            tableScroll3.pack(side = RIGHT, fill = Y)

            #Top frame
            s3 = ttk.Style()
            ttk.Style().theme_use('default')

            #Configure the style of Heading in Treeview widget
            s3.configure('Treeview.Heading', rowheight = 50, background="light gray", font=('Arial Bold', 10), fill = BOTH,highlightbackground="gray",  highlightthickness=2)

            table3 = ttk.Treeview(topframe3, yscrollcommand = tableScroll3.set, height = 80)
            table3['columns'] = ('lease_number', 'hall_name', 'hall_number', 'room_number', 'student_name', 'occupancy_status', 'cleaning_status', 'lease_duration')

            tableScroll3.config(command = table.yview)

            #Display when clicked
            table3.bind('<ButtonRelease-1>', allSelect)

            #Setting tables
            table3.column("#0", width = 0, stretch = NO)
            table3.column("lease_number",anchor=CENTER, width=100)
            table3.column("hall_name",anchor=CENTER, width=100)
            table3.column("hall_number",anchor=CENTER, width=100)
            table3.column("room_number",anchor=CENTER, width=100)
            table3.column("student_name",anchor=CENTER, width=100)
            table3.column("occupancy_status",anchor=CENTER, width=120)
            table3.column("cleaning_status",anchor=CENTER, width=110)
            table3.column("lease_duration",anchor=CENTER, width=110)

            #Setting the heading for the table
            table3.heading("#0",text="",anchor=CENTER)
            table3.heading("lease_number",text="Lease Number",anchor=CENTER)
            table3.heading("hall_name",text="Hall Name",anchor=CENTER)
            table3.heading("hall_number",text="Hall Number",anchor=CENTER)
            table3.heading("room_number",text="Room Number",anchor=CENTER)
            table3.heading("student_name",text="Student Name",anchor=CENTER)
            table3.heading("occupancy_status",text="Occupancy Status",anchor=CENTER)
            table3.heading("cleaning_status",text="Cleaning Status",anchor=CENTER)
            table3.heading("lease_duration",text="Lease Duration",anchor=CENTER)

            #Inserting the data selected from the database into the table
            for row in rows:
                table3.insert("", END, values=row)

            con.close()
            #Setting the font
            fontStyle = tkFont.Font(family = "Lucida Grande", size = 10)

            table3.pack()

            #Bottom Frame
            label3 = Label(bottomframe3,text="Lease Information", font = fontStyle)
            label3.grid(row=0)

            #Display when clicked released
            table3.bind('<ButtonRelease-1>', allSelect)

            #Hall name label and text entry box
            hallNameLabel4 = Label(bottomframe3, text="Hall Name").grid(sticky = W, row=1, column=0)
            hallName3 = StringVar()
            hallNameEntry3 = Entry(bottomframe3, textvariable=hallName3)
            hallNameEntry3.grid(row=1, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            hallNameEntry3.bind("<Key>", lambda a: "break")
            hallNameEntry3.config({"background": "light gray"})
            

            hallNumberLabel4 = Label(bottomframe3, text="Hall Number").grid(sticky = W,row=2, column=0)
            hallNumber3 = StringVar()
            hallNumberEntry3 = Entry(bottomframe3, textvariable=hallNumber3)
            hallNumberEntry3.grid(row=2, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            hallNumberEntry3.bind("<Key>", lambda a: "break")
            hallNumberEntry3.config({"background": "light gray"})

            roomNumberLabel4 = Label(bottomframe3, text="Room Number").grid(sticky = W,row=3, column=0)
            roomNumber3 = StringVar()
            roomNumberEntry3 = Entry(bottomframe3, textvariable=roomNumber3)
            roomNumberEntry3.grid(row=3, column=1)
            #So it won't allow input on the entry box when pressed any key it break
            roomNumberEntry3.bind("<Key>", lambda a: "break")
            roomNumberEntry3.config({"background": "light gray"})
            
            #Just empty label to create space
            spacer10 = Label(bottomframe3, text="")
            spacer10.grid(row=1, column=2)
            #Lease number label and entry boxes
            leaseNumberLabel4 = Label(bottomframe3, text="Lease Number").grid(sticky = W,row=1, column=3)
            leaseNumber3 = StringVar()
            leaseNumberEntry3 = Entry(bottomframe3, textvariable=leaseNumber3)
            leaseNumberEntry3.grid(row=1, column=4)
            #Lease id label which is invisible becuse of pack_forget to hide it in the interface but still can get the lease id
            lease_id3 = StringVar()
            leaseIdEntry3 = Entry(bottomframe3, textvariable=lease_id3)
            leaseIdEntry3.pack_forget()
            #Hall id label which is invisible becuse of pack_forget to hide it in the interface but still can get the Hall id
            hallId3 = StringVar()
            hallIdEntry3 = Entry(bottomframe3, textvariable=hallId3)
            hallIdEntry3.pack_forget()
            #Room id label which is invisible becuse of pack_forget to hide it in the interface but still can get the Room id
            roomId3 = StringVar()
            roomIdEntry3 = Entry(bottomframe3, textvariable=roomId3)
            roomIdEntry3.pack_forget()
            #Student id label which is invisible becuse of pack_forget to hide it in the interface but still can get the Student id
            studentId3 = StringVar()
            studentIdEntry3 = Entry(bottomframe3, textvariable=studentId3)
            studentIdEntry3.pack_forget()
            #Student number label and entry boxes
            studentNameLabel4 = Label(bottomframe3, text="Student Name").grid(sticky = W,row=2, column=3)
            studentName3 = StringVar()
            studentNameEntry3 = Entry(bottomframe3, textvariable=studentName3)
            studentNameEntry3.grid(row=2, column=4)
            #Occupancy status list of option
            OccupancyList2 = [
            "Unoccupied",
            "Occupied",
            ] 
            #Variable set for occupancy list chosen and set as string variable
            variable3 = StringVar(bottomframe3)
            variable3.set(OccupancyList2[0])
            #Occupancy label and drop down button
            occupancyLabel4 = Label(bottomframe3, text="Occupancy").grid(row=3, column=3)
            option2 = OptionMenu(bottomframe3, variable3, *OccupancyList2).grid(row=3, column=4)
            #Cleaning status list of option
            CleaningStatusList2 = [
            "Off-line",
            "Clean",
            "Dirty",
            ] 
            #Variable set for cleaning status list chosen and set as string variable
            variable4 = StringVar(bottomframe3)
            variable4.set('Off-line')
            #Cleaning status label and drop down button
            cleaningStatusLabel3 = Label(bottomframe3, text="Cleaning Status").grid(row=4, column=3)
            option3 = OptionMenu(bottomframe3, variable4, *CleaningStatusList2).grid(row=4, column=4)

            leaseDurationLabel3 = Label(bottomframe3, text="Lease Duration")
            leaseDurationLabel3.grid(sticky = W,row=1, column=5)
            leaseDuration3 = StringVar()
            leaseDurationEntry3 = Entry(bottomframe3, textvariable=leaseDuration3)
            leaseDurationEntry3.grid(row=1, column=6)

            #Empty label to create space between
            spacer11 = Label(bottomframe3, text="")
            spacer11.grid(row=5, column=0)
            #Delete the selected row in the table and in the database
            deleteButton3 = Button(bottomframe3, text="Delete", command=deleteLeaseForAll)
            deleteButton3.grid(row=6, column=3)
            #Update the selected row in the table and in the database
            updateButton3 = Button(bottomframe3, text="Update", command=updateLeaseForAll)
            updateButton3.grid(row=6, column=4)
            #Refresh the all row in the table
            refreshButton3 = Button(bottomframe3, text="Refresh", command=lambda:refreshTable(table3))
            refreshButton3.grid(row=6, column=5) 

            spacer12 = Label(bottomframe3, text="")
            spacer12.grid(row=7, column=3)
        #If usertype is manager or warden, it will display warning message they can't access this tab
        if user == "Manager" or user == "Warden": 
            allframe3 = Frame(tab3, highlightbackground="red",  highlightthickness=2,width=900,height=400)
            allframe3.pack(side=TOP, fill = BOTH, expand = True, padx=2, pady=2)
            #Warning red label
            warningLabel3 = Label(allframe3, text="You can't acess this tab! \n Only SuperStaff\n can acess this tab!", font=("Arial", 40),fg='red')
            warningLabel3.pack(pady=20)

    except con.Error as err:
        print("Failed to connect to the database", err)

    finally:
        if con:
            con.close()
            print("Connection closed")

    w3.mainloop()

#To check if user already exist on the database
def validation(uName, uPass):
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()

        print(uName.get()+" "+uPass.get())
      
        cur.execute('''SELECT * FROM users WHERE uname = ? AND passwd = ?''',(uName.get(),uPass.get()))
        if cur.fetchone():
            print("Log In Successfull!")

            w2 = Toplevel(w) 
            w2.title("Login Success")
            w2.geometry('200x200')
            spacer7 = Label(w2, text="")
            spacer7.grid(row=2, column=3)
            Button(w2, text="Home", command=systemWindow).grid(row=3, column=1, padx = 10, pady = 10)
            Button(w2, text="Log out", command=w2.destroy).grid(row=3, column=2, padx = 10, pady = 10)
            spacer8 = Label(w2, text="")
            spacer8.grid(row=4, column=5)
            Label(w2,text="Login is successful",fg='green').grid(row=6,column=1 ,padx = 10, pady = 10,sticky=E)
            Label(tab1,text="").grid(row=5,column=0)
            label = Label(tab1,text="Login is successful! \n User is found! \n Please Continue\n to the next window",fg='green').grid(row=6,column=1)

        else:
            Label(tab1,text="").grid(row=5,column=0)
            label2 = Label(tab1,text="Login failed!\n User is not found! \n or \n Wrong Password!",fg='red').grid(row=6,column=1)
            print("Log In Failed!")

    except con.Error as err:
        print("Operation is failed", err)
    finally:
        if con:
            con.close()
            print("Connection closed")
        
#To refresh the user type
def tabulate(tr):
    #Delete the existing item in the table
    for item in tr.get_children():
        tr.delete(item)
    #Connecting to the database and selecting all the data from the users table
    try:
        con = sqlite3.connect('staff.db')
        cur = con.cursor()
        i=1    
        for row in cur.execute("select * from users"):
            txt = "L"+str(i)
            i=i+1
            tr.insert("", 'end', text =txt, values =(row[1], row[3]))


    except con.Error as err:
        print("Operation is failed", err)
    finally:
        if con:
            con.close()
            print("Connection closed")
    return tr

#Creating all the table
createUsersTable()
createHalltable()
createStudentTable()
createRoomTable()
createLeaseTable()

#Main window
w = Tk()
w.title("UWE Bristol Accomodation System")
#Creating tabs
tabControl = ttk.Notebook(w)
#£ tabs for log in, register and user list
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

#Naming the tab
tabControl.add(tab1, text ='Login')
tabControl.add(tab2, text ='Register')
tabControl.add(tab3, text ='User List')
tabControl.pack(expand = 1, fill ="both")
#Setting the text variable as string variable from the entry boxes
uName = StringVar()
uPass = StringVar()
uType = StringVar()
uid = StringVar()

# Tab 1 development starts from here
userNameLabel = Label(tab1, text="User Name").grid(row=0, column=0, padx = 10, pady = 10)

userNameEntry = Entry(tab1, textvariable=uName).grid(row=0, column=1)  

passwordLabel = Label(tab1,text="Password").grid(row=1, column=0, padx = 10, pady = 10)  
passwordEntry = Entry(tab1, textvariable=uPass, show='*').grid(row=1, column=1)  
spacer8 = Label(tab1, text="")
spacer8.grid(row=2, column=1)
loginButton = Button(tab1, text="Login", command=lambda:validation(uName,uPass)).grid(row=4, column=1, sticky=W) 

#Tab 2 development starts from here
userNameLabel2 = Label(tab2, text="User Name:").grid(row=0,column=0, padx = 10, pady = 10)
userNameEntry2 = Entry(tab2, textvariable=uName).grid(row=0,column=1)

passwordLabel2 = Label(tab2, text="Password:").grid(row=1,column=0, padx = 10, pady = 10)
passwordEntry2 = Entry(tab2, textvariable=uPass, show='*').grid(row=1,column=1)

userIdLabel = Label(tab2, text="User Id:").grid(row=2,column=0, padx = 10, pady = 10)
userIdEntry = Entry(tab2, textvariable=uid).grid(row=2,column=1)

userTypeLabel = Label(tab2, text="User Type:").grid(row=3,column=0,  padx = 10, pady = 10)
uType.set("Select a value")
userTypeOption = OptionMenu(tab2, uType, "All", "Manager", "Warden").grid(row=3,column=1,  padx = 10, pady = 10)
#Data save to the database when condition is met
saveButton = Button(tab2,text="Save", command=lambda:save(uName, uPass, uType)).grid(row=4,column=0)

# Tab 3 bilt from this point
trv = ttk.Treeview(tab3,selectmode="browse")
trv.grid(row=0,column=1)

#Scrollbar
tableScroll4 = ttk.Scrollbar(tab3,orient ="vertical", command = trv.yview)
tableScroll4.grid(row=0,column=2)

trv.configure(xscrollcommand = tableScroll4.set)
 
#Defining number of columns
trv["columns"] = ("1", "2")
 
#Defining heading
trv['show'] = 'headings'
 
#Assigning the width and anchor to the respective columns
trv.column("1", width = 120, anchor ='c')
trv.column("2", width = 120, anchor ='c')

#Assigning the heading names to the respective columns
trv.heading("1", text ="User Name")
trv.heading("2", text ="User Type")
#Retrieveing data from users table and inserting into the treeview
trv = tabulate(trv)

#To insert data on the user list ---- newly added
Button(tab3, text="Refresh", command=lambda:tabulate(trv)).grid(row=4, column=1, sticky=E) 

w.mainloop()