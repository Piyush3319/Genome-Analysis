import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
# mycurser.execute("""create table Eco_db ( seq_num int ,gen_desc varchar(50),atgc_length int,a_length int ,t_length int ,g_length int ,c_length int ,gc_per double)""")
# conn.commit()
seq_num = 1
atgc_seq = ""
count=0
ch = ""
triplet = ""
fin_prot = ""
file_1 = open("upload.txt", "r")
for line in file_1:
    if line == "\n":
        print("blank line")
    else:
        ch = line.split("\t")
        atgc_seq = ch[2]
        for char in atgc_seq:
            triplet = triplet + char
            count = count +1
            if count == 3:
                print(triplet,end = "\t")
                count = 0
                triplet = ""
            
            
