import math

# Constantes físicas
h = 6.62607015e-34  # Constante de Planck (J·s)
c = 2.99792458e8    # Velocidade da luz (m/s)
e = 1.602176634e-19 # Carga elementar (C)
epsilon_0 = 8.854187817e-12 # Permissividade do vácuo (F/m)
me = 9.10938356e-31 # Massa do elétron (kg)
k = 8.987551787e9   # Constante de Coulomb (N·m²/C²)

# Definições de funções
def raio_orbita(n):
    """Calcula o raio da órbita para um número quântico n."""
    r = (epsilon_0 * h**2 * n**2) / (math.pi * me * e**2)
    return r

def velocidade_eletron(n):
    """Calcula a velocidade do elétron para um número quântico n."""
    v = (e**2) / (2 * epsilon_0 * h * n)
    return v

def comprimento_onda_eletron(n):
    """Calcula o comprimento de onda de De Broglie para o elétron."""
    v = velocidade_eletron(n)
    lambda_n = h / (me * v)
    return lambda_n

def energia_cinetica(n):
    """Calcula a energia cinética do elétron para um número quântico n."""
    r = raio_orbita(n)
    K = (e**2) / (8 * math.pi * epsilon_0 * r)
    return K

def energia_potencial(n):
    """Calcula a energia potencial do elétron para um número quântico n."""
    r = raio_orbita(n)
    U = -(e**2) / (4 * math.pi * epsilon_0 * r)
    return U

def energia_total(n):
    """Calcula a energia total do elétron para um número quântico n."""
    E = energia_cinetica(n) + energia_potencial(n)
    return E

def energia_foton(n_inicial, n_final):
    """Calcula a energia do fóton absorvido ou emitido na transição."""
    E_inicial = energia_total(n_inicial)
    E_final = energia_total(n_final)
    Efoton = abs(E_inicial - E_final)
    return Efoton

def frequencia_foton(Efoton):
    """Calcula a frequência do fóton dado sua energia."""
    f = Efoton / h
    return f

def comprimento_onda_foton(Efoton):
    """Calcula o comprimento de onda do fóton dado sua energia."""
    lambda_foton = h * c / Efoton
    return lambda_foton

# Função de menu
def menu():
    print("Programa para o Estudo do Átomo de Bohr")
    print("1 - Cálculos a partir do número quântico n")
    print("2 - Cálculo da energia e comprimento de onda do fóton")
    print("3 - Encontrar n final ou n inicial a partir da energia do fóton")
    print("4 - Cálculo do fóton emitido ou absorvido")
    print("5 - Conversão de energia e comprimento de onda")
    print("0 - Sair")

def main():

    print("-------------------- AUTORES DO PROJETO --------------------")
    print("Giovanna Mendes, Guilherme Meireles, Ranielly Affonso e Natasha Almeida")
    print("Conceitos utilizados no programa: \n")
    print("O projeto foi criado para calcular as propriedades relacionadas ao átomo de Bohr.\n"
      "O software permite que o usuário insira alguns parâmetros como raio, velocidade, comprimento,\n"
      "energias e frequência")

    

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            n = int(input("Digite o número quântico n: "))
            r_n = raio_orbita(n)
            v_n = velocidade_eletron(n)
            lambda_n = comprimento_onda_eletron(n)
            K_n = energia_cinetica(n)
            U_n = energia_potencial(n)
            E_n = energia_total(n)
            
            print(f"Raio da órbita (r_n): {r_n:.3e} m")
            print(f"Velocidade do elétron (v_n): {v_n:.3e} m/s")
            print(f"Comprimento de onda do elétron (λ_n): {lambda_n:.3e} m")
            print(f"Energia cinética (K_n): {K_n:.3e} J")
            print(f"Energia potencial (U_n): {U_n:.3e} J")
            print(f"Energia total (E_n): {E_n:.3e} J")
        
        elif opcao == 2:
            n_inicial = int(input("Digite o número quântico inicial: "))
            n_final = int(input("Digite o número quântico final: "))
            Efoton = energia_foton(n_inicial, n_final)
            f_foton = frequencia_foton(Efoton)
            lambda_foton = comprimento_onda_foton(Efoton)
            
            print(f"Energia do fóton: {Efoton:.3e} J")
            print(f"Frequência do fóton: {f_foton:.3e} Hz")
            print(f"Comprimento de onda do fóton: {lambda_foton:.3e} m")
        
        elif opcao == 3:
            n_inicial = int(input("Digite o número quântico inicial ou final: "))
            f_foton = float(input("Digite a frequência do fóton absorvido: "))
            lambda_foton = comprimento_onda_foton(f_foton)
            
            print(f"Comprimento de onda do fóton absorvido: {lambda_foton:.3e} m")
        
        elif opcao == 4:
            n_inicial = int(input("Digite o número quântico inicial ou final: "))
            f_foton = float(input("Digite a frequência do fóton emitido: "))
            lambda_foton = comprimento_onda_foton(f_foton)
            
            print(f"Comprimento de onda do fóton emitido: {lambda_foton:.3e} m")
        
        elif opcao == 5:
            print("Escolha a conversão: ")
            print("A. Frequência do fóton")
            print("B. Energia do fóton")
            escolha = input("Digite A ou B: ").upper()
            
            if escolha == "A":
                f_foton = float(input("Digite a frequência do fóton: "))
                Efoton = h * f_foton
                Efoton_ev = Efoton / e
                print(f"Energia do fóton: {Efoton:.3e} J ou {Efoton_ev:.3e} eV")
            
            elif escolha == "B":
                Efoton = float(input("Digite a energia do fóton (J): "))
                lambda_foton = comprimento_onda_foton(Efoton)
                print(f"Comprimento de onda do fóton: {lambda_foton:.3e} m")
        
        elif opcao == 0:
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
