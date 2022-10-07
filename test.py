from os import walk
import numpy as np
import cv2
from time import sleep, time
import battleList.core
from chat import chat
import hud.creatures
import hud.core
import radar.config
import radar.core
import skills.core
import utils.core
import utils.image
from PIL import Image, ImageOps
import pathlib
import timeit


def main():
    # beingAttackedCreature = None
    # corpsesToLoot = np.array([], dtype=hud.creatures.creatureType)
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot())
    stamina = skills.core.getStamina(screenshot)
    print('stamina', stamina)
    # radarCoordinate = radar.core.getCoordinate(screenshot)
    # battleListCreatures = battleList.core.getCreatures(screenshot)
    # hudCoordinate = hud.core.getCoordinate(screenshot)
    # hudImg = hud.core.getImgByCoordinate(screenshot, hudCoordinate)
    # creaturesBars = hud.creatures.getCreaturesBars(hudImg.flatten())
    # res = timeit.repeat(lambda: skills.core.getStamina(
    #     screenshot), repeat=10, number=1)
    # print(res)
    # a = new_panel.array([
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10]
    # ])
    # r = np.take(a, [[0, 1, 2], [5, 6, 7]])
    # print(r)
    # while True:
    # loop_time = time()
    # hudCreatures = hud.creatures.getCreatures(
    #     screenshot, battleListCreatures, radarCoordinate=radarCoordinate)
    # # print(hudCreatures)
    # res = battleList.core.isAttackingSomeCreature(battleListCreatures)
    # print(res)
    # battleListCreatures = battleList.core.getCreatures(screenshot)
    # break
    # timef = (time() - loop_time)
    # timef = timef if timef else 1
    # fps = 1 / timef
    # print('FPS {}'.format(fps))


if __name__ == '__main__':
    main()
