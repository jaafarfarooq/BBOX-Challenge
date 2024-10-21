import json
from asyncio.windows_events import NULL

from sqlalchemy import null
def file_write(Knights,items):
    dict={}
    write_file=open("data_source_files/final_state.json","w")
    for knight in Knights:
        #print(Knights[knight].name+' : ['+str(Knights[knight].position)+','+Knights[knight].status+','+str(Knights[knight].attack)+','+str(Knights[knight].defence)+']')
        if Knights[knight].item is not NULL:
            dict[Knights[knight].name]=[Knights[knight].position,Knights[knight].status,Knights[knight].item.name,Knights[knight].attack,Knights[knight].defence]
        else:
            if Knights[knight].status not in ["DEAD","DROWNED"]:
                dict[Knights[knight].name]=[Knights[knight].position,Knights[knight].status,'null',Knights[knight].attack,Knights[knight].defence]
            else:
                dict[Knights[knight].name]=['null',Knights[knight].status,'null',Knights[knight].attack,Knights[knight].defence]
    for item in items:
        #print(items[item].name+' : ['+str(items[item].position)+','+str(items[item].equipped))
        if items[item].Knight is not NULL:
            dict[items[item].name]=[items[item].Knight.position,items[item].equipped]
        else:
            dict[items[item].name]=[items[item].position,items[item].equipped]
    json.dump(dict, write_file,indent=4)
    del dict
    write_file.close()