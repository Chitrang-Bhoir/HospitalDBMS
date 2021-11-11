from connector import c, hospital_db
from color import *
import mysql.connector

#query builder class
class queryBuilder(object):
    def __init__(self):

        #defining keywords
        self.exit = ['exit', 'e', 'quit', 'q']
        self.help = ['help', 'h']
        self.insert = ['insert', 'i']
        self.update = ['update', 'u']
        self.delete = ['delete', 'd']
        self.query = ['query', 'q']
        self.show = ['show', 's']
        self.tables = ['tables', 't']

    #get list of tables in the database
    def tablelist(self):

        #execute query
        c.execute('show tables;')

        #fetch entries
        rslt = c.fetchall()

        #build the list
        tables = []
        for table in rslt:
            tables.append(table[0])
        
        #return list
        return tables

    #print list of tables in the database
    def printTablelist(self, tables):
        print(f'{DATA}')
        for table in tables:
            print(table)
        print(f'{RESET}')

    #insert entry into the table    
    def insertData(self, table):

        #no error till now
        err = False

        #check table names
        if(table == 'patient'): #table is patient

            #input column values
            id = str(input(f'{REQUEST}id : {QUERY}'))
            name = str(input(f'{REQUEST}name : {QUERY}'))
            dob = str(input(f'{REQUEST}dob : {QUERY}'))
            contact_no = str(input(f'{REQUEST}contact_no : {QUERY}'))

            #build sql query
            sql = f'insert into patient values ("{id}", "{name}", "{dob}", "{contact_no}");'
        elif(table == 'department'):    #table is department

            #input column values
            name = str(input(f'{REQUEST}name : {QUERY}'))
            floor = str(input(f'{REQUEST}floor : {QUERY}'))

            #build sql query
            sql = f'insert into department values ("{name}", {floor});'
        elif(table == 'doctor'):    #table is doctor

            #input column values
            id = str(input(f'{REQUEST}id : {QUERY}'))
            name = str(input(f'{REQUEST}name : {QUERY}'))
            designation = str(input(f'{REQUEST}designation : {QUERY}'))
            contact_no = str(input(f'{REQUEST}contact_no : {QUERY}'))
            salary = str(input(f'{REQUEST}salary : {QUERY}'))
            department = str(input(f'{REQUEST}department : {QUERY}'))

            #build sql query
            sql = f'insert into doctor values ("{id}", "{name}", "{designation}", "{contact_no}", {salary}, "{department}");'
        elif(table == 'nurse'): #table is nurse

            #input column values
            id = str(input(f'{REQUEST}id : '))
            name = str(input(f'{REQUEST}name : '))
            contact_no = str(input(f'{REQUEST}contact_no : '))
            salary = str(input(f'{REQUEST}salary : '))

            #build sql query
            sql = f'insert into nurse values("{id}", "{name}", "{contact_no}", {salary});'
        elif(table == 'admission'): #table is admission

            #input column values
            patient_id = str(input(f'{REQUEST}patient_id : {QUERY}'))
            admission_date = str(input(f'{REQUEST}admission_date : {QUERY}'))
            discharge_date = str(input(f'{REQUEST}discharge_date : {QUERY}'))
            bed_no = str(input(f'{REQUEST}bed_no : {QUERY}'))
            total_fees = str(input(f'{REQUEST}total_fees : {QUERY}'))
            fees_paid = str(input(f'{REQUEST}fees_paid : {QUERY}'))

            #build sql query
            sql = f'insert into admission values ("{patient_id}", "{admission_date}", "{discharge_date}", {bed_no}, {total_fees}, {fees_paid});'
        elif(table == 'diagnosis'): #table is diagnosis

            #input column values
            patient_id = str(input(f'{REQUEST}patient_id : {QUERY}'))
            diagnosis = str(input(f'{REQUEST}diagnosis : {QUERY}'))
            doctor_id = str(input(f'{REQUEST}doctor_id : {QUERY}'))

            #build sql query
            sql = f'insert into diagnosis values ("{patient_id}", "{diagnosis}", "{doctor_id}");'
        elif(table == 'nurse_duty'):    #table is nurse_duty

            #input column values
            nurse_id = str(input(f'{REQUEST}nurse_id : {QUERY}'))
            bed_no = str(input(f'{REQUEST}bed_no : {QUERY}'))

            #build sql query
            sql = f'insert into nurse_duty values("{nurse_id}", {bed_no});'
        else:

            #error occured
            err = True
            print(f'{ERROR}Error message:{ERRORINFO} Table does not exist{RESET}')

        #execute query if no error
        if(not err):
            try:
                c.execute(sql)
                hospital_db.commit()
                print(f"{MESSAGE}Data inserted successfully!{RESET}")
            except mysql.connector.Error as sqlerr:
                print(f"{ERROR}Error code:{ERRORINFO}", sqlerr.errno)
                print(f"{ERROR}SQLSTATE value:{ERRORINFO}", sqlerr.sqlstate)
                print(f"{ERROR}Error message:{ERRORINFO}", sqlerr.msg)

    #print contents of the table
    def printTableData(self, table):
        str_row = ''
        print(f'{DATA}')
        for row in table:
            for data in row:
                str_row += str(data) + '\t\t'
            print(str_row)
            str_row = ''
        print(f'{RESET}')

    #get contents of the table
    def showTableData(self, table):

        #check if table exists
        if(table in self.tablelist()):  #exists

            #build query
            sql = f'select * from {table};'

            #executing query and printing the data
            try:
                c.execute(sql)
                rslt = c.fetchall()
                self.printTableData(rslt)
            except mysql.connector.Error as sqlerr:
                print(f"{ERROR}Error code:{ERRORINFO}", sqlerr.errno)
                print(f"{ERROR}SQLSTATE value:{ERRORINFO}", sqlerr.sqlstate)
                print(f"{ERROR}Error message:{ERRORINFO}", sqlerr.msg)
        else:   #does not exist -> ERROR
            print(f"{ERROR}Error message:{ERRORINFO} Table does not exist.{RESET}")

    #run query
    def runQuery(self, query):

        #make sql query words list
        query.remove(query[0])

        #set show according to the nature of query
        show = False
        if(query[0] in ['select', 'SELECT']):
            show = True
        
        #build query
        query = ' '.join(query)

        #execute the query and print the data if required
        try:
            c.execute(query)
            if(show):
                rslt = c.fetchall()
                self.printTableData(rslt)
            else:
                print(f'{MESSAGE}Query executed successfully!{RESET}')
        except mysql.connector.Error as sqlerr:
                print(f"{ERROR}Error code:{ERRORINFO}", sqlerr.errno)
                print(f"{ERROR}SQLSTATE value:{ERRORINFO}", sqlerr.sqlstate)
                print(f"{ERROR}Error message:{ERRORINFO}", sqlerr.msg)

    #delete entry from table
    def deleteData(self, table):

        #no error till now
        err = False

        #check table name
        if(table == 'patient'): #table is patient

            #input primary key
            id = str(input(f'{REQUEST}id : {QUERY}'))

            #build sql query
            sql = f'delete from {table} where id="{id}";'
        elif(table == 'department'):    #table is patient

            #input primary key
            name = str(input(f'{REQUEST}name : {QUERY}'))

            #build sql query
            sql = f'delete from {table} where name="{name}";'
        elif(table == 'doctor'):    #table is patient

            #input primary key
            id = str(input(f'{REQUEST}id : {QUERY}'))

            #build sql query
            sql = f'delete from {table} where id="{id}";'
        elif(table == 'nurse'): #table is patient

            #input primary key
            id = str(input(f'{REQUEST}id : {QUERY}'))

            #build sql query
            sql = f'delete from {table} where id="{id}";'
        elif(table == 'admission'): #table is patient

            #input primary key
            patient_id = str(input(f'{REQUEST}patient_id : {QUERY}'))
            admission_date = str(input(f'{REQUEST}admission_date : '))

            #build sql query
            sql = f'delete from {table} where patient_id="{patient_id}" and admission_date="{admission_date}";'
        elif(table == 'diagnosis'): #table is patient

            #input primary key
            patient_id = str(input(f'{REQUEST}patient_id : {QUERY}'))
            diagnosis = str(input(f'{REQUEST}diagnosis : {QUERY}'))

            #build sql query
            sql = f'delete from {table} where patient_id="{patient_id}" and diagnosis="{diagnosis}";'
        elif(table == 'nurse_duty'):    #table is patient

            #input primary key
            nurse_id = str(input(f'{REQUEST}nurse_id : {QUERY}'))
            bed_no = str(input(f'{REQUEST}bed_no : {QUERY}'))

            #build sql query
            sql = f'delete from {table} where nurse_id="{nurse_id}" and bed_no="{bed_no}";'
        else:

            #error occured
            err = True
            print(f'{ERROR}Error message:{ERRORINFO} Table does not exist{RESET}')

        #execute query if no error
        if(not err):
            try:
                c.execute(sql)
                hospital_db.commit()
                print(f"{MESSAGE}Data deleted successfully!{RESET}")
            except mysql.connector.Error as sqlerr:
                print(f"{ERROR}Error code:{ERRORINFO}", sqlerr.errno)
                print(f"{ERROR}SQLSTATE value:{ERRORINFO}", sqlerr.sqlstate)
                print(f"{ERROR}Error message:{ERRORINFO}", sqlerr.msg)

    def updateData(self, table):

        #no error till now
        err = False

        #check table names
        if(table == 'patient'): #table is patient

            #input primary key
            id = str(input(f'{REQUEST}id : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            sql = f'update {table} set {col}="{val}" where id="{id}";'
        elif(table == 'department'):    #table is department

            #input primary key
            name = str(input(f'{REQUEST}name : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            if(col == 'name'):
                sql = f'update {table} set {col}="{val}" where name="{name}";'
            else:
                sql = f'update {table} set {col}={val} where name="{name}";'
        elif(table == 'doctor'):    #table is doctor

            #input primary key
            id = str(input(f'{REQUEST}id : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            if(col != 'salary'):
                sql = f'update {table} set {col}="{val}" where id="{id}";'
            else:
                sql = f'update {table} set {col}={val} where id="{id}";'
        elif(table == 'nurse'): #table is nurse

            #input primary key
            id = str(input(f'{REQUEST}id : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            if(col != 'salary'):
                sql = f'update {table} set {col}="{val}" where id="{id}";'
            else:
                sql = f'update {table} set {col}={val} where id="{id}";'
        elif(table == 'admission'): #table is admission

            #input primary key
            patient_id = str(input(f'{REQUEST}patient_id : {QUERY}'))
            admission_date = str(input(f'{REQUEST}admission_date : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            if(col in ['patient_id', 'admission_date', 'discharge_date']):
                sql = f'update {table} set {col}="{val}" where patient_id="{patient_id}" and admission_date="{admission_date}";'
            else:
                sql = f'update {table} set {col}={val} where patient_id="{patient_id}" and admission_date="{admission_date}";'
        elif(table == 'diagnosis'): #table is diagnosis

            #input primary key
            patient_id = str(input(f'{REQUEST}patient_id : {QUERY}'))
            diagnosis = str(input(f'{REQUEST}diagnosis : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            sql = f'update {table} set {col}="{val}" where patient_id="{patient_id}" and diagnosis="{diagnosis}";'
        elif(table == 'nurse_duty'):    #table is nurse_duty

            #input primary key
            nurse_id = str(input(f'{REQUEST}nurse_id : {QUERY}'))
            bed_no = str(input(f'{REQUEST}bed_no : {QUERY}'))

            #input column name
            col = str(input(f'{REQUEST}column to be updated : {QUERY}'))

            #input new value
            val = str(input(f'{REQUEST}new value : {QUERY}'))

            #build sql query
            if(col != 'bed_no'):
                sql = f'update {table} set {col}="{val}" where nurse_id="{nurse_id}" and bed_no="{bed_no}";'
            else:
                sql = f'update {table} set {col}={val} where nurse_id="{nurse_id}" and bed_no="{bed_no}";'
        else:

            #error occured
            err = True
            print(f'{ERROR}Error message:{ERRORINFO} Table does not exist{RESET}')

        #execute query if no error
        if(not err):
            try:
                c.execute(sql)
                hospital_db.commit()
                print(f"{MESSAGE}Data updated successfully!{RESET}")
            except mysql.connector.Error as sqlerr:
                print(f"{ERROR}Error code:{ERRORINFO}", sqlerr.errno)
                print(f"{ERROR}SQLSTATE value:{ERRORINFO}", sqlerr.sqlstate)
                print(f"{ERROR}Error message:{ERRORINFO}", sqlerr.msg)