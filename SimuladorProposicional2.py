from sys import stdin

oper = {'&', '|'}
atomos_dic = {}
atomos_list = []

def remover_espacios (string: str) -> list:
    lista = list(string)
    c = 0
    while c < len(lista):
      if lista[c] == ' ':
        lista.pop(c)
      else:
        c += 1

    return lista

# liampia el diccionario y la lista para despues llenarlos con los 
# atomos respectivos y con un valor inicial de 0
def numero_atomos(prop:list) -> int:
    atomos_dic.clear
    atomos_list.clear
    for i in range(len(prop)):
      if prop[i] not in {'(', ')', '!', '&', '|'}:
        atomos_dic[prop[i]] = False
        if prop[i] not in atomos_list:
          atomos_list.append(prop[i])

            
    return len(atomos_dic)

def binario(x : int) -> str:
  x2 = ''
  if x == 0:
    x2 = '0'
  else:
    n = 0
    while 2**n <= x:
      n += 1

    for i in range(n):
      if x >= 2**(n-i-1):
        x2 += '1'
        x = x % 2**(n-i-1)
      else:
        x2 += '0'

  return x2

def V(form: list, r : int, l : int):
  if r == l: 
    ans = atomos_dic[form[r]]
  elif form[r] == '!':
    ans = not V(form, r + 1, l)
  elif form[r] == '(' and form[l] == ')': 
    cnt = 0
    i = r + 1
    md = -1
    while i < l and md == -1:
      if form[i] == '(':
        cnt += 1
      elif form[i] == ')':
        cnt -= 1
      if form[i] in oper and cnt == 0:
        md = i
      i += 1

    if form[md] == '&':
      ans = V(form, r + 1, md - 1) and V(form, md + 1, l - 1)
    elif form[md] == '|':
      ans = V(form, r + 1, md - 1) or V(form, md + 1, l - 1)

  return ans

def elementos_iguales(lista: list) -> int:
  if lista[0] == True:
    x = 1
  elif lista [0] == False:
    x = 0
  for i in range(len(lista)):
    if lista[0] != lista[i]:
      x = -1
  
  return x

# cantidad de formulas a evaluar
cdfae = int(stdin.readline())

for i in range(cdfae):
  prop = remover_espacios(str(stdin.readline().strip()))
  na = numero_atomos(prop)
  resultados_atomos_dic = []
  
  a = 0
  while a < 2**na:
    abin = list(binario(a))[:: -1]
    while len(abin) < na:
      abin.append(0)
    for j in range(na):
      atomos_dic[atomos_list[j]] = bool(int(abin[j]))
    resultados_atomos_dic.append(V(prop, 0, len(prop)-1))
    a += 1

  print(elementos_iguales(resultados_atomos_dic))