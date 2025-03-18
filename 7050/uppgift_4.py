tal = int(input("mata in ett tal"))
if 0 <= tal <= 9:
    print (f"{tal} är ensifrigt tal")
elif 10 <= tal <= 99:
    print (f"{tal} är tvåsiffriga tal")
elif 100 <= tal <= 999:
    print (f"{tal} är tresiffriga tal")
elif 1000 <= tal:
    print (f"{tal} är minst fyrsifrriga tal")
else:
    print ("tal mindre än 0 är negativa")
    