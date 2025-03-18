tal1 = int(input("mata in första talet"))
tal2 = int(input("mata in andra talet"))
tal3 = int(input("mata in tredje talet"))
if tal1 > tal2 and tal1 < tal3:
    print(f"{tal2} {tal1} {tal3}")
elif tal2 > tal1 and tal2 < tal3:
    print(f"{tal1} {tal2} {tal3}")
elif tal1 > tal3 and tal1 < tal2:
    print(f"{tal3} {tal1} {tal2}")
elif tal3 > tal2 and tal3 < tal1:
    print(f"{tal2} {tal3} {tal1}") 

