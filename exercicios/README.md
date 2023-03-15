# <span style='color:yellow; font-weight: bold;'>Exercicio 01</span>
## <span style='color:green; font-weight: bold;'>Dicas</span>:
- Criar uma pasta de `exercicios`

    - Vídeo mostrando como criar uma pasta no <span style='color:lightblue'>VSCode</span>: https://youtu.be/sfy8mMdoGm4
- Criar um arquivo por exercicio. Ex.: `ex01.py`    


    - Vídeo mostrando como criar um arquivo dentro de uma pasta no <span style='color:lightblue'>VSCode</span>: https://youtu.be/MOUuwvO309Q
- Copiar o código da descrição e colar no exercicio respectivo e testar sem alterar e se tiver tudo certo, fazer as alterações.

    - Vídeo mostrando como copiar o código e colar dentro de um arquivo no <span style='color:lightblue'>VSCode</span>: https://youtu.be/Q1N-3FyRoks

--- 

### Alterar o código para que a saída seja com mais detalhes
<br>

- O código atual esta exibindo da seguinte forma:
```bash
Digite seu nome: Igor
Digite seu endereco: Rua xv de novembro, 1517
Digite sua profissao: Programador
Igor Rua xv de novembro, 1517 Programador
```

- Forma desejada:
```bash
Digite seu nome: Igor
Digite seu endereco: Rua xv de novembro, 1517
Digite sua profissao: Programador
Nome: Igor - Endereco: Rua xv de novembro, 1517 - Profissao: Programador
```
- Código:
```python
nome = input("Digite seu nome: ")
endereco = input("Digite seu endereco: ")
profissao = input("Digite sua profissao: ")

print(f"{nome} - {endereco} - {profissao}") # Alterar aqui
```

Entradas:
 - nome (string)
 - endereço (string)
 - profissao (string)

Saídas:
- inteiro
```bash
Nome: Igor - Endereco: Rua xv de novembro, 1517 - Profissao: Programador
```

# <span style='color:yellow; font-weight: bold;'>Exercicio 02</span>

### Alterar o código para que a variavel b leia do teclado um novo valor numero e seja convertido para inteiro

- Exemplo de ler o dado do teclado:
    ```python 
    z = input("Digite um valor: ") # Isso vai ler um valor do teclado em --> STRING <-- e atribuir na variavel z
    ```
- Exemplo de conversão de string para inteiro:
    ```python 
    int("5") # Isso vai resultar no inteiro 5
    ```

- Código:
```python
a = int( input("Digite um numero: ") )
b = 5 # Alterar aqui para ler do teclado e converter para inteiro
print(a+b)
```

Entradas:
 - a (inteiro)
 - b (inteiro)

Saídas:
- inteiro
```bash
15
```

# <span style='color:yellow; font-weight: bold;'>Exercicio 03</span>

### Utilizar o código do exercicio anterior e exibir o resultado das seguintes formas



Entradas:
 - a
 - b

Saídas:
```bash
A soma de 9+3 = 12
A multiplicação de 9x3 = 27
A subtração de 9-3 = 6
A divisão de 9/3 = 3
```

# <span style='color:yellow; font-weight: bold;'>Exercicio 04</span>

### Calcular o desconto de <span style="color:green">R$ 10,00</span> em cima do valor digitado e exibir o valor total, valor do desconto e o valor com desconto.

- Código:


    ```python
    valor_total = int(input("Digite o valor total: "))
    desconto = 10.00
    valor_total_com_desconto = 25 - 10 # Realizar o calculo aqui do desconto com o valor digitado
    print("O valor total é: R$ 25.00") # Alterar para exibir o valor dinamico 
    print(f"O valor do desconto é: R$ {desconto}") # Não alterar, já exibe o valor correto
    print("O valor total com desconto é: R$ 15.00") # Alterar para exibir o valor dinamico

    ```

Entradas:
 - Valor Total

Saídas:
```bash
O valor total é: R$ 25.00
O valor do desconto é: R$ 10.00
O valor total com desconto é: R$ 15,00
```


# <span style='color:yellow; font-weight: bold;'>Exercicio 05</span>

### Utilizando o exercicio anterior, calcular o desconto de <span style="color:green">10%</span> em cima do valor digitado e exibir o valor total, valor do desconto e o valor com desconto.
- Dicas:
    - Para calcular a porcentagem de um valor, deve-se multiplicar o percentual correspondente pela quantidade total. Ex.: 
    - - `10% de 200 é (10/100)x200 = 20` 
    - Para calcular o valor total com desconto, deve-se subtrair o valor total pelo desconto:
    - - `R$ 200,00 - R$ 20,00 = R$ 180,00`
    - ```bash
    Valor Total: R$ 200,00
    Porcentagem de desconto: 10%
    Valor do desconto : R$ 20,00
    Valor total com desconto: R$ 200,00 - $R$ 20,00 = R$ 180,00
    ```
Entradas:
 - Valor Total

Saídas:
```bash
Valor Total: R$ 200,00
Porcentagem de desconto: 10%
Valor do desconto : R$ 20,00
Valor total com desconto: R$ 180,00
```
 


# <span style='color:yellow; font-weight: bold;'>Exercicio 06</span>

### Utilizando o exercicio anterior, calcular o desconto e o valor total com desconto tendo como entrada o valor total e a porcentagem

Entradas:
 - Valor Total
 - Porcentagem de desconto

Saídas:
```bash
Valor Total: R$ 200,00
Porcentagem de desconto: 10%
Valor do desconto : R$ 20,00
Valor total com desconto: R$ 180,00
```

# <span style='color:yellow; font-weight: bold;'>Exercicio 07</span>

### Calcular a area de um retangulo
- Para se calcular a área de um retângulo é necessário multiplicar o comprimento pela largura.
- Ex.: 
    - comprimento: 3cm
    - largura: 5cm
    - area = largura * comprimento  => 5*3 => 15


Entradas:
 - comprimento (cm)
 - largura (cm)

Saídas:
```bash
A área do retangulo de 3cm de comprimento e 5cm de largura é 15cm²
```


# <span style='color:yellow; font-weight: bold;'>Exercicio 08</span>

### Calcular a média
- Escreva um programa que calcule a média de duas notas entre 0 e 10
- Ex.: 
    - nota1: 8
    - nota2: 6
    - media = (nota1 + nota2)/2 => (8 + 6) / 2 => 7.00


Entradas:
 - nota1 (float)
 - nota2 (float)

Saídas:
```bash
A média é 7.00
```

Bônus: E se forem 3 notas?

# <span style='color:yellow; font-weight: bold;'>Exercicio 9</span>

### Maior
- Escreva um programa que recebe 2 numeros inteiros e retorna o maior deles
- Ex.: 
    - Se os números 3 e 5 forem digitados, o retorno deve ser 5.
    - Se o os números 20 e 58 forem digitaos, o retorno deve ser 58.


Entrada:
 - a (int)
 - b (int)

Saída:
inteiro
```bash
20
```



# <span style='color:yellow; font-weight: bold;'>Exercicio 10</span>

### Positivo ou negativo
- Escreva um programa que recebe como entrada um número e retorna uma mensagem dizendo se é positivo ou negativo.
- Ex.: 
    - Se o valor digitado for maior do que 0, exibir a mensagem `POSITIVO`
    - Se o valor digitado for menor do que 0, exibir a mensagem `NEGATIVO`
    - Se o valor digitado for igual a 0, exibir a mensagem `ZERO`


Entradas:
 - numero (int)

Saídas:
```bash
POSITIVO
```
ou 
```bash
NEGATIVO
```
ou 
```bash
ZERO
```







# <span style='color:yellow; font-weight: bold;'>Exercicio 11</span>

### Maior de idade
- Escreva um programa que recebe como entrada uma idade e retorna uma mensagem dizendo se é adulto ou não.
- Ex.: 
    - Se a idade digitada for maior ou igual a 18 exibir a mensagem `É maior de idade`, caso contrário exibir a mensagem `Não é maior de idade`


Entradas:
 - idade (int)

Saídas:
```bash
É maior de idade
```
ou 
```bash
Não é maior de idade
```


# <span style='color:yellow; font-weight: bold;'>Exercicio 12</span>

### IMC
- Escreva um programa que calcula o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

    | IMC  | Classificação |
    | ------------- | ------------- |
    | < 18,5  | Abaixo do Peso  |
    | 18,6 - 24,9  | Saudavel   |
    | 25,0 - 29,9  | Peso em excesso  |
    | 30,0 - 34,9  | Obesidade Grau I  |
    | 35,0 - 39,9 | Obesidade Grau II(severa)  |
    | ≥ 40,0   | Obesidade Grau III(morbida)  |

- Como calcular o IMC:
    - IMC = Peso ÷ (Altura × Altura)

- Ex.: 
    - Se a idade digitada for maior ou igual a 18 exibir a mensagem `É maior de idade`, caso contrário exibir a mensagem `Não é maior de idade`


Entradas:
 - Peso (float)
 - Altura (float)

Saídas:
```bash
Peso em excesso 
```






