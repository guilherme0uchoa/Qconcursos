import sqlite3

conn = sqlite3.connect(r'Q_DB.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS acertos (id INTEGER, gabarito CHAR(1), resposta CHAR(1))')
cursor.execute('CREATE TABLE IF NOT EXISTS total (id INTEGER, gabarito CHAR(1), resposta CHAR(1))')



def data_entry(questao,gabarito,resposta):
    cursor.execute('INSERT INTO acertos VALUES (?,?,?)',(questao,gabarito,resposta))

    conn.commit()

def data_entry_total(questao,gabarito,resposta):
    cursor.execute('INSERT INTO total VALUES (?,?,?)',(questao,gabarito,resposta))

    conn.commit()


#consulta

sql = "SELECT * FROM acertos WHERE id=?"

def read_data(word):
    for row in cursor.execute(sql,(word,)):
        return row[0]

sql1 = "SELECT * FROM total WHERE id=?"

def read_datat(word):
    for row in cursor.execute(sql1,(word,)):
        return row[0]


contar = "SELECT COUNT (rowid) FROM total WHERE rowid"

def total_data_total():
    for i in cursor.execute(contar):
        return int (i[-1])

contar_acertos = "SELECT COUNT (rowid) FROM acertos WHERE rowid"

def total_data_acertos():
    for i in cursor.execute(contar_acertos):
        return int (i[-1])
