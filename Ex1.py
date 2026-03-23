# Conversão de unidades

print("Conversor de medidas\n")
a = 1
while a ==1:

    options = int(input("Escolha a conversão: \n1)N⮕kgf \n2)kPa⮕bar \n3)PSI⮕bar \n4)cm²⮕m²\n"))
    valor = float(input("Coloque o valor da unidade: "))
    if options == 1:
        resultado = valor/9.807
        print(valor , "N = "+"% .4f" % resultado + "kgf")
    elif options == 2:
        resultado = valor/100
        print(valor , "kPa = "+"% .4f" % resultado + "bar")
    elif options == 3:
        resultado = valor/14.504
        print(valor , "PSI = "+"% .4f" % resultado + "bar")
    elif options == 4:
        resultado = valor/10000
        print(valor,"cm² = % .4f" % resultado + "m²")
    else:
        print("Conversão inválida")

    a = int(input("Deseja converter mais alguma medida? Digite 1 se sim.\n"))