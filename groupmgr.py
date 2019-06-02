import random

import dbConnector
import uastudent

db = dbConnector.initDB();

def addGroupIDToDB(group_id, group_type):

    cursor = db.cursor()

    sql_insert_query = ( "INSERT INTO ce301.grouping "
                         "(group_id, group_type) "
                         "VALUES (%s,%s)")

    insertThis = (group_id, group_type)

    result = cursor.execute(sql_insert_query, insertThis)

    db.commit()
    print ('Record' + group_id + 'inserted successfully into table')

def add_group_member(group_id, member_id):

    cursor = db.cursor()

    sql_insert_query = ( "INSERT INTO ce301.grouping_member "
                         "(group_id, related_id) "
                         "VALUES (%s,%s)")


    insertThis = (group_id, member_id)

    result = cursor.execute(sql_insert_query, insertThis)

    db.commit()
    print ('Record' + member_id + 'inserted successfully into grouping member')


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def grouping_config():


    start_list = uastudent.currentAccounts;

    group_prefix= input("Enter group prefix: ")
    group_type= input("Enter group type: ")


    random.shuffle(start_list)

    i = 1;

    group_size = int(input("Enter group size: "))

    grouping = chunks(start_list, group_size)

    for group in grouping:

        #print("group:  " + group_prefix + i.__str__());
        group_id = group_prefix + i.__str__();

        addGroupIDToDB(group_id, group_type);

        i += 1;

        for student in group:
            add_group_member(group_id, student.user_id)
            print("group:  " + group_id + "  Member: " + student.last_name);



create_group = input("Do you wish to create a new grouping? (Y/N): ")

if create_group == "Y":
    grouping_config();
else:
    pass

