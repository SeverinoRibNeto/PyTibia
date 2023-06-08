import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
import src.repositories.inventory.core as inventoryCore
from ...typings import Context
from .common.base import BaseTask


class OpenLockerTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'openLocker'
        self.delayAfterComplete = 1

    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnoreTask = inventoryCore.isLockerOpen(context['screenshot'])
        return shouldIgnoreTask

    def do(self, context: Context) -> Context:
        slot = gameWindowCore.getSlotFromCoordinate(context['radar']['coordinate'], context['deposit']['lockerCoordinate'])
        gameWindowSlot.rightClickSlot(slot, context['gameWindow']['coordinate'])
        return context

    def did(self, context: Context) -> bool:
        return self.shouldIgnore(context)
