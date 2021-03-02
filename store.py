########## IMPORTS ##############
import mysql.connector
from datetime import datetime

########## MYSQL CONNECTOR ##############

try:
    mydb = mysql.connector.connect(
        user="root", passwd="root", host="localhost", database="primes",  auth_plugin = 'mysql_native_password',
    )
    mycursor = mydb.cursor()
except Exception as e:
    print(e)
########## INJECTOR FUNCTION ##############

def injectDb(range, time_elapsed, algorithm,count):
    timestamp = datetime.now()
    lowerLimit = range[0]
    upperimit = range[1]

    try:
        sql = "INSERT INTO master (timestamp, lower_limit, upper_limit, time_elapsed, algo, count) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (timestamp, lowerLimit, upperimit, time_elapsed, algorithm, count)
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print(e)
        return None
    except IndexError:
        print ("MySQL Error: %s",str(e))
        return None
    except TypeError as e:
        print(e)
        return None
    except ValueError as e:
        print(e)
        return None

