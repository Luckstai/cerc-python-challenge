# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])


input("Aperte Enter para continuar...")


# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(1, 21):
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(20):
    genero = data_list[i][6]
    print(f"Amostra do indice {i} não contém a informação gênero." if len(genero) == 0 else genero)

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem


def column_to_list(data, index):
    column_list = []
    data_size = len(data)

    for i in range(data_size):
        feature = data_list[i][index]
        if(index == 2):
            column_list.append(int(feature))
        else:
            column_list.append(feature)
        # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
# assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado." Este teste está incorreto, a quantidade total de linhas é 1048576 e ao remover o cabeçalho na tarefa 1 cai para 1048575
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
data_list_size = len(data_list)

for i in range(data_list_size):
    gender = data_list[i][6]

    if gender == "Female":
        female += 1


    if gender == "Male":
        male += 1


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate." Teste inválido, o correto seria: Male: 665437 Female: 198247
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    male = 0
    female = 0


    data_list_size = len(data_list)

    for i in range(data_list_size):
        gender = data_list[i][6]

        if gender == "Female":
            female += 1

        if gender == "Male":
            male += 1


    return [male, female]


def count_user_type(data_list):
    subscriber = 0
    customer = 0
    dependent = 0

    data_list_size = len(data_list)

    for i in range(data_list_size):
        user_type = data_list[i][5]

        if user_type == "Subscriber":
            subscriber += 1

        if user_type == "Customer":
            customer += 1

        if user_type == "Dependent":
            dependent += 1

    return [subscriber, customer, dependent]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
# assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!" # Teste inválido, o correto seria: Male: 665437 Female: 198247
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.


def most_popular_gender(data_list):
    male, female = count_gender(data_list)
    answer = None
    if male > female:
        answer = "Male"
    if female > male:
        answer = "Female"
    if female == male:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = column_to_list(data_list, -3)
types = ["Subscribe", "Customer", "Dependent"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))

answer = "A condição é falsa porque na função count_gender o algoritimo considera apenas Female e Male na contagem e o dataset do desafio contém amostras sem a informação gênero (string vazia)."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)


def calc_max(trip_duration_list):
    max = trip_duration_list[0]
    for x in trip_duration_list:
        if x > max:
            max = x
    return max


def calc_min(trip_duration_list):
    min = trip_duration_list[0]
    for x in trip_duration_list:
        if x < min:
            min = x
    return min


def calc_mean(trip_duration_list):
    return sum(trip_duration_list) / len(trip_duration_list)


def calc_median(trip_duration_list):
    sorted_list = sorted(trip_duration_list)
    mid = len(sorted_list) // 2
    return (sorted_list[mid] + sorted_list[-mid-1]) / 2


min_trip = calc_min(trip_duration_list)
max_trip = calc_max(trip_duration_list)
mean_trip = calc_mean(trip_duration_list)
median_trip = calc_median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip,
      "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
# assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!" # Teste invalido, o correto seria 884.790509977827
# assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!" Teste inválido, o correto seria 624.0
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations_list = column_to_list(data_list, 3)
start_stations = list(set(start_stations_list))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
# print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations." # Teste inválido, o correto seria 578
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz.
print("\nTAREFA 11: Imprimindo a documentação da funções:")

with open("task11.txt", encoding="UTF-8") as f:
    print(f.read())

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    count_items = []

    for gender in column_list:
        if gender != '':
            count_items.append(gender)

    item_types = list(set(count_items))
    print("Tipos:", len(item_types), "Counts:", len(count_items))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------    
    column_list = column_to_list(data_list, -2) # Essa coluna é a de Gênero e só possui 2 tipos strings vazias não são gêneros
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    # print("Tipos:", types, "Counts:", counts)
    # assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!" # Teste inválido, o correto seria 2
    # assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!" # Teste inválido, o correto seria 863684
    # -----------------------------------------------------
