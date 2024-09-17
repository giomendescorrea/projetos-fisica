import math

print("--------------------------- Autores do projeto ---------------------------")
print("Giovanna Mendes, Guilherme Meireles, Ranielly Affonso e Natasha Almeida.")
print("\nO programa foi criado para calcular as propriedades relacionadas às ondas eletromagnéticas,"
      "\nde acordo com os conceitos estudados em Física Moderna.\n"
      "O software permite que o usuário insira alguns parâmetros como comprimento de onda, frequência, campos magnéticos,"
      "número de onda e intensidade.\n")

print("Conceitos utilizados no programa:\n")

print("1. Comprimento de Onda:\n"
      "Representa a distância que as ondas se propagam no vácuo. O programa solicita o comprimento da onda e calcula"
      " a frequência, o número de onda e a frequência angular usando as seguintes fórmulas:\n"
      "   - Frequência: f = c / λ\n"
      "   - Número de Onda: k = 2π / λ\n"
      "   - Frequência Angular: w = 2πf\n")

print("2. Frequência:\n"
      "Indica quantos ciclos de uma onda passam por um ponto em um período de tempo. O programa solicita a frequência"
      " da onda e calcula o comprimento da onda, o número de onda e a frequência angular usando as fórmulas:\n"
      "   - Comprimento de Onda: λ = c / f\n"
      "   - Número de Onda: k = 2π / λ\n"
      "   - Frequência Angular: w = 2πf\n")

print("3. Frequência Angular:\n"
      "É a velocidade com que a onda oscila em radianos por segundo. O programa solicita a frequência angular e"
      " calcula a frequência, o comprimento e o número da onda usando as seguintes fórmulas:\n"
      "   - Frequência: f = w / 2π\n"
      "   - Comprimento de Onda: λ = c / f\n"
      "   - Número de Onda: k = 2π / λ\n")

print("4. Número de Onda:\n"
      "Calcula quantas ondas existem por metro. O programa solicita o número de onda e calcula o comprimento, a"
      " frequência e a frequência angular usando as fórmulas:\n"
      "   - Comprimento de Onda: λ = 2π / k\n"
      "   - Frequência: f = c / λ\n"
      "   - Frequência Angular: w = 2πf\n")

print("5. Campo Magnético:\n"
      "É uma região do espaço onde uma carga elétrica em movimento, como uma corrente elétrica, experimenta uma força."
      " O programa solicita o campo magnético e calcula o campo elétrico e a intensidade da onda usando as fórmulas:\n"
      "   - Campo Elétrico: E = B * c\n"
      "   - Intensidade: I = E² / (2 * μ₀ * c)\n")

print("6. Campo Elétrico:\n"
      "Calcula o campo magnético e a intensidade da onda a partir do campo elétrico fornecido pelo usuário. As fórmulas"
      " usadas são:\n"
      "   - Campo Magnético: B = E / c\n"
      "   - Intensidade: I = E² / (2 * μ₀ * c)\n")

print("7. Intensidade da Onda:\n"
      "É a medida da energia transportada pela onda por unidade de área e tempo. O programa solicita a intensidade da onda"
      " e calcula o campo elétrico e magnético usando as fórmulas:\n"
      "   - Campo Elétrico: E = sqrt(2 * μ₀ * c * I)\n"
      "   - Campo Magnético: B = E / c\n")

# variável c
velocidade_luz = 3e+08
# variável u chamada de mi
constante_magnetica = (4 * math.pi) * (10 ** -7)

def calcula_comprimento(comprimento_onda):
    frequencia = velocidade_luz/comprimento_onda # Hz
    numero_onda = (2*math.pi)/comprimento_onda # rad/m
    frequencia_angular = (2*math.pi)*frequencia # rad/s
    return frequencia, numero_onda, frequencia_angular

def calcula_frequencia(frequencia):
    comprimento_onda = velocidade_luz/frequencia # m
    numero_onda = (2*math.pi)/comprimento_onda # rad/m 
    frequencia_angular = (2*math.pi)*frequencia # rad/s
    return comprimento_onda, numero_onda, frequencia_angular

def calcula_frequencia_angular(frequencia_angular):
    frequencia = frequencia_angular/(2*math.pi) # Hz
    comprimento_onda = velocidade_luz/frequencia # m
    numero_onda = (2*math.pi)/comprimento_onda # rad/m
    return frequencia, comprimento_onda, numero_onda

