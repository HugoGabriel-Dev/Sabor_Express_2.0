from restaurantes import Restaurante

def main():
    restaurante1 = Restaurante('restaurante A', 'italiana')

    restaurante1.receber_avaliacao('Hugo', 8)

    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()