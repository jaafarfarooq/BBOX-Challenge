from asyncio.windows_events import NULL
import Knights_Items.Knight as Knight
import Knights_Items.Item as Item
import Arena.battle as battle
import Arena.equip_item as equip_item
import Arena.drown as drown
import file_read.file_reader as file_read
import file_write.file_writer as file_writer
if __name__ == '__main__':
    totalMoves=file_read.file_reader()
    Knights={'R' :Knight.Knight('red', [0,0],"LIVE" , NULL , 1 ,1) , 'G':Knight.Knight('green',[7,7],"LIVE",NULL,1,1),'B':Knight.Knight('blue',[7,0],"LIVE",NULL,1,1),'Y':Knight.Knight('yellow',[0,7],"LIVE",NULL,1,1)}
    items={'A' :Item.Item('axe',[2,2],False,2,0,NULL),'D':Item.Item('dagger',[2,5],False,1,0,NULL),'M':Item.Item('magic_stuff',[5,2],False,1,1,NULL),'H':Item.Item('helmet',[5,5],False,0,1,NULL)}
    moves={'N': [-1,0],'E': [0,1],'S':[1,0],'W':[0,-1]}
    for move in totalMoves:
        temp=[Knights[move[0]].position[0]+moves[move[1]][0],Knights[move[0]].position[1]+moves[move[1]][1]]
        if(temp[0]<0 or temp[0]>7 or temp[1]<0 or temp[1]>7):
            drown.drowned(Knights[move[0]])
            continue
        
        if (temp in [items['A'].position, items['D'].position, items['M'].position, items['H'].position]) and (Knights[move[0]].item is NULL) :
            for i in ['A','M','D','H']:
                if items[i].position == temp:
                    print('Item equipped '+i + ' by '+ Knights[move[0]].name)
                    equip_item.equip_item(Knights[move[0]],items[i])
                    break
        
        if temp in [Knights['R'].position ,Knights['G'].position ,Knights['B'].position ,Knights['Y'].position]:
            #Knights[move[0]].position=temp
            for k in Knights:
                if Knights[k].position==temp:
                    Knights[move[0]].position=temp
                    print('Battle bw '+ Knights[move[0]].name + ' and '+ Knights[k].name)
                    battle.battle( Knights[move[0]], Knights[k])
                    break
            continue
        
        Knights[move[0]].position=temp
    file_writer.file_write(Knights,items)