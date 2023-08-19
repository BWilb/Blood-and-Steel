import sys
import time

import pypyodbc


def initial_upload_to_database(nations):
    """initial upload to database function will upload to each and every database within database management directory"""
    foreign_records = []
    # establishment of national records, including the nation of the player
    for i in range(0, len(nations)):
        foreign_records.append([nations[i].date.date(), nations[i].name, nations[i].stability, nations[i].leader,
                                nations[i].population, nations[i].births, nations[i].deaths, nations[i].happiness,
                                nations[i].current_gdp, nations[i].national_debt, nations[i].alliance])

    DRIVER = "SQL Server"
    SERVER_NAME = "VWNC71429\MSSQLSERVER01"
    DATABASE_NAME = "Capstone"

    connection = f"""Driver={{{DRIVER}}};
                    Server={SERVER_NAME};
                    Database={DATABASE_NAME};
                    Trust_Connection=yes;
    """
    # inserting
    try:
        conn = pypyodbc.connect(connection)
        print('connection is successful')
    except Exception as e:
        print(e)
        print("task is terminated")
        sys.exit()
    else:
        cursor = conn.cursor()

    recreating_db = """
    USE Capstone
    IF OBJECT_ID('nations.Nation', 'U') IS NOT NULL
        DROP TABLE nations.Nation
    
    CREATE TABLE nations.Nation
        (NationID int primary key IDENTITY(1, 1) NOT NULL,
        CurrentDate date NOT NULL,
        NationName varchar(35) NOT NULL,
        NationStability FLOAT NOT NULL,
        NationLeader VARCHAR(35) NOT NULL,
        NationPopulation int NOT NULL,
        Births INT NOT NULL,
        Deaths INT NOT NULL,
        NationHappiness FLOAT NOT NULL,
        NationGDP float NOT NULL,
        NationalDebt float NOT NULL,
        NationalAlliance varchar(20) NOT NULL
        )
    """
    """instead of continually recreating database in MSSQL when you need to manipulate the DB, 
    the code recreates it at the beginning"""
    try:
        cursor.execute(recreating_db)
    except Exception as e:
        cursor.rollback()
        print(e.value)
        print("Failed to push to database")

    else:
        print("database successfully recreated")
        cursor.commit()
    finally:
        if conn.connected == 1:
            print("connection closed")
            # conn.close()

    insert_statement = """
    INSERT INTO nations.Nation
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            # conn.close()


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
        # print('connection is successful')
    except Exception as e:
        print(e)
        print("task is terminated")
        sys.exit()
    else:
        cursor = conn.cursor()

    for i in range(0, (len(nations))):
        update_query = f"""UPDATE nations.Nation SET NationPopulation={nations[i].population},
        NationGDP={nations[i].current_gdp}, NationalDebt={nations[i].national_debt}, Births={nations[i].births},
        Deaths={nations[i].deaths}, NationStability={nations[i].stability},
        NationHappiness={nations[i].happiness}
        WHERE NationID={(i + 1)}"""
        try:
            cursor.execute(update_query)
            cursor.commit()

        except Exception as e:
            print(e)
            print("unable to update")

        # cursor.close()
