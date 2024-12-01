from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_mariadb_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='airport_db',
        user='dokyeom',
        password='seventeen17',
        autocommit=True,
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci'
    )

@app.route('/airport/<icao_code>')

def get_icao(icao_code):
    connection = get_mariadb_connection()
    sql = f"SELECT ident, name, municipality FROM airport_data WHERE ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()
    if result:
        response = {
            "ICAO": result["ident"],
            "Name": result["name"],
            "Location": result["municipality"]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)