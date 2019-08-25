import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
mycurser.execute("""create table final_database(gen_desc varchar(50),atgc_length int,a_length int,t_length int,g_length int,c_length int,gc_per double,strand varchar(50),length int,pid varchar(10),gene varchar(10),synonym varchar(10),code varchar(10),cog varchar(10),product varchar(50),protien_seq varchar(3000),Nc_value varchar(50))""")
conn.commit()
my_query = "select final_db.gen_desc,final_db.atgc_length,final_db.a_length,final_db.t_length,final_db.g_length,final_db.c_length,final_db.gc_per,final_db.strand,final_db.length,final_db.pid,final_db.gene,final_db.synonym,final_db.code,final_db.cog,final_db.product,protien_dbtest.protien_seq,protien_dbtest.Nc from final_db JOIN protien_dbtest ON protien_dbtest.seq_num = final_db.seq_num"
mycurser.execute(my_query)
data = mycurser.fetchall()
for row in data:
    #print(row)
    gen_desc = row[0]
    #print(gen_desc)
    atgc_length = row[1]
    #print(atgc_length)
    a_count = row[2]
    #print(a_count)
    t_count = row[3]
    #print(t_count)
    g_count = row[4]
    #print(g_count)
    c_count = row[5]
    #print(c_count)
    gc_per = row[6]
    #print(gc_per)
    strand = row[7]
    #print(strand)
    length = row[8]
    #print(length)
    pid = row[9]
    #print(pid)
    gene = row[10]
    #print(gene)
    synonym = row[11]
    #print(synonym)
    code = row[12]
    #print(code)
    cog = row[13]
    #print(cog)
    product = row[14]
    #print(product)
    protien_seq = row[15]
    #print(protien_seq)
    Nc_values = row[16]
    #print(Nc_values)
    sql_insert_query = """ INSERT INTO `final_database` (`gen_desc`,`atgc_length`, `a_length` ,`t_length`,`g_length`,`c_length`,`gc_per`,`strand`,`length`,`pid`,`gene`,`synonym`,`code`,`cog`,`product`,`protien_seq`,`Nc_value`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    insert_tuple = (gen_desc,atgc_length,a_count,t_count,g_count,c_count,gc_per,strand,length,pid,gene,synonym,code,cog,product,protien_seq,Nc_values)
    mycurser.execute( sql_insert_query,insert_tuple )
conn.commit()
conn.close()
    
