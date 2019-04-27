from autorclass import Autor
import psycopg2

class AutorDao:
    def inserir(self,p):
        con = psycopg2.connect('host=localhost dbname=postgres user=postgres password=test123')
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM "Autor" WHERE cod=%s""", [p.cod])  
        lis = cur.fetchone()

        if(lis[0] == 0):
            try:
                with con.cursor() as cur:
                    p.cod = cur.execute("""INSERT INTO "Autor" (nome, email) VALUES (%s, %s) RETURNING cod""", [p.nome, p.email])
                    con.commit()
                    cur.close()
                    con.close()
            except:
                print("ERRO")
    
    def deletar(self,p):
        con = psycopg2.connect('host=localhost dbname=postgres user=postgres password=test123')
        cur = con.cursor()
        cur.execute('delete from "Autor" where cod = (%s)',[p])
        con.commit()
        con.close()
    
    def buscar(self,p):
        con = psycopg2.connect('host=localhost dbname=postgres user=postgres password=test123')
        cur = con.cursor()
        cur.execute('SELECT * FROM "Autor" where cod = (%s)',[p])
        con.commit()
        print(cur.fetchone())
        con.close()

    def listar():
        con = psycopg2.connect('host=localhost dbname=postgres user=postgres password=test123')
        cur = con.cursor()
        sql = 'select *from "Autor"'
        cur.execute(sql)
        for linha in cur.fetchall():
            print(linha)
        con.close() 

if __name__ == "__main__":
    d = AutorDao()
    d.listar()

        


