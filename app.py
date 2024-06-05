from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.receber_avaliacao("Pedro", 10)
restaurante_praca.receber_avaliacao("Miguel", 3)
restaurante_praca.receber_avaliacao("Giovanna", 5)




def main():
    Restaurante.listar_restaurante()
    

if __name__ == "__main__":
    main()