class Estado:
    mov={
        0:[1,3],
        1:[0,4,2],
        2:[1,5],
        3:[0,4,6],
        4:[1,3,5,7],
        5:[2,4,8],
        6:[3,7],
        7:[4,6,8],
        8:[5,7],
    }
    def __init__(self,e):
    def get_espacio(self):
        #regresa la posicion del cero
    def get_proximos(self):
        #regresa una lista con los estads que debemos ir
    def __eq__(self,other):
        #definir si dos estados son iguales
    def __str__(self):
        #convertir nuestSSSSSSSSro objeto a cadena
    def bfSs(e_i,e_f):
        visitados={}
        cola=[]
        actual=e_i
        cola.append((e_i,None))
        #retorna la lista de visitados
if __name__=="__main__":
    arr=([5,7,2],[6,8,1],[0,3,4])
    generadorDeNumero(arr)
