#exemplo de agrecação:

from classes import Cafeteira, Mantimentos

if __name__ == "__main__":
    print()
    
    
    recarga = Mantimentos('1000', '120')
    cafe1 = Cafeteira()
    refil1 = Mantimentos('130','20')
    
    cafe1.inserir_mantimentos(recarga)
    cafe1.verificandoQuantidades()
    
    cafe1.misturando('puro')
    cafe1.verificandoQuantidades()
    cafe1.misturando('puro')
    cafe1.verificandoQuantidades()
    cafe1.misturando('puro')
    cafe1.verificandoQuantidades()    
    cafe1.misturando('puro')
    cafe1.verificandoQuantidades()
    cafe1.inserir_mantimentos(refil1)
    print()
    cafe1.verificandoQuantidades()    
    cafe1.misturando('puro')
    cafe1.verificandoQuantidades()

  