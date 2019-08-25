import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd='', db='ecoli_database')
mycurser = conn.cursor()
#mycurser.execute("""create table protien_dbtest ( seq_num int , protien_seq varchar(3000),Nc double )""")
conn.commit()
seq_num = 1
cod_seq = ""
final_totel = 0.0
def check_zero(codc):
    if codc!=0:
        ##print("codc_inside ===== ",codc)
        return (codc*codc)
    else:
        return 0
def protien(field9):
    se=list(field9)
    cod_seq=""
    amino=""
    count=1
    codc = [0] * 64
    for i in se:
        amino=amino+i
        if (count%3) == 0:
            ##print("amino = "+amino)
            if (amino == 'TTT'):
                codc[0]=codc[0]+ 1  # Phe
                ret = 'F'
            if (amino == 'TTC'):
                # print("the string is: PHE\n")
                ret = 'F'# Phe
                codc[1] += 1
            if (amino == 'TTG'):
                ret = 'L'
                codc[2] += 1
            if(amino == 'TTA'):
                ret = 'L'
                codc[3] += 1
            if(amino == 'CTT'):
                ret = 'L'
                codc[4] += 1
            if(amino == 'CTC'):
                ret = 'L'
                codc[5] += 1
            if(amino == 'CTA'):
                ret = 'L'
                codc[6] += 1
            if(amino == 'CTG'):
                # print("the string is: LEU\n")
                ret = 'L'
                codc[7] += 1 # Leu
            if (amino == 'ATT'):
                ret = 'I'
                codc[8] += 1
            if (amino == 'ATC'):
                ret = 'I'
                codc[9] += 1
            if (amino == 'ATA'):
                # print("the string is: ILE")
                ret = 'I'
                codc[10] += 1
            if (amino == 'ATG'):
                # print("\nthe string is: MET")
                ret = 'M'
                codc[11] += 1
            if (amino == 'GTA'):
                ret = 'V'
                codc[12] += 1
            if (amino == 'GTT'):
                ret = 'V'
                codc[13] += 1
            if (amino == 'GTG'):
                ret = 'V'
                codc[14] += 1
            if (amino == 'GTC'):
                # print("\nthe string is: VAL")
                ret = 'V'
                codc[15] += 1
            if (amino == 'TCA'):
                ret = 'S'
                codc[16] += 1
            if (amino == 'TCT'):
                ret = 'S'
                codc[17] += 1
            if (amino == 'TCG'):
                ret = 'S'
                codc[18] += 1
            if (amino == 'TCC'):
                # print("\nthe string is: SER")
                ret = 'S'
                codc[19] += 1
            if (amino == 'CCA'):
                ret = 'P'
                codc[20] += 1
            if (amino == 'CCT'):
                ret = 'P'
                codc[21] += 1
            if (amino == 'CCG'):
                ret = 'P'
                codc[22] += 1
            if (amino == 'CCC'):
                # print("\nthe string is: PRO")
                ret = 'P'
                codc[23] += 1
            if (amino == 'ACA'):
                ret = 'T'
                codc[24] += 1
            if (amino == 'ACT'):
                ret = 'T'
                codc[25] += 1
            if (amino == 'ACG'):
                ret = 'T'
                codc[26] += 1
            if (amino == 'ACC'):
                # print("\nthe string is: THR")
                ret = 'T'
                codc[27] += 1
            if (amino == 'GCA'):
                ret = 'A'
                codc[28] += 1
            if (amino == 'GCT'):
                ret = 'A'
                codc[29] += 1
            if (amino == 'GCG'):
                ret = 'A'
                codc[30] += 1
            if (amino == 'GCC'):
                # print("\nthe string is: ALA")
                ret = 'A'
                codc[31] += 1
            if (amino == 'TAT'):
                ret = 'Y'
                codc[32] += 1
            if (amino == 'TAC'):
                # print("\nthe string is: TYR")
                ret = 'Y'
                codc[33] += 1
            if (amino == 'TAA'):
                ret = 'Stop'
                codc[34] += 1
            if (amino == 'TAG'):
                # print("\nthe string is: ....STOP...")
                ret = 'Stop'
                codc[35] += 1
            if (amino == 'CAT'):
                ret = 'H'
                codc[36] += 1
            if (amino == 'CAC'):
                # print("\nthe string is: HIS")
                ret = 'H'
                codc[37] += 1
            if (amino == 'CAA'):
                ret = 'Q'
                codc[38] += 1
            if (amino == 'CAG'):
                # print("\nthe string is: GLN")
                ret = 'Q'
                codc[39] += 1
            if (amino == 'AAT'):
                ret = 'N'
                codc[40] += 1
            if (amino == 'AAC'):
                # print("\nthe string is: ASN")
                ret = 'N'
                codc[41] += 1
            if (amino == 'AAA'):
                ret = 'K'
                codc[42] += 1
            if (amino == 'AAG'):
                # print("\nthe string is: LYS")
                ret = 'K'
                codc[43] += 1
            if (amino == 'GAC'):
                ret = 'D'
                codc[44] += 1
            if (amino == 'GAT'):
                # print("\nthe string is: ASP")
                ret = 'D'
                codc[45] += 1
            if (amino == 'GAA'):
                ret = 'E'
                codc[46] += 1
            if (amino == 'GAG'):
                # print("\nthe string is: GLU")
                ret = 'E'
                codc[47] += 1
            if (amino == 'TGT'):
                ret = 'C'
                codc[48] += 1
            if (amino == 'TGC'):
                # print("\nthe string is: CYS")
                ret = 'C'
                codc[49] += 1
            if (amino == 'TGA'):
                # print("\nthe string is: ....STOP")
                ret = 'Stop'
                codc[50] += 1
            if (amino == 'TGG'):
                # print("\nthe string is: TRP")
                ret = 'W'
                codc[51] += 1
            if (amino == 'AGT'):
                ret = 'S'
                codc[52] += 1
            if (amino == 'AGC'):
                # print("\nthe string is: SER")
                ret = 'S'
                codc[53] += 1
            if (amino == 'AGA'):
                ret = 'R'
                codc[54] += 1
            if (amino == 'AGG'):
                # print("\nthe string is: ARG")
                ret = 'R'
                codc[55] += 1
            if (amino == 'CGA'):
                ret = 'R'
                codc[56] += 1
            if (amino == 'CGT'):
                ret = 'R'
                codc[57] += 1
            if (amino == 'CGG'):
                ret = 'R'
                codc[58] += 1
            if (amino == 'CGC'):
                # print("\nthe string is: ARG")
                ret = 'R'
                codc[59] += 1
            if (amino == 'GGA'):
                ret = 'G'
                codc[60] += 1
            if (amino == 'GGT'):
                ret = 'G'
                codc[61] += 1
            if (amino == 'GGC'):
                ret = 'G'
                codc[62] += 1
            if (amino == 'GGG'):
                # print("\nthe string is: GLY")
                ret = 'G'
                codc[63] += 1
            cod_seq=cod_seq+ret
            amino=""
        count+=1
    c=0
    for li in codc:
        ##print("code[",c,"]= ",li)
        c+=1
    ##print()
    total=[0] * 23
    #print("for phe---->> ")
    total[0]= codc[0]+codc[1]
    if(total[0]!=0 ):
        codc[0]= codc[0]/total[0]
        codc[1]= codc[1]/total[0]
        total[0]= check_zero(codc[0])+check_zero(codc[1])
        ##print("total==",total[0])
    #print("for Leu---->> ")
    total[1]= codc[2]+codc[3]+codc[4]+codc[5]+codc[6]+codc[7]
    if(total[1]!=0):
        codc[2]= codc[2]/total[1]
        codc[3]= codc[3]/total[1]
        codc[4]= codc[4]/total[1]
        codc[5]= codc[5]/total[1]
        codc[6]= codc[6]/total[1]
        codc[7]= codc[7]/total[1]
        total[1]=check_zero(codc[2])+check_zero(codc[3])+check_zero(codc[4])+check_zero(codc[5]) +check_zero(codc[6]) +check_zero(codc[7])
        ##print("total1=",total[1])
        ##print("codc=",codc[2],codc[3],codc[4],codc[5],codc[6])
    #print("for Ile---->> ")
    total[2]= codc[8]+codc[9]+codc[10]
    if(total[2]!=0):
        codc[8]= codc[8]/total[2]
        codc[9]= codc[9]/total[2]
        codc[10]= codc[10]/total[2]
        total[2]=check_zero(codc[8])+check_zero(codc[9])+check_zero(codc[10])
        ##print("check = ",check_zero(codc[8]),check_zero(codc[9]))
        ##print("total[2]=",total[2])
        ##print("codc=",codc[8],codc[9],codc[10])
   # print("for Met---->>")
    total[3]= codc[11]
    if(total[3]!=0):
        codc[11]= codc[11]/total[3]
        total[3]=check_zero(codc[11])
        ##print("total=",total[3])
    #print("for Val---->>")
    total[4]= codc[12]+codc[13]+codc[14]+codc[15]
    ##print("codc[12] =",codc[12])
    ##print("codc[13] =",codc[13])
    ##print("codc[14] =",codc[14])
    ##print("codc[15] =",codc[15])
    ##print("total here =" ,total[4])
    if(total[4]!=0):
        codc[12]= codc[12]/total[4]
        codc[13]= codc[13]/total[4]
        codc[14]= codc[14]/total[4]
        codc[15]= codc[15]/total[4]
      ##  print("codc[12] =",codc[12])
        ##print("codc[13] =",codc[13])
        ##print("codc[14] =",codc[14])
        ##print("codc[15] =",codc[15])
        ##print("check zero == ",check_zero(codc[12]))
        total[4]=check_zero(codc[12])+check_zero(codc[13])+check_zero(codc[14])+check_zero(codc[15])
        ##print("1/total here =" ,total[4])
    #print("for Ser---->>")
    total[5]= codc[16]+codc[17]+codc[18]+codc[19]
    if(total[5]!=0):
        codc[16]= codc[16]/total[5]
        codc[17]= codc[17]/total[5]
        codc[18]= codc[18]/total[5]
        codc[19]= codc[19]/total[5]
        total[5]=check_zero(codc[16])+check_zero(codc[17])+check_zero(codc[18])+check_zero(codc[19])
    #print("for  Pro---->>")
    total[6]= codc[20]+codc[21]+codc[22]+codc[23]
    if(total[6]!=0):
        codc[20]= codc[20]/total[6]
        codc[21]= codc[21]/total[6]
        codc[22]= codc[22]/total[6]
        codc[23]= codc[23]/total[6]
        total[6]=check_zero(codc[20])+check_zero(codc[21])+check_zero(codc[22])+check_zero(codc[23])
   # print("for Thr---->>")
    total[7]= codc[24]+codc[25]+codc[26]+codc[27]
    if(total[7]!=0):
        codc[24]= codc[24]/total[7]
        codc[25]= codc[25]/total[7]
        codc[26]= codc[26]/total[7]
        codc[27]= codc[27]/total[7]
        total[7]=check_zero(codc[24])+check_zero(codc[25])+check_zero(codc[26])+check_zero(codc[27])
   # print("for Ala---->>")
    total[8]= codc[28]+codc[29]+codc[30]+codc[31]
    if(total[8]!=0):
        codc[28]= codc[28]/total[8]
        codc[29]= codc[29]/total[8]
        codc[30]= codc[30]/total[8]
        codc[31]= codc[31]/total[8]
        total[8]=check_zero(codc[28])+check_zero(codc[29])+check_zero(codc[30])+check_zero(codc[31])
   # print("for Tyr---->>")
    total[9]= codc[32]+codc[33]
    if(total[9]!=0):
        codc[32]= codc[32]/total[9]
        codc[33]= codc[33]/total[9]
        total[9]=check_zero(codc[32])+check_zero(codc[33])
    #print("for Stop---->>")
    total[10]= codc[34]+codc[35]
    if(total[10]!=0):
        codc[34]= codc[34]/total[10]
        codc[35]= codc[35]/total[10]
        total[10]=check_zero(codc[34])+check_zero(codc[35])
   # print("for His---->>")
    total[11]= codc[36]+codc[37]
    if(total[11]!=0):
        codc[36]= codc[36]/total[11]
        codc[37]= codc[37]/total[11]
        total[11]=check_zero(codc[36])+check_zero(codc[37])
   # print("for Gln---->>")
    total[12]= codc[38]+codc[39]
    if(total[12]!=0):
        codc[38]= codc[38]/total[12]
        codc[39]= codc[39]/total[12]
        total[12]=check_zero(codc[38])+check_zero(codc[39])
   # print("for Asn---->>")
    total[13]= codc[40]+codc[41]
    if(total[13]!=0):
        codc[40]= codc[40]/total[13]
        codc[41]= codc[41]/total[13]
        total[13]=check_zero(codc[40])+check_zero(codc[41])
   # print("for Lys---->>")
    total[14]= codc[42]+codc[43]
    if(total[14]!=0):
        codc[42]= codc[42]/total[14]
        codc[43]= codc[43]/total[14]
        total[14]=check_zero(codc[42])+check_zero(codc[43])
  #  print("for Asp---->>")
    total[15]= codc[44]+codc[45]
    if(total[15]!=0):
        codc[44]= codc[44]/total[15]
        codc[45]= codc[45]/total[15]
        total[15]=check_zero(codc[44])+check_zero(codc[45])
   # print("for Glu---->>")
    total[16]= codc[46]+codc[47]
    if(total[16]!=0):
        codc[46]= codc[46]/total[16]
        codc[47]= codc[47]/total[16]
        total[16]=check_zero(codc[46])+check_zero(codc[47])
 #   print("for Cys---->>")
    total[17]= codc[48]+codc[49]
    if(total[17]!=0):
        codc[48]= codc[48]/total[17]
        codc[49]= codc[49]/total[17]
        total[17]=check_zero(codc[48])+check_zero(codc[49])
  #  print("for Ter---->>")
    total[18]= codc[50]
    if(total[18]!=0):
        codc[50]= codc[50]/total[18]
        total[18]=check_zero(codc[50])
  #  print("for Trp---->>")
    total[19]= codc[51]
    if(total[19]!=0):
        codc[51]= codc[51]/total[19]
        total[19]=check_zero(codc[51])
        ##print("total= ",total[19])
   # print("for Ser---->>")
    total[20]= codc[52]+codc[53]
    if(total[20]!=0):
        codc[52]= codc[52]/total[20]
        codc[53]= codc[53]/total[20]
        total[20]=check_zero(codc[52])+check_zero(codc[53])
        ##print("total= ",total[20])
   # print("for Arg---->>")
    total[21]= codc[54]+codc[55]+codc[56]+codc[57]+codc[58]+codc[59]
    if(total[21]!=0):
        codc[54]= codc[54]/total[21]
        codc[55]= codc[55]/total[21]
        codc[56]= codc[56]/total[21]
        codc[57]= codc[57]/total[21]
        codc[58]= codc[58]/total[21]
        codc[59]= codc[59]/total[21]
        total[21]=check_zero(codc[54])+check_zero(codc[55])+check_zero(codc[56])+check_zero(codc[57])+check_zero(codc[58])+check_zero(codc[59])
        ##print("total= ",total[21])
   # print("for Gly---->>")
    total[22]= codc[60]+codc[61]+codc[62]+codc[63]
    if(total[22]!=0):
        codc[60]= codc[60]/total[22]
        codc[61]= codc[61]/total[22]
        codc[62]= codc[62]/total[22]
        codc[63]= codc[63]/total[22]
        total[22]=check_zero(codc[60])+check_zero(codc[61])+check_zero(codc[62])+check_zero(codc[63])
        ##print("total= ",total[22])
    final_total=0
    for i in total:
        if i!=0:
            ##print("i=",i)
            final_total=final_total+(1/i)
    ##print("final total== ",final_total)
    ##print("m= ",codc[0])
    ##print(cod_seq)
    return cod_seq,final_total

file_1 = open("upload.txt", "r")
i8=0
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
        #i8=0
        #for char in atgc_seq:
        var,data = protien(atgc_seq)
        #data=round(data)
        
        sql_insert_query = """ INSERT INTO `protien_dbtest` (`seq_num`, `protien_seq`,`Nc`) VALUES (%s,%s,%s)"""
        insert_tuple = (str(seq_num),str(var),str(data))
        mycurser.execute( sql_insert_query,insert_tuple )
        seq_num = seq_num + 1
        conn.commit()
        #print(var,data)
conn.commit()
conn.close()
