"""
This program does the permutations in a string
@Rjuarez

"""

def rest(principal, restando):
    for i in restando:
        if i in principal:
            temporal = principal.partition(i)
            principal = temporal[0] +temporal[2]
        else:
            return -1
            break;            
    return principal

def recursive(lista, cadena):
    old_list = lista
    new_list = list('')
    for i in old_list:
        temporal = rest(cadena,i)
        temporal = list(temporal)
        for j in temporal:
            new_list.append(i+j)
    if len(new_list[0]) < len(cadena):
        recursive(new_list, cadena)
    else:
        print(new_list)
        print(len(new_list))

    
cadena = input("Ingresa cadena: ")
lista = list(cadena)
recursive(lista, cadena)