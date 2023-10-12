count = 0
def node0(arr):
    return arr.index(0)

def nodeX(arr,n):
    return arr.index(n)

def movetop(arr):
    pos0 = node0(arr)
    aux = arr[pos0-3]
    arr[pos0-3] = 0
    arr [pos0] = aux
    global count
    count += 1
    imprimir(arr)
    return arr

def movebottom(arr):
    pos0 = node0(arr)
    aux = arr[pos0+3]
    arr[pos0+3] = 0
    arr [pos0] = aux
    global count
    count += 1
    imprimir(arr)
    return arr

def moveleft(arr):
    pos0 = node0(arr)
    aux = arr[pos0-1]
    arr[pos0-1] = 0
    arr [pos0] = aux
    global count
    count += 1
    imprimir(arr)
    return arr

def moveright(arr):
    pos0 = node0(arr)
    aux = arr[pos0+1]
    arr[pos0+1] = 0
    arr [pos0] = aux
    global count
    count += 1
    imprimir(arr)
    return arr

def imprimir(arr):
    print(arr[0],arr[1],arr[2])
    print(arr[3],arr[4],arr[5])
    print(arr[6],arr[7],arr[8])
    print("-----------------------")
    return 0
ordenini = [7,2,4,5,0,6,8,3,1]

movetop(ordenini)
moveleft(ordenini)
movebottom(ordenini)
movebottom(ordenini)
moveright(ordenini)
movetop(ordenini)
movetop(ordenini)
moveleft(ordenini)
movebottom(ordenini)
movebottom(ordenini)
moveright(ordenini)
movetop(ordenini)
print("Movimientos: ",count)
