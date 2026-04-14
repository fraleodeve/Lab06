from database.DB_connect import DBConnect
from model.prodotti import Prodotti
from model.rivenditori import Rivenditori
from model.vendite import Vendite


class DAO():

    #def __init__(self):
        #pass

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select distinct year(Date)
                    from go_daily_sales"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["year(Date)"])

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getVendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select *
                    from go_daily_sales"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Vendite(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getProdotti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select *
                    from go_products"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Prodotti(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getRivenditori():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select *
                    from go_retailers"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Rivenditori(**row))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getTopVendite(anno, brand, rivenditore):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select gds.Retailer_code, gds.Product_number, gds.`Date`, gds.Quantity * gds.Unit_sale_price as n
                    from go_daily_sales gds
                    where gds.Retailer_code = %s and gds.Product_number = %s and year(gds.`Date`) = %s """
        cursor.execute(query, (anno, brand, rivenditore))

        res = []
        for row in cursor:
            res.append((Vendite(
                Retailer_code = row["Retailer_code"],
                Product_number = row["Product_number"],
                Date = row["Date"],
            ), row["n"]))

        cursor.close()
        cnx.close()

        return res

