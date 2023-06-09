import os
from Traffic_Dict import Traffic

def ReadOb(objinfo_name):

    folder_path=r"C:\IPG\carmaker\win64-11.1.2\Movie\3D\Vehicles"
    # 获取文件夹中所有文件的列表
    file_list = os.listdir(folder_path)
    # 过滤出后缀名为.obj的文件名
    obj_files = [filename for filename in file_list if filename.endswith(".obj")]

    key = objinfo_name.split('.')[0]
    key = key + '.obj'
    if key in obj_files:
        movie_geometry = key
    else:
        movie_geometry = objinfo_name.replace('objinfo','mobj')

    Traffic['Movie.Geometry'] = '3D/Vehicles/' + movie_geometry

    #获取objinfo文件路径

    objinfo_file_path = os.path.join(folder_path, objinfo_name)

    objinfo_dict={}

    #打开objinfo文件
    with open(objinfo_file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                key = key.replace('Traffic.','')
                objinfo_dict[key.strip()] = value.strip('\n')
        for key in Traffic:
            if key in objinfo_dict.keys():
                Traffic[key] = objinfo_dict[key]

        return Traffic


    
    
