  
def esPrimo(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
def codificar(texto):
    texto = texto.lower()
    lista = []
    for i in texto:
        lista.append(i)



    abecedario = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    i = 0
    e = 0
    while i < len(lista):
        e = 0
        if esPrimo(i) and lista[i].isalpha():
            while e < len(abecedario):
                if lista[i] == "a":
                    lista[i] = "z"
                    i +=1 
                    e = 100
                elif lista[i] == abecedario[e]:
                    lista[i] = abecedario[e - 1]
                    i += 1
                    e = 100
                else:
                    e += 1
        elif lista[i].isalpha():
            while e < len(abecedario):
                if lista[i] == "z":
                    lista[i] = "a"
                    i += 1
                    e = 100
                elif lista[i] == abecedario[e]:
                    lista[i] = abecedario[e + 1]
                    i += 1
                    e = 100
                else:
                    e += 1
        else:
            lista[i] = lista[i]
            i += 1
    lista.reverse()
    i = 0
    e = 0
    while i < len(lista):
        e = 0
        if esPrimo(i) and lista[i].isalpha():
            while e < len(abecedario):
                if lista[i] == "a":
                    lista[i] = "z"
                    i += 1
                    e = 100
                elif lista[i] == abecedario[e]:
                    lista[i] = abecedario[e - 1]
                    i += 1
                    e = 100
                else:
                    e += 1
        elif lista[i].isalpha():
            while e < len(abecedario):
                if lista[i] == "z":
                    lista[i] = "a"
                    i += 1
                    e = 100
                elif lista[i] == abecedario[e]:
                    lista[i] = abecedario[e + 1]
                    i += 1
                    e = 100
                else:
                    e += 1
        else:
            lista[i] = lista[i]
            i += 1
    lista.reverse()
   

    codigo_final = "".join(lista)
    return(codigo_final)

   


entrada = input()
salida = codificar(entrada)
print(salida)