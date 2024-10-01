import math

h_js = 6.626e-34  # Constante de Planck em J.s
h_ev = 4.135e-15
c = 3e+08
e = 1.602e-19  # Carga do elétron em Coulombs
massa = 9.11e-31

def calcular_raio(numero_quantico):
    raio = (numero_quantico**2) * 5.29e-11  # m
    velocidade = 2.187e+06 / numero_quantico  # m/s
    comprimento_onda = h_js / (massa * velocidade)  # m     ESTA DANDO ERROOOOOOOOOOOOOOOOOO
    energia_cinetica = 13.6 / (numero_quantico**2)  # 
    energia_potencial = -27.2 / (numero_quantico**2)  # energia potencial
    energia_total = -13.6 / (numero_quantico**2)  # energia total

    return raio, velocidade, comprimento_onda, energia_cinetica, energia_potencial, energia_total

def calcular_n_final_inicial(n_final, n_inicial):
    energia_inicial = -13.6 / (n_inicial**2)
    energia_final = -13.6 / (n_final**2)
    energia_absorvida = energia_final - energia_inicial
    frequencia = energia_absorvida/h_ev
    comprimento_onda = (h_ev * c) / energia_absorvida

    return energia_absorvida, frequencia, comprimento_onda

def calcular_n_inicial(n_final, opcao, variavel):
    if opcao == 1:
        energia_foton = h_js * variavel
    elif variavel == 2:
        frequencia = h_js / variavel
        energia_foton = h_js * frequencia
    n_final = math.sqrt((e**4) / (2 * h_js * energia_foton))
    return int(n_final)


while True:
    print("1. Número quântico (n)")
    print("2. Número quântico inicial (ni) e final (nf): ")
    print("3. Número quântico INICIAL (ni) e frequência (f) ou comprimento de onda (y) emitido: ")
    print("4. Número quântico FINAL (nf) e frequência (f) ou comprimento de onda (y) emitido: ")
    print("5. Frequência (f) ou comprimento de onda (y): ")
    print("6. Energia do fóton: ")
    print("0. Sair")
    entrada = int(input("Digite o número da variável que será inserida: "))

    if entrada == 1:
        numero_quantico = float(input("Digite o valor do número quântico: "))
        raio, velocidade, comprimento_onda, energia_cinetica, energia_potencial, energia_total = calcular_raio(numero_quantico)
        print(f"\nRaio: {raio:.3e} em m")
        print(f"\nRaio: {(raio*1e09):.3e} em nm")
        print(f"\nVelocidade: {velocidade:.3e} em m/s")
        print(f"\nComprimento de onda: {comprimento_onda:.3e} em m")
        print(f"\nComprimento de onda: {(comprimento_onda*1e09):.3e} em nm")
        print(f"\nEnergia cinética: {energia_cinetica:.3e} em eV")
        print(f"\nEnergia potencial: {energia_potencial:.3e} em eV")
        print(f"\nEnergia total: {energia_total:.3e} em eV")
    
    elif entrada == 2:
        n_inicial = float(input("Digite o valor do número quântico inicial: "))
        n_final = float(input("Digite o valor do número quântico final: "))
        energia_absorvida, frequencia, comprimento_onda = calcular_n_final_inicial(n_final, n_inicial)
        print(f"\nEnergia absorvida: {energia_absorvida:.3e} em eV")
        print(f"\nComprimento de onda: {comprimento_onda:.3e} em m")
        print(f"\nComprimento de onda: {(comprimento_onda*1e09):.3e} em nm")
        print(f"\nFrequência: {(frequencia):.3e} em Hz")
        print(f"\nFrequência: {(frequencia/1e+12):.3e} em THz")
        
    elif entrada == 3:
        n_final = float(input("Digite o valor do número quântico final: "))
        opcao = int(input("Digite 1 para inserir a Frequência e 2 para inserir Comprimento de onda: "))
        if opcao == 1:
            variavel = float(input("Digite o valor da frequência em Hz: "))
        elif opcao == 2:
            variavel = float(input("Digite o valor do comprimento de onda em metros: "))
        n_inicial = calcular_n_inicial(n_final, opcao, variavel)
        print(f"\nNúmero quântico final: {n_inicial}")
         



















