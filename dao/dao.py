import mysql


class LibrettoDao:


    def getAllVoti(self):
        cnx = mysql.connector.connect(
            user = "root",
            password = "Leotokounmpo#34",
            host = "127.0.0.1",
            database = "libretto")

        cursor = cnx.cursor(dictionary=True)

        query = """select * from voti"""
        rs = cursor.execute(query)

        for row in rs:
            print(row)


        cnx.close()

if __name__ == "__main__":
    mydao = LibrettoDao()
    mydao.getAllVoti()
