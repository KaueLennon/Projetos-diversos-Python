from poo_aulas import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.altenar_estado()
restaurante_praca.receber_avalicao('Guilherme', 10)
restaurante_praca.receber_avalicao('Lais', 8)
restaurante_praca.receber_avalicao('Joao', 2)

def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()