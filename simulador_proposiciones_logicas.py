# Autor: Juan Andrés Correa Arenas

from sys import stdin
# & = conjunción(AND) , | = disyunción(OR)
oper = {'&', '|'}
atomos = {}

def remover_espacios (string: str) -> list:
    lista = list(string)
    c = 0
    while c < len(lista):
        if lista[c] == ' ':
            lista.pop(c)
        else:
            c += 1

    return(lista)

def invalida(propo: list) -> bool:
  p = propo.copy()
  c = 0
  while c < len(p):
    if p[c] != '(' and p[c] != ')':
      p.pop(c)
    else:
      c += 1

  c = 1
  while c < len(p):
    if p[c] == ')' and p[c-1] == '(':
      p.pop(c)
      p.pop(c-1)
      c = 1
    else:
      c += 1

  if len(p)==0:
    r = True
  elif len(p) > 0:
    r = False

  return(r)

def V(form: list, r : int, l : int):
  if r == l: 
    ans = atomos[form[r]]
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
  
no = int(stdin.readline())
for i in range (no):
    atomo = remover_espacios(str(stdin.readline().strip()))
    atomos[atomo[0]] = bool(int(atomo[-1]))

cdfae = int(stdin.readline())

for i in range(cdfae):
    prop = remover_espacios(str(stdin.readline().strip()))
    if not invalida(prop):
      print(-1)
    else:
      ans = V(prop, 0, len(prop)-1)
      if ans:
        print(1)
      else:
        print(0)