from restaurantes import Restaurante

def main():
    restaurante1 = Restaurante('restaurante A', 'italiana')
    restaurante2 = Restaurante('restaurante B', 'chinesa')

    restaurante1.alternar_estado()

    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()