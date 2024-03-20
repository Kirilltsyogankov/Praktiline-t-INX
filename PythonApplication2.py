print("Tere! Ma olen sinu uus sõber - Python!")
nimi=input("Palun sisestage oma nimi. ")
print(nimi+ ", oh, milline kaunis nimi!")
num=int(input(nimi+ ", kas ma võin leida sinu kehamassiindeksi? 0 - ei, 1 - jah =>"))
if num==1:
   try:
     pikkus=float(input("Sisestage oma pikkus (meetrites)."))
   except:
    print("Viga sisestamisel, proovige uuesti.")
    exit()
   try:
     mass=float(input("Sisestage oma mass (kilogrammides)."))
   except:
    print("Viga sisestamisel, proovige uuesti.") 
    exit()
   indeks=round(mass / (0.01*pikkus)**2,1)
   print(nimi+ ", sinu kehamassiindeks on:" +str(indeks))
   if indeks<16:
     print("Tervisele ohtlik alakaal")
   elif  16<=indeks<19: 
     print("Alakaal")
   elif  19<=indeks<25:  
     print("Normaalkaal")
   elif  25<=indeks<30:
     print("Ülekaal")
   elif  30<=indeks<35:
     print("Rasvumine")
   elif  35<=indeks<40: 
     print("Tugev rasvumine")
   elif  indeks>=40: 
     print("Tervisele ohtlik rasvumine  ")
else:
  print("Kahju! See on väga kasulik info!""\n")
print("Kohtumiseni, " + nimi + "! Igavesti sinu, Python!")