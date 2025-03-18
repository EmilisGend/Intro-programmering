fm = str(input("skriv din födelsemånad "))
if fm in ["december", "januari", "februari"]:
    print("du fyller år på vintern")
elif fm in ["mars", "april", "maj"]:
    print("du fyller år på våren")
elif fm in ["juni", "juli", "augusti"]:
    print("du fyller år på sommaren")
elif fm in ["september", "oktober", "november"]:
    print ("du fyller år på hösten")