secret = "gay"
secrett = ""
secrettt = ""
secretttt = ""

i = 1

secrett = input (" dame la palabra secreta: ")

while i==1:

    if secrett != secret:
        print("es incorrecto")
        secrettt = input ("dame la palabra")
    else:
        print("ganaste")
        break


    if secrettt != secret:
      print("es incorrecto")
      secretttt = input ("dame la palabra")
    else:
        print (" ganaste")
        break

    if secretttt != secret:
        print(" es incorecto")
        break
    else:
        print("mal do it again")
        break
