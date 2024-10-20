import mysql.connector
from geopy.distance import geodesic


def get_icao(icao_code):
    sql = f"SELECT airport.ident, airport.name, country.name FROM airport, country WHERE airport.ident = '{icao_code}' and airport.iso_country = country.iso_country"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
    return

def get_area_code(country_code):
    sql1 = f"SELECT airport.name, airport.type FROM airport, country WHERE country.iso_country = '{country_code}' and airport.iso_country = country.iso_country ORDER BY airport.type ASC"
    cursor = connection.cursor()
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    for a in result1:
        print(a)
    return

def get_icao_and_degree(icao_degree_code):
    sql2 = f"SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{icao_degree_code}'"
    cursor = connection.cursor()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    print(result2[0])
    return result2[0]

connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='dokyeom',
        password='seventeen17',
        autocommit=True,
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci'
)

#8.1
print("Exercise 8.1")
input_code = input("Enter the ICAO code of an airport: ")
get_icao(input_code)

#8.2
print("Exercise 8.2")
input_country_code = input("Enter the area code: ")
get_area_code(input_country_code)

#8.3
print("Exercise 8.3")

input_code_1 = input("Enter the ICAO code of first airport: ")
airport_1 = get_icao_and_degree(input_code_1)

input_code_2 = input("Enter the ICAO code of second airport: ")
airport_2 = get_icao_and_degree(input_code_2)

from geopy import distance
from geopy.distance import geodesic

degree_1 = (airport_1[2], airport_1[3])
degree_2 = (airport_2[2], airport_2[3])

distance = geodesic(degree_1, degree_2).kilometers
print(f"Distance between these two airports is {distance:.4f} km")


