import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
#mycurser.execute("""create table gen_db ( seq_num int,strand varchar(50),length int,pid varchar(10) ,gene varchar(10),synonym varchar(10) ,code varchar(10) ,cog varchar(10),product varchar(50))""")
#conn.commit()
Location = ""
Strand = ""
Length = ""
PID = ""
Gene = ""
Synonym = ""
code = ""
COG = ""
Product = ""
seq_num = 1

file_location = "C://Users//Asus//AppData//Local//Programs//Python//Python37-32//GeneDetails.txt.txt"
file_1 = open(file_location, "r")
for line in file_1:
    ch = line.split("\t")
    #print(len(ch))
    if len(ch)!= 9:
        print("Description about the file")
    else:
        if ch[0]=="Location" or ch[1]=="Strand" or ch[2]=="Length" or ch[3]=="PID" or ch[4]=="Gene" or ch[5]=="Synonym" or ch[6]=="code" or ch[7]=="COG" or ch[8]== "Product":
            print("information about the field");
        else:
            #print(ch)
            #print(len(ch))
            Location = ch[0]
            #print(Location)
            Strand = ch[1]
            Length = ch[2]
            PID = ch[3]
            Gene = ch[4]
            Synonym = ch[5]
            Code = ch[6]
            COG = ch[7]
            Product = ch[8]
            sql_insert_query = """ INSERT INTO `gen_db` (`seq_num`,`strand`, `length`, `pid` ,`gene`,`synonym`,`code`,`cog`,`product`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            insert_tuple = (str(seq_num),Strand,Length,PID,Gene,Synonym,code,COG,Product)
            mycurser.execute( sql_insert_query,insert_tuple )
            seq_num = seq_num +1
conn.commit()
conn.close()
        
        
