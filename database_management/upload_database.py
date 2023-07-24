import sys
import time

import pypyodbc

def initial_upload_to_database(nations):
    foreign_records = []
    for i in range(0, len(nations)):
        foreign_records.append([(i + 1), nations[i].date.date(), nations[i].name, nations[i].population,
                                round(nations[i].current_gdp, 2),
                                round(nations[i].national_debt, 2), nations[i].leader,
                                nations[i].stability, nations[i].happiness, nations[i].alliance])
    DRIVER = "SQL Server"
    SERVER_NAME = "VWNC71429\MSSQLSERVER01"
    DATABASE_NAME = "Capstone"

    connection = f"""Driver={{{DRIVER}}};
                    Server={SERVER_NAME};
                    Database={DATABASE_NAME};
                    Trust_Connection=yes;
    """
    try:
        conn = pypyodbc.connect(connection)
        print('connection is successful')
    except Exception as e:
        print(e)
        print("task is terminated")
        sys.exit()
    else:
        cursor = conn.cursor()

    insert_statement = """
    INSERT INTO nations.Nation
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:

        # inserting data from AI nations and user nation
        for foreign_record in foreign_records:
            cursor.execute(insert_statement, foreign_record)

    except Exception as e:
        cursor.rollback()
        print(e.value)
        print("Failed to push to database")
    else:
        print("records inserted successfully")
        cursor.commit()
    finally:
        if conn.connected == 1:
            print("connection closed")
            #conn.close()

def update_database_info(nations):
    DRIVER = "SQL Server"
    SERVER_NAME = "VWNC71429\MSSQLSERVER01"
    DATABASE_NAME = "Capstone"

    connection = f"""Driver={{{DRIVER}}};
                        Server={SERVER_NAME};
                        Database={DATABASE_NAME};
                        Trust_Connection=yes;
        """

    try:
        conn = pypyodbc.connect(connection)
        #print('connection is successful')
    except Exception as e:
        print(e)
        print("task is terminated")
        sys.exit()
    else:
        cursor = conn.cursor()

    for i in range(0, (len(nations))):
        f = 1
        update_query = f"""UPDATE nations.Nation SET NationPopulation={nations[i].population},
        NationGDP={nations[i].current_gdp}, NationalDebt={nations[i].national_debt} 
        WHERE NationID={(i + 1)}"""
        try:
            cursor.execute(update_query)
            cursor.commit()
            print("updated_successfully")

        except Exception as e:
            print(e)
            print("unable to update")

        #cursor.close()
        time.sleep(1.5)