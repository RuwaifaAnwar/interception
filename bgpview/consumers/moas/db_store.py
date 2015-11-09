import sqlite3

"""
Setting up database"""
conn = sqlite3.connect('test1.db')
c = conn.cursor()
#c.execute('''CREATE TABLE moas2 (prefix text, status int, list int, asn1 int, asn2 int, stime int, etime int)''')
#conn.commit()

#conn.close()


def insert_db(prefix,lists,asn,asn2,time):
        insert_str="INSERT into moas2 (prefix,list,asn1,asn2,status,stime) VALUES ('"+prefix+"',"+str(lists)+","+str(asn)+","+str(asn2)+",1 ,"+str(time)+");"

        c.execute(insert_str)
        conn.commit()

def update_moas_end():
    update_str="UPDATE moas2 SET etime="+str(time)+" where prefix = '"+prefix+"'  and asn1="+str(asn1)+"  and asn2= "+str(asn1)+" );"
    c.execute(update_str)
    conn.commit()
    

def select_db():
    select_st="select * from moas2"
    c.execute(select_st)
    for row in c.execute(select_st):
        print row

    

#insert_db('prefix','1','12','1','12312')
#select_db()