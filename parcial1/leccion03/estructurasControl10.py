# For

animales = ['Leon', 'Zebra', 'Murcielago', 'Humano']
comidas = ['Carnivoro', 'Herbivoro', 'Insectivoro', 'Omnivoro']

for animal, comida in zip(animales, comidas):
    print(f'{animal} es {comida}')