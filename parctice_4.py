import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
#mycurser.execute("""create table protien_db ( seq_num int , protien_seq varchar(3000),stop_codon int )""")
#conn.commit()
amino_acid ={'ATT':'I','ATC':'I','ATA':'I','CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TTT':'F','TTC':'F','ATG':'M','TGT':'C','TGC':'C','GCT':'A','GCC':'A','GCA':'A','GCA':'A','GCG':'A','GGT':'G','GGC':'G','GGA':'G','GGG':'G','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','TCT':'S','TCC':'S','TCA':'S','TCG':'S','AGT':'S','AGC':'T','TAT':'Y','TAC':'Y','TGG':'W','CAA':'Q','CAG':'Q','ATT':'N','AAC':'N','CAT':'H','CAC':'H','GAA':'E','CAC':'E','GAT':'D','GAC':'D','AAA':'K','AAG':'K','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R','TAA':'STOP','TAG':'STOP','TGA':'STOP'}
count = 0
stop_count = 0
triplet = ""
protien_seq = ""
final_atgc_seq = ""
seq_num = 1
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
            if char != '\n':
                final_atgc_seq = final_atgc_seq + char
        #print(final_atgc_seq)
        #print("length of atgc_seq : - ",len(final_atgc_seq))
        #print(atgc_seq)
        #print("....................................Next record sequence................................")
        #print("........................next record atgc triplet...............................")
        for char in final_atgc_seq:
            count = count + 1
            triplet = triplet + char
            if count == 3:
                #print(triplet,end = "\t")
                if triplet in amino_acid:
                    if amino_acid.get(triplet) == "STOP":
                        print("stop codon is found")
                        stop_count = stop_count + 1
                    else:
                        protien_seq = protien_seq + amino_acid.get(triplet)
                #print(protien_seq)
                triplet = ""
                count = 0
       # print(".............................................IT'S PROTIEN SEQUENCE IS .......................................................")
        #print(protien_seq,"\t",len(protien_seq))
        sql_insert_query = """ INSERT INTO `protien_db` (`seq_num`, `protien_seq`,`stop_codon`) VALUES (%s,%s,%s)"""
        insert_tuple = (seq_num,protien_seq,stop_count)
        mycurser.execute( sql_insert_query,insert_tuple )
        seq_num = seq_num + 1
        #print("\n\n\n")
        protien_seq = ""
        triplet = ""
        count = 0
        stop_count = 0
        final_atgc_seq = ""
conn.commit()
conn.close()
