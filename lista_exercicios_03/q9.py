def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        indice_menor = i

        for j in range(i+1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        # Trocar os elementos utilizando a variável temporária tmp
        tmp = lista[i]
        lista[i] = lista[indice_menor]
        lista[indice_menor] = tmp

lista = [7, 4, 3, 12, 8]

print("Lista original:", lista)

selection_sort(lista)

print("Lista ordenada:", lista)
