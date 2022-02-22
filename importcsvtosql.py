import MySQLdb
import csv

mydb=MySQLdb.connect(host="127.0.0.1", user="root", password="", database="testeA1")

with open("itens.csv", newline='') as csvfile: #with open pq ele fecha sozinho o arquivo apos o uso
    rows = csv.reader(csvfile, delimiter=';')#definindo o limitador que separa
    all_value=[]

    for row in rows:#percorrer todas as linhas
        value=(row[0],row[1],row[2],row[3],row[4],row[5],row[6])#definindo qual o valor para as separacoes
        all_value.append(value)#obtendo valor

query="insert into 'tbl_testetabela'('group id','material id',ítem qty','item_dim1','item_dim2','item_dim3','item_class') values (%i,%i,%f,%s,%s,%s,%s)"

mycursor = mydb.cursor()#o que percorre na tabela
mycursor.executemany(query, all_value)
mydb.commit()

