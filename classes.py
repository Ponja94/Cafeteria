
class Cafeteira:
    def __init__(self):
        self.mantimentos = []
        self.tem_mantimentos = False
                
    def inserir_mantimentos(self, refil):
        if self.mantimentos == []:
            self.mantimentos.append(refil)
            self.tem_mantimentos = True
            print(f'Foi adicionado pela primeira vez na máquina')
            return 
        
        for mantimento in self.mantimentos:
            mantimento.agua = int(mantimento.agua) + int(refil.agua)
            mantimento.cafe = int(mantimento.cafe) + int(refil.cafe)
            print(f'foi adicionado novos mantimentos')
        
        
    def verificandoQuantidades(self):
        for mantimento in self.mantimentos:
            if int(mantimento.agua) <= 300:
                self.tem_mantimentos == False
                print(f'Favor adicionar água, temos apenas temos {mantimento.agua} ml de água.')
                return
                 
            if int(mantimento.cafe) <= 100:
                self.tem_mantimentos == False 
                print(f'Favor adicionar café, temos apenas {mantimento.cafe} g de café.')
                print(f'Favor adicionar água, temos apenas temos {mantimento.agua} ml de água.')
                
                return

        print(f'Temos mantimentos para fazer o café.')
    
    def misturando(self, pedido):
        self.pedido = pedido
        if self.tem_mantimentos == True:
            if pedido.lower() == 'puro':
                for mantimento in self.mantimentos:
                    mantimento.agua = int(mantimento.agua) - 200
                    mantimento.cafe = int(mantimento.cafe) - 20
                
            elif pedido.lower() == 'pingado':
                for mantimento in self.mantimentos:
                    mantimento.agua = int(mantimento.agua) - 100
                    mantimento.cafe = int(mantimento.cafe) - 10
                
            print(f'Seu café {pedido.capitalize()} está pronto. //Sobou {mantimento.agua} ml de água e {mantimento.cafe} g de pó de café//')
            return
            
        if self.tem_mantimentos == False:
            print('Favor verificar se tem mantimentos para o seu café.')
        
    
class Mantimentos:
    def __init__(self, agua, cafe): # ml, g
        self.agua = agua
        self.cafe = cafe

    
    def setando(self):
        print('setado')
    
    
    