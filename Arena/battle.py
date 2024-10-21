from asyncio.windows_events import NULL


def battle(attacker,defender):
    """_summary_

    Args:
        attacker (_type_): _description_
        defender (_type_): _description_
    """
    attacker.attack+=0.5
    if attacker.attack>defender.defence:
        #[null,"DROWNED",null,0,0]
        if defender.item is not NULL:
            defender.item.position=defender.position
            defender.item.equipped=False
            defender.item.Knight=NULL
        defender.position=NULL
        defender.status='DEAD'
        defender.item=NULL
        defender.attack=0
        defender.defence=0
        attacker.attack-=0.5

    else:
        if attacker.item is not NULL:
            attacker.item.position=attacker.position
            attacker.item.equipped=False
            attacker.item.Knight=NULL
        attacker.position=NULL
        attacker.status='DEAD'
        attacker.item=NULL
        attacker.attack=0
        attacker.defence=0
