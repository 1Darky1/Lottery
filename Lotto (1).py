import random
  
sorsolas= []
beolvas= []
while len(beolvas) < 5:
    try:
        puffer = input("Kérem adjon meg egy számot 1 és 90 között: ")
        if int(puffer) >= 1 and int(puffer) <= 90 and (int(puffer) not in beolvas):
            beolvas.append(int(puffer))
        else:
            print("nem megfelelő számot adtál meg.")
    except ValueError:
        print("Nem megfelelő számot adott meg,")
            
while len(sorsolas) < 5:
    puffer2 = random.randint(1,90)
    if puffer2 not in sorsolas:
        sorsolas.append(puffer2)
            
eredmeny = 0
    
for y in range(5):
    for z in range(5):
        if beolvas[y] == sorsolas[z]:
            eredmeny += 1
                
print(eredmeny, "találata volt az öt ös lottón")

print(sorsolas, "ezek voltak a nyerő találatok")