import random
response="y"
while response=="y":
#crear un bucle(ciclo)
 num=random.randint(1,6)
#randint generar un numero aletorio enteros

 if num==1:
    print("[-----]") 
    print("[     ]") 
    print("[  0  ]") 
    print("[     ]") 
    print("[-----]")

    
 if num==2:
    print("[-----]") 
    print("[  0  ]") 
    print("[  0  ]") 
    print("[     ]") 
    print("[-----]")

 if num==3:
    print("[-----]") 
    print("[  0  ]") 
    print("[  0  ]") 
    print("[  0  ]") 
    print("[-----]")

 if num==4:
    print("[-----]") 
    print("[ 0 0 ]") 
    print("[ 0 0 ]") 
    print("[      ]") 
    print("[-----]")

 if num==5:
    print("[-----]") 
    print("[ 0 0 ]") 
    print("[ 0 0 ]") 
    print("[  0  ]") 
    print("[-----]")

 if num==6:
    print("[-----]") 
    print("[ 0 0 ]") 
    print("[ 0 0 ]") 
    print("[ 0 0 ]") 
    print("[-----]")

 response=input(" y para continuar y n para salir")