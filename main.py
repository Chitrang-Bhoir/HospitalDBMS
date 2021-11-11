from queryBuilder import queryBuilder
from color import *

if __name__ == '__main__':

    #query builder object
    qb = queryBuilder()

    #list of tables in database
    tables = qb.tablelist()

    #print headers
    print(f"{TITLE}~~~~~~~~~~~~~~~~~~~~HOSPITAL DATABASE MANAGEMENT SYSTEM~~~~~~~~~~~~~~~~~~~~{RESET}")
    print(f"{MANUAL}Type h for help{RESET}")

    #infinite loop
    while True:

        #input query from user
        query = str(input(f"{BULLET}>>> {QUERY}"))

        #check query cases
        if(query in qb.exit):   #exit
            print(f'{RESET}')
            break
        elif(query in qb.help): #print manual
            print(f"{MANUAL}~~~~~~~~~~~~~~~~~~~~~~~~~MANUAL~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}")
            print(f"{BULLET}▣{MANUAL}  To insert an entry     :   insert|i <table-name>{RESET}")
            print(f"{BULLET}▣{MANUAL}  To update an entry     :   update|u <table-name>{RESET}")
            print(f"{BULLET}▣{MANUAL}  To delete an entry     :   delete|d <table-name>{RESET}")
            print(f"{BULLET}▣{MANUAL}  To print table names   :   tables|t{RESET}")
            print(f"{BULLET}▣{MANUAL}  To print table content :   show|s <table-name>{RESET}")
            print(f"{BULLET}▣{MANUAL}  To enter an SQL query  :   query|q <query>{RESET}")
            print(f"{BULLET}▣{MANUAL}  To print the manual    :   help|h{RESET}")
            print(f"{BULLET}▣{MANUAL}  To exit the program    :   exit|e|quit|q{RESET}")
        elif(query in qb.tables):   #print table names
            qb.printTablelist(tables)
        elif(len(query.split(' ')) == 2):   #query has 2 words

            #splitting every word
            query = query.split(' ')

            #check cases for first word
            if(query[0] in qb.insert):  #insert entry
                qb.insertData(query[1])
            elif(query[0] in qb.update):    #update data
                qb.updateData(query[1])
            elif(query[0] in qb.delete):    #delete entry
                qb.deleteData(query[1])
            elif(query[0] in qb.show):  #show contents of table
                qb.showTableData(query[1])
        else:   #other cases

            #split every word
            query = query.split(' ')

            if(query[0] in qb.query):   #SQL query
                qb.runQuery(query)
            else:   #other cases -> ERROR
                print(f'{ERROR}Error message:{ERRORINFO} Invalid Query.{RESET}')            