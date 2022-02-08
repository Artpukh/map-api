import requests

import os
import sys

import pygame
import requests
spn = 65
map_request = f"http://static-maps.yandex.ru/1.x/?ll=-14.96952040,40.1680&spn={spn},{spn}&l=map"

response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


def mash(spn):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll=-14.96952040,40.1680&spn={spn},{spn}&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))





# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if spn < 1:
                    spn += 0.05
                elif spn < 10:
                    spn += 1
                elif spn > 80:
                    pass
                else:
                    spn += 5
                mash(spn)
            elif event.key == pygame.K_PAGEDOWN:
                if spn < 2 and spn > 0.1:
                    spn -= 0.05
                elif spn < 10 and spn >= 2:
                    spn -= 1
                elif spn <= 0.1:
                    pass
                else:
                    spn -= 10
                mash(spn)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()

pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
