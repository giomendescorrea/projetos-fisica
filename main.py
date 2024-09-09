import math

print("Autores do projeto: Giovanna Mendes, Guilherme Meireles, Ranielly Affonso e Natasha Almeida.")

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
        break
         
    else:
        print("Comando não encontrado, utilize uma entrada válida.")




    
