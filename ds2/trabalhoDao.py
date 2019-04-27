from trabalhoclass import Trabalho
import psycopg2

class TrabalhoDao:
    def inserir(self,p):
        con = psycopg2.connect('host=localhost dbname=postgres user=postgres password=test123')
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) FROM "Trabalho" WHERE cod=%s""", [p.cod])  
        test = cur.fetchone()

        if(test[0] == 0):
            try:
                with con.cursor() as cur:
                    cur.execute("""INSERT INTO "Trabalho" (conteudo, nota, "dataEntrega", titulo, "dataHoraAtualizacao") VALUES (%s, %s, %s, %s, %s) RETURNING cod""", [p.conteudo, p.nota, p.dataEntrega, p.titulo, p.dataHoraAtualizacao])
                    con.commit()
                    p.cod = cur.fetchone()
                    cur.execute("""INSERT INTO "TrabalhoAutor" ("codAutor", "codTrabalho") VALUES (%s, %s)""",(codAutor, p.cod[0]))
                    con.commit()
                    cur.close()
                    con.close()
            except:
                print("Deu Ruim")
    
if __name__ == "__main__":
    d = TrabalhoDao()
    p=Trabalho('aaa',3,12/12/12,'dfs')
    d.inserir(p)