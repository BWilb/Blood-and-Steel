import sys
import time

import pypyodbc


def initial_upload_to_database(nations):
    """initial upload to database function will upload to each and every database within database management directory"""
    foreign_records = []
    for i in range(0, len(nations)):
        foreign_records.append([nations[i].date.date(), nations[i].name, nations[i].stability,
                                nations[i].leader, nations[i].population, nations[i].births,
                                nations[i].deaths, nations[i].happiness, nations[i].current_gdp,
                                nations[i].national_debt,
                                nations[i].alliance])

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

    insert_statement = """
    INSERT INTO nations.Nation
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:

        # inserting data from AI nations and user nation
        for foreign_record in foreign_records:
            cursor.execute(insert_statement, foreign_record)
            print("hi")

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
        f = 1
        update_query = f"""UPDATE nations.Nation SET NationPopulation={nations[i].population},
        NationGDP={nations[i].current_gdp}, NationalDebt={nations[i].national_debt}, Births={nations[i].births},
        Deaths={nations[i].deaths}, NationStability={nations[i].stability},
        NationHappiness={nations[i].happiness}
        WHERE NationID={(i + 1)}"""
        try:
            cursor.execute(update_query)
            cursor.commit()
            print("updated_successfully")

        except Exception as e:
            print(e)
            print("unable to update")

        # cursor.close()


def retrieving_population(nations):
    pass


def retreiving_economy(nations):
    pass
