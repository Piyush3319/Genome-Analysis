import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
mycurser.execute("""create table gen_db ( gen_desc varchar(50),atgc_length int,a_length int ,t_length int ,g_length int ,c_length int ,gc_per double)""")
conn.commit()
print(mycurser)
A_char = 0
T_char = 0
G_char = 0
C_char = 0
GC_per = 0
gen_desc = ""
final_desc = ""
seq_len = 0
file_1 = open("upload.txt", "r")
for line in file_1:    
    for char in line:
        if char == "A":
            A_char = A_char + 1
        elif char == "T":
            T_char = T_char + 1
        elif char == "G":
            G_char = G_char + 1
        elif char == "C":
            C_char = C_char + 1
        else:
            if (char != 'A' or char != 'T' or char != 'G' or char != 'C'):
                gen_desc = gen_desc + char
    seq_len = (A_char + T_char + G_char + C_char) - 1
    #print(gen_desc)
    ch=gen_desc.split(" ")
    temp=ch[0].split("\t")
    #print(temp[len(temp)-1])
    final_desc=temp[len(temp)-1]
    #print("The Genome Description is  :", final_desc)
    gen_desc = ""
    try:
        GC_per = (G_char + C_char) / seq_len * 100
    except ZeroDivisionError:
        print("")
    sql_insert_query = """ INSERT INTO `gen_db` (`gen_desc`, `atgc_length`, `a_length` ,`t_length`,`g_length`,`c_length`,`gc_per`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    insert_tuple = (final_desc,str(seq_len),str(A_char),str(T_char),str(G_char),str(C_char),str(GC_per))
    mycurser.execute( sql_insert_query,insert_tuple )
conn.commit()
conn.close()

