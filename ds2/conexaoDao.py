import psycopg2

class conexaoDao():
    def connect(self): 
        banco = "dbname=postgres user=postgres password=test123 host=localhost port=5432"
        return psycopg2.connect(banco)