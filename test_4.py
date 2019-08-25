import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
mycurser.execute("""create table final_db (seq_num int,gen_desc varchar(50),atgc_length int,a_length int ,t_length int ,g_length int ,c_length int ,gc_per double,strand varchar(50),length int,pid varchar(10) ,gene varchar(10),synonym varchar(10) ,code varchar(10) ,cog varchar(10),product varchar(50))""")
conn.commit()
seq_num = 1
my_query = "select eco_db.gen_desc,eco_db.atgc_length,eco_db.a_length,eco_db.t_length,eco_db.g_length,eco_db.c_length,eco_db.gc_per,gen_db.strand,gen_db.length,gen_db.pid,gen_db.gene,gen_db.synonym,gen_db.code,gen_db.cog,gen_db.product from gen_db JOIN eco_db ON gen_db.seq_num = eco_db.seq_num"
mycurser.execute(my_query)
data = mycurser.fetchall()
for row in data:
    gen_desc = row[0]
    atgc_length = row[1]
    a_count = row[2]
    t_count = row[3]
    g_count = row[4]
    c_count = row[5]
    gc_per = row[6]
    strand = row[7]
    length = row[8]
    pid = row[9]
    gene = row[10]
    synonym = row[11]
    code = row[12]
    cog = row[13]
    product = row[14]
    sql_insert_query = """ INSERT INTO `final_db` (`seq_num`,`gen_desc`,`atgc_length`, `a_length` ,`t_length`,`g_length`,`c_length`,`gc_per`,`strand`,`length`,`pid`,`gene`,`synonym`,`code`,`cog`,`product`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    insert_tuple = (seq_num,gen_desc,atgc_length,a_count,t_count,g_count,c_count,gc_per,strand,length,pid,gene,synonym,code,cog,product)
    mycurser.execute( sql_insert_query,insert_tuple )
    seq_num = seq_num + 1
conn.commit()
conn.close()
    