def calcula_numero_onda(numero_onda):
    comprimento_onda = (2*math.pi)/numero_onda # m
    frequencia = velocidade_luz/comprimento_onda # Hz
    frequencia_angular = (2*math.pi)*frequencia # rad/s
    return comprimento_onda, frequencia, frequencia_angular

def calcula_campo_magnetico(campo_magnetico):
    campo_eletrico = campo_magnetico*velocidade_luz
    intensidade_onda = (math.pow(campo_eletrico, 2))/(2*constante_magnetica*velocidade_luz)
    return campo_eletrico, intensidade_onda

def calcula_campo_eletrico(campo_eletrico):
    campo_magnetico = campo_eletrico/velocidade_luz
    intensidade_onda = (math.pow(campo_eletrico, 2))/(2*constante_magnetica*velocidade_luz)
    return campo_magnetico, intensidade_onda

def calcula_intensidade_onda(intensidade_onda):
    campo_eletrico = math.sqrt(2*constante_magnetica*velocidade_luz*intensidade_onda)
    campo_magnetico = campo_eletrico/velocidade_luz
    return campo_eletrico, campo_magnetico

while True:
    print("---------- MENU ----------")
    print("1. Comprimento de onda (y)")
    print("2. Frequência (f)")
    print("3. Frequência angular (w)")
    print("4. Número de onda (k)")
    print("5. Campo magnético da onda (Bm)")
    print("6. Campo elétrico da onda (Em)")
    print("7. Intensidade da onda (I)")
    print("0. Sair")
    entrada = int(input("Digite o número da variável que será inserida: "))

    if entrada == 1:
        comprimento_onda = float(input("Digite o valor do comprimento de onda em metros: "))
        frequencia, numero_onda, frequencia_angular = calcula_comprimento(comprimento_onda)
        print(f"\nFrequência da onda: {frequencia:.3e} Hz")
        print(f"Número de onda: {numero_onda:.3e} rad/m")
        print(f"Frequência angular da onda: {frequencia_angular:.3e} rad/s\n")

    elif entrada == 2:
        frequencia = float(input("Digite o valor da frequência em Hz: "))
        comprimento_onda, numero_onda, frequencia_angular = calcula_frequencia(frequencia)
        print(f"\nComprimento de onda: {comprimento_onda:.3e} m")
        print(f"Número de onda: {numero_onda:.3e} rad/m")
        print(f"Frequência angular da onda: {frequencia_angular:.3e} rad/s\n")

    elif entrada == 3:
        frequencia_angular = float(input("Digite o valor da frequência angular em rad/s: "))
        frequencia, comprimento_onda, numero_onda = calcula_frequencia_angular(frequencia_angular)
        print(f"\nComprimento de onda: {comprimento_onda:.3e} m")
        print(f"Frequência da onda: {frequencia:.3e} Hz")
        print(f"Número de onda: {numero_onda:.3e} rad/m\n")

    elif entrada == 4:
        numero_onda = float(input("Digite o valor do número de onda em rad/m: "))
        comprimento_onda, frequencia, frequencia_angular = calcula_numero_onda(numero_onda)
        print(f"\nComprimento de onda: {comprimento_onda:.3e} m")
        print(f"Frequência da onda: {frequencia:.3e} Hz")
        print(f"Frequência angular da onda: {frequencia_angular:.3e} rad/s\n")

    elif entrada == 5:
        campo_magnetico = float(input("Digite o valor do campo magnético da onda em T: "))
        campo_eletrico, intensidade_onda = calcula_campo_magnetico(campo_magnetico)
        print(f"\nCampo elétrico: {campo_eletrico:.3e} V/m")
        print(f"Intensidade da onda: {intensidade_onda:.3e} W/m²\n")

    elif entrada == 6:
        campo_eletrico = float(input("Digite o valor do campo elétrico da onda em V/m: "))
        campo_magnetico, intensidade_onda = calcula_campo_eletrico(campo_eletrico)
        print(f"\nCampo magnético: {campo_magnetico:.3e} V/m")
        print(f"Intensidade da onda: {intensidade_onda:.3e} W/m²\n")

    elif entrada == 7:
        intensidade_onda = float(input("Digite o valor da intensidade da onda em W/m²: "))
        campo_magnetico, campo_eletrico = calcula_intensidade_onda(intensidade_onda)
        print(f"\nCampo magnético: {campo_magnetico:.3e} T")
        print(f"Campo elétrico: {campo_eletrico:.3e} V/m\n")

    elif entrada == 0:
        print("---Obrigado por utilizar o nosso software. Até a próxima :)")
        break
         
    else:
        print("Comando não encontrado, utilize uma entrada válida.")




    
