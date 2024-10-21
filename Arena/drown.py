from asyncio.windows_events import NULL

def drowned(knight):
    if knight.item is not NULL:
        knight.item.position=knight.position
        knight.item.equipped=False
        knight.item.Knight=NULL
    knight.position=NULL
    knight.status='DROWNED'
    knight.item=NULL
    knight.attack=0
    knight.defence=0