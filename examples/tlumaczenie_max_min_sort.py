import copy


def sorted_custom(lista,key=None):
    nowa_list = copy.copy(lista)
    if key is not None:
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if key(nowa_list[j]) > key(nowa_list[j + 1]):
                    nowa_list[j], nowa_list[j + 1] = nowa_list[j + 1], nowa_list[j]
    else:
        n = len(lista)
        for i in range(n):
            for j in range(0,n-i-1):
                if nowa_list[j] > nowa_list[j+1]:
                    nowa_list[j],nowa_list[j+1] = nowa_list[j+1],nowa_list[j]

    return nowa_list


def custom_max(lista,key=None):
    if key is not None:
        max_value = lista[0]
        for element in lista:
            if key(element) > key(max_value):
                max_value = element

        return max_value
    else:
        max_value = lista[0]
        for element in lista:
            if element > max_value:
                max_value = element

        return max_value



#print(sorted_custom([2,3,1,4,5,2]))
#[1,2,2,3,4,5]

print(custom_max([2,3,1,4,5,2],key=lambda x: -x))