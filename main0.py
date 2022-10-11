import readchar
import string
import random
from termcolor import colored








def generate_letter():
  letter=random.choice(string.ascii_lowercase)
  return letter

def read_letter():
  key = readchar.readkey()
  return key


def play():
  g = generate_letter()
  print("Type letter " + colored(str(g), 'blue'))
  r = read_letter()
  if str(g) == str(r):
    print("You typed letter " + colored(str(r), 'green'))
    return True
  else:
    print("You typed letter " + colored(str(r), 'red'))
    return  False







def main():
  nmax=int(input("Máximos inputs..."))
  i=0
  acertos=0
  erros=0
  while i < nmax:
    if play():
      acertos+=1
    else:
      erros+=1
    i+=1
  print("Acertos: "+str(acertos))
  print("Erros: "+str(erros))



if __name__=="__main__":
  main()
