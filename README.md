# 📐 Conversor de Unidades

## 🧾 Descrição do Projeto

Este projeto consiste em um **conversor de unidades** desenvolvido em Python.
O programa permite ao usuário converter diferentes tipos de medidas de forma simples, por meio de um menu interativo no terminal.

---

## ⚙️ Funcionalidades

O sistema realiza as seguintes conversões:

* **Newton (N) → Quilograma-força (kgf)**
* **Quilopascal (kPa) → Bar**
* **PSI → Bar**
* **Centímetro quadrado (cm²) → Metro quadrado (m²)**

Além disso, o usuário pode realizar múltiplas conversões sem precisar reiniciar o programa.

---

## 🧠 Lógica do Programa

O programa funciona com base em:

1. Um **laço de repetição (`while`)**, que mantém o programa ativo.
2. Um **menu de opções**, onde o usuário escolhe o tipo de conversão.
3. Entrada de dados:

   * Tipo de conversão
   * Valor a ser convertido
4. Estruturas condicionais (`if`, `elif`, `else`) para determinar qual cálculo executar.
5. Exibição do resultado formatado.

---

## 💻 Código

```python
# Conversão de unidades

print("Conversor de medidas\n")
a = 1
while a == 1:

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
```

---

## 📊 Exemplos de Uso

```
Escolha a conversão:
1) N⮕kgf
2) kPa⮕bar
3) PSI⮕bar
4) cm²⮕m²

Opção: 1
Valor: 98.07

Resultado:
98.07 N = 10.0000 kgf
```

---

## 👨‍💻 Participantes

```

Programador 1: Marcos Ramos RM: 565631
Programador 2: Heitor Costa RM: 562007
Responsável pelos calculos: Matheus Porto RM:561847
Tester 1: Bruno Coelho RM: 555279
Tester 2: Henrique Buassalli RM: 564877
