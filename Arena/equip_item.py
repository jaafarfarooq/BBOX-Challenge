from asyncio.windows_events import NULL
def equip_item(knight,item):
    knight.attack+=item.attack
    knight.defence+=item.defence
    knight.item=item
    item.equipped=True
    item.position=NULL
    item.Knight=knight