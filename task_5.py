import pymysql
#conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
#mycurser = conn.cursor()
#mycurser.execute("""create table protien_db ( seq_num int , protien_seq varchar(3000),stop_codon int )""")
#conn.commit()
amino_acid ={'ATT':'I','ATC':'I','ATA':'I','CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TTT':'F','TTC':'F','ATG':'M','TGT':'C','TGC':'C','GCT':'A','GCC':'A','GCA':'A','GCA':'A','GCG':'A','GGT':'G','GGC':'G','GGA':'G','GGG':'G','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','TCT':'S','TCC':'S','TCA':'S','TCG':'S','AGT':'S','AGC':'T','TAT':'Y','TAC':'Y','TGG':'W','CAA':'Q','CAG':'Q','ATT':'N','AAC':'N','CAT':'H','CAC':'H','GAA':'E','CAC':'E','GAT':'D','GAC':'D','AAA':'K','AAG':'K','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R','TAA':'STOP','TAG':'STOP','TGA':'STOP'}
count = 0
icount=0
lcount=0
vcount=0
fcount=0
mcount=0
ccount=0
acount = 0
gcount =0
pcount=0
tcount=0
scount=0
ycount=0
wcount=0
qcount=0
ncount=0
hcount=0
ecount=0
dcount=0
kcount=0
rcount=0
stopcount =0
totel_codons = 0
stop_count = 0
nc_value= 0.0
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
        print(atgc_seq)
        #print("....................................Next record sequence................................")
        print("........................protein counts...............................")
        for char in final_atgc_seq:
            count = count + 1
            triplet = triplet + char
            if count == 3:
                #print(triplet,end = "\t")
                if triplet in amino_acid:
                    if amino_acid.get(triplet)=='I':
                        icount = icount +1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet)== 'L':
                        lcount = lcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet)== 'V':
                        vcount = vcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet)=='F':
                        fcount = fcount +1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'M':
                        mcount = mcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet)== 'C':
                        ccount = ccount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'A':
                        acount = acount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'G':
                        gcount = gcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'P':
                        gcount = gcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'T':
                        tcount = tcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'S':
                        scount = scount +1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'Y':
                         ycount = ycount +1
                         protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'W':
                        wcount = wcount +1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'Q':
                        qcount = qcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'N':
                        ncount = ncount +1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'H':
                        hcount = hcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'E':
                        ecount = ecount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'D':
                        dcount == dcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet)== 'K':
                        kcount = kcount + 1
                        protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == 'R':
                         rcount = rcount + 1
                         protien_seq = protien_seq + amino_acid.get(triplet)
                    if amino_acid.get(triplet) == "STOP":
                        stopcount = stopcount + 1
                        print("Stop Codon is found")
                        
                #print(protien_seq)
                triplet = ""
                count = 0
                
        #print(".............................................IT'S PROTIEN SEQUENCE IS .......................................................")
        #print(protien_seq,"\t",len(protien_seq))
        #sql_insert_query = """ INSERT INTO `protien_db` (`seq_num`, `protien_seq`,`stop_codon`) VALUES (%s,%s,%s)"""
        #insert_tuple = (seq_num,protien_seq,stop_count)
        #mycurser.execute( sql_insert_query,insert_tuple )
        totel_codon = (icount + lcount + vcount + fcount + mcount + ccount + acount + gcount + pcount + tcount + scount + ycount + wcount + qcount + ncount + hcount + ecount + dcount + kcount + rcount + stop_count)
        #nc_value = 
        seq_num = seq_num + 1
        #print("\n\n\n")
        print(icount,lcount,vcount,fcount,mcount,ccount,acount,gcount, pcount,tcount,scount,ycount,wcount,qcount,ncount,hcount,ecount,dcount,kcount,rcount,stopcount)
        protien_seq = ""
        triplet = ""
        count = 0
        stop_count = 0
        final_atgc_seq = ""
        icount=0
        lcount=0
        vcount=0
        fcount=0
        mcount=0
        ccount=0
        acoun=0
        gcount =0
        pcount=0
        tcount=0
        scount=0
        ycount=0
        wcount=0
        qcount=0
        ncount=0
        hcount=0
        ecount=0
        dcount=0
        kcount=0
        rcount=0
        stopcount=0
conn.commit()
conn.close()
