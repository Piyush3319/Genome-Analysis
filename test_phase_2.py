import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
mycurser.execute("""create table Eco_db ( seq_num int ,gen_desc varchar(50),atgc_length int,a_length int ,t_length int ,g_length int ,c_length int ,gc_per double)""")
conn.commit()
seq_num = 1
gen_desc = ""
atgc_seq = ""
final_desc = ""
A_char = 0
T_char = 0
G_char = 0
C_char = 0
seq_len = 0
gc_per = "" 
ch = ""
file_1 = open("upload.txt", "r")
for line in file_1:
    if line == "\n":
        print("blank line")
    else:
        ch = line.split("\t")
        #print(len(ch))
        gen_desc = ch[1]
        temp1 = gen_desc.split(" ")
        temp=temp1[0].split("\t")
        #print(temp[len(temp)-1])
        final_desc=temp[len(temp)-1]
        #print(final_desc)
        atgc_seq = ch[2]
        for char in atgc_seq:
            if char == "A":
                A_char = A_char + 1
            elif char == "T":
                T_char = T_char + 1
            elif char == "G":
                G_char = G_char + 1
            elif char == "C":
                C_char = C_char + 1
        #print(seq_num,"\t",gen_desc,"\t",atgc_seq)
        #print("......................................Dtails : - A_count , T_count ,G_count and C_count......................................")
        seq_len = (A_char + T_char + G_char + C_char)
        gc_per = ((G_char + C_char)/seq_len) * 100
        #print(seq_len)
        #print(A_char,"\t",T_char,"\t",G_char,"\t",C_char,"\t",seq_len,"\t",gc_per)
        sql_insert_query = """ INSERT INTO `eco_db` (`seq_num`,`gen_desc`, `atgc_length`, `a_length` ,`t_length`,`g_length`,`c_length`,`gc_per`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        insert_tuple = (str(seq_num),final_desc,seq_len,A_char,T_char,G_char,C_char,gc_per)
        mycurser.execute( sql_insert_query,insert_tuple )
        A_char=0
        T_char=0
        G_char=0
        C_char=0
        seq_len=0
        gc_per = ""
        seq_num =seq_num + 1
conn.commit()
conn.close()
        
        

