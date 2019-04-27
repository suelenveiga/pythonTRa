import psycopg2

con = psycopg2.connect('host=localhost dbname=postgres user=postgres password=test123')
cur = con.cursor()
#listar limit ofsset se tiver se tiver com id alterar, se não tiver criar 
#sql = "select *from alunos"
#cur.execute(sql)
#for linha in cur.fetchall():
    #print(linha)

#con.close() 
#inserir
cur.execute('insert into "Autor" (nome, email) values (%s,%s)',["guilherme","gyih"])
con.commit()

#alterar
#cur.execute("update alunos set aluno = %s  where id = (%s)",["lorrana",3])
#con.commit()

#deletar 
#cur.execute("delete from alunos where id = (%s)",[3])
#con.commit()
#buscar 

#buscar
#cur.execute('SELECT * FROM "Autor"') 
#con.commit()
print(cur.fetchone())

con.close() 
