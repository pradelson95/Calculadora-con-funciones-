def menú():

  print("1.suma\n")
  print("2.resta\n")
  print("3.múltiplicación\n")
  print("4.divición\n")
  print("5.salir\n")

menú()

def inicio():

  try:
    
    opciones_de_menú = int(input("Elija una opción de menú:"))
    
    if opciones_de_menú==1:
        
        num1 = float(input("ingrese el primer número:"))
        
        num2 = float(input("ingrese el segundo número:"))
        
        resultado = num1+num2
        return resultado

    elif opciones_de_menú==2:

      num1 = float(input("ingrese el primer número:"))
        
      num2 = float(input("ingrese el segundo número:"))
        
      resultado = num1-num2
      return resultado 

    elif opciones_de_menú==3:

      
      num1 = float(input("ingrese el primer número:"))
        
      num2 = float(input("ingrese el segundo número:"))
        
      resultado = num1*num2
      return resultado 

    elif opciones_de_menú==4:

      
      num1 = float(input("ingrese el primer número:"))
        
      num2 = float(input("ingrese el segundo número:"))
        
      resultado = num1//num2
      return resultado 
    
    elif opciones_de_menú==5:
      print("Gracias por usar nuestra calculadora")

    else:
      pass   

  except Exception as error:
    print("algo salio mal!,error")

print(inicio())

