tal1 = int(input("mata in första talet"))
tal2 = int(input("mata in andra talet"))
tal3 = int(input("mata in tredje talet"))
if tal2 > tal1 < tal3:
    print("första talet är minst")
elif tal1 > tal2 < tal3:
    print("andra talet är minst")
else:
    print("tredje talet är minst")