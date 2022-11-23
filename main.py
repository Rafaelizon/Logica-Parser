#Rafael Guaitanele Niszczak

constanteCaracteres = ["T", "F"]

proposicaoCaracteres = []
for i in range(48, 58):
    proposicaoCaracteres.append(chr(i))
for i in range(97, 123):
    proposicaoCaracteres.append(chr(i))

abreParen = "("
fechaParen = ")"

operadorUnarioCaracteres = [r"\neg"]
operadorBinarioCaracteres = ["\disj", "\conj", "\implic", r"\biImplic"]


def dividirFormulas(formulas):

    # exemplos de entrada:
    # string = "(a b (a b c d) (a b c d) d) (a b c d)"
    # string2 = "(a b c d) a"

    strings = ["", ""]

    n = 0
    if(formulas[0] == abreParen):
        for i in range(0, len(formulas)):
            if formulas[i] == abreParen:
                n += 1
            elif formulas[i] == fechaParen:
                n -= 1
                if(n < 0):
                    return strings
                elif (n == 0):
                    for j in range(0, i + 1):
                        strings[0] += formulas[j]
                    for j in range(i + 2, len(formulas)):
                        strings[1] += formulas[j]
                    break
        return strings
    else:
        strings = formulas.split(" ", 1)
    return strings

def proposicao(string):
    for i in range(0, len(string)):
        caracter = str(string[i])
        if caracter not in proposicaoCaracteres:
            return False
    if(string == ""):
        return False
    return True

def formulaUnaria(string):
    strings = string.split(" ", 2)
    if (strings[0] == abreParen and strings[2][len(strings[2]) - 1] == fechaParen):
        if (strings[1] in operadorUnarioCaracteres):
            if(formula(strings[2][:-2])):
                return True
    return False

def formulaBinaria(string):
    strings = string.split(" ", 2)
    if (strings[0] == abreParen and strings[2][len(strings[2]) - 1] == fechaParen):
        if (strings[1] in operadorBinarioCaracteres):
            formulas = dividirFormulas(strings[2][:-2])
            if(formula(formulas[0]) and formula(formulas[1])):
                return True
    return False

def formula(string):
    if (string in constanteCaracteres or proposicao(string) or formulaUnaria(string) or formulaBinaria(string)):
        return True
    else:
        return False

# exemplo: ( \neg ( \disj ( \biImplic ( \neg T ) ( \neg T ) ) ( \neg T ) ) )

nomeArquivo = ""

while(True):
    nomeArquivo = input("Digite o nome do arquivo (Exemplo: arquivo1.txt): ")
    try:
        with open(nomeArquivo, "r") as arquivo:
            linhas = arquivo.read().split("\n")
        break
    except:
        print("Nome de arquivo invalido! Digite novamente")

for i in range(1, int(linhas[0]) + 1):
    if(formula(linhas[i])):
        print(linhas[i] + ": valida")
    else:
        print(linhas[i] + ": invalida")