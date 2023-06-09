import DefaultPara_PreDriver as DP
from Traffic_Dict import Traffic

#Defensive Normal Aggressive
def ReadPD(Character):
    #判断车辆类型
    if Traffic['ObjectClass'] == 'Car':
        OC = 'Car'
    else:
        OC = 'Truck'
    
    #写入纵向运动参数
    for key1 in DP.Long['Generic'][OC][Character]:
        key2 = 'AutoDrv.Long.Gen.' + key1
        if key2 in Traffic.keys():
            Traffic[key2] = DP.Long['Generic'][OC][Character][key1]

    #写入横向运动参数
    for key1 in DP.Lateral['Human_driver'][OC][Character]:
        key2 = 'AutoDrv.Lat.' + key1
        if key2 in Traffic.keys():
            Traffic[key2] = DP.Lateral['Human_driver'][OC][Character][key1]

    #写入路口决策参数
    for key1 in DP.Long_Junction[OC][Character]:
        key2 = 'AutoDrv.Long.' + key1
        if key2 in Traffic.keys():
            Traffic[key2] = DP.Long_Junction[OC][Character][key1]

    #写入变道参数
    for key1 in DP.Lane_Change[OC][Character]:
        key2 = 'AutoDrv.' + key1
        if key2 in Traffic.keys():
            Traffic[key2] = DP.Lane_Change[OC][Character][key1]

    return Traffic


