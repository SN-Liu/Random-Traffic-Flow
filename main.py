from Traffic_Dict import Traffic
import Read_ob
import Read_PreDriver
from HDM_Expert_param import HDM_Expert
import random
import pandas as pd
from scipy.stats import weibull_min
import numpy as np
import matplotlib.pyplot as plt
from noise_data import noise_data_dict
from choose_vel import choose

#获取车道数量以及车道长度
with open('autonomous_parameters_test','r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith('Road.nRoutes'):
            key, value = line.split('=')
            lane_number = int(value.strip())
        if line.startswith('Road.RoadNetworkLength'):
            key, value = line.split('=')
            lane_length = float(value.strip())

#交通目标数量
Traffic_Number = 200

#车辆密度
density = (Traffic_Number * 1609) /(lane_length * lane_number)
flow_state = ''
if density < 12:
    flow_state = 'free'
elif density > 12 and density < 30:
    flow_state = 'stable'
elif density > 30 :
    flow_state = 'unstable'
print(flow_state)

#交通流部分内容
traffic_segment = {
    'ob_name':'',
    'character':'',
    'class':'',
    'lane':'',
    'velocity':'',
    'position':''
}

traffic_segment_list = []

for i in range(Traffic_Number):
    traffic_segment_list.append(traffic_segment.copy())


#交通目标种类（小客车\小货车\大货车&大客车）
Traffic_object_P ={
    'Car':0.55,         #小客车
    'Van':0.2,          #小货车
    'Truck':0.25        #大货车&大客车
}

Traffic_object_list = []

df = pd.read_excel('Traffic_object_class_highway.xlsx')
col_car = df['Car']
col_van = df['Van'].dropna(axis=0)
col_truck = df['Truck'].dropna(axis=0)


for key in Traffic_object_P:
    for i in range(round(Traffic_Number*Traffic_object_P[key])):
        if key == 'Car':
            Traffic_object_list.append(random.choice(col_car))
        elif key == 'Van':
            Traffic_object_list.append(random.choice(col_van))
        elif key == 'Truck':
            Traffic_object_list.append(random.choice(col_truck))

if len(Traffic_object_list) != Traffic_Number:
    Traffic_object_list.append(random.choice(col_car))
    
random.shuffle(Traffic_object_list)


#三种交通流
Traffic_driver_P = {
    'Defensive' :{
        'Pa':0.2,       #激进型驾驶员占比
        'Pn':0.1,       #普通型驾驶员占比
        'Pc':0.7        #保守型驾驶员占比
    },
    'Normal':{
        'Pa':0.2,
        'Pn':0.5,
        'Pc':0.3
    },
    'Aggressive':{
        'Pa':0.7,
        'Pn':0.2,
        'Pc':0.1
    }
}
#定义交通流种类
Traffic_characters = 'Aggressive'

#三种驾驶员性格
Driver_characters = ['Defensive','Normal','Aggressive']
Driver_characters_list = []

for key in Traffic_driver_P[Traffic_characters]:
    for i in range(round(Traffic_Number*Traffic_driver_P[Traffic_characters][key])):
        Driver_characters_list.append(random.choice(Driver_characters))

if len(Driver_characters_list) != Traffic_Number:
    Driver_characters_list.append(random.choice(Driver_characters))
random.shuffle(Driver_characters_list)
#print(Driver_characters_list)


#车速分布
#weibull参数字典
Weibull_para = {
    'free' : {
        'shape':11.48,
        'scale':77.6,
        'location':20.7
    },
    'stable': {
        'shape':4.021,
        'scale':88,
        'location':-12.71
    },
    'unstable': {
        'shape':2.937,
        'scale':28,
        'location':-4.779
    }
}

speed_range = {
    'free':{
        'start': 40,
        'end': 140
    },
    'stable':{
        'start':20,
        'end':130
    },
    'unstable':{
        'start':0,
        'end':70
    }
}

shape = Weibull_para[flow_state]['shape']           #形状参数
scale = Weibull_para[flow_state]['scale']            #比例参数
location = Weibull_para[flow_state]['location']         #位置参数
print(shape)
print(scale)
print(location)

start = speed_range[flow_state]['start']
end = speed_range[flow_state]['end']

#weibull分布
def weibull_pdf(x):
    return weibull_min.pdf((x - location) / scale, shape) / scale

#车速分布函数
def velocity_distribution(number):
    x = np.linspace(start,end,10000)

    # 计算累积分布函数（CDF）
    cdf = np.cumsum(weibull_pdf(x))
    cdf /= cdf[-1]

    # 生成均匀分布的随机数
    u = np.random.random(number)

    # 使用逆函数将随机数转换为符合给定分布的数据
    return np.interp(u, cdf, np.linspace(start, end, len(cdf)))



#车道分布(根据车辆类型随机分布车道)
#车速分配 自由流：
#        稳定流：
#        拥挤流：

velocity_all = velocity_distribution(number= 10*Traffic_Number)
velocity_all_copy = velocity_all.tolist()
print(velocity_all_copy)
# 创建第二个子图
plt.hist(velocity_all, bins=30, density=True, alpha=0.7)
plt.xlabel('x2')
plt.ylabel('Probability')
plt.title('Data Generated from Weibull Distribution')
plt.grid(True)
plt.show()



for i in range(len(Traffic_object_list)):
    traffic_segment_list[i]['ob_name'] = Traffic_object_list[i]
    traffic_segment_list[i]['character'] = Driver_characters_list[i]

    if Traffic_object_list[i] in col_car.values:
        traffic_segment_list[i]['class'] = 'car'
        traffic_segment_list[i]['lane'] = random.choices(range(0,lane_number),[2,2,1,1],k=1)[0]
        vel_temp = choose(velocity_all_copy,'car',flow_state,traffic_segment_list[i]['character'])
        traffic_segment_list[i]['velocity'] = vel_temp
        velocity_all_copy.remove(vel_temp)
        
    if Traffic_object_list[i] in col_van.values:
        traffic_segment_list[i]['class']='van'
        traffic_segment_list[i]['lane'] = random.choice(range(0,lane_number))
        vel_temp = choose(velocity_all_copy,'van',flow_state,traffic_segment_list[i]['character'])
        traffic_segment_list[i]['velocity'] = vel_temp
        velocity_all_copy.remove(vel_temp)       

    if Traffic_object_list[i] in col_truck.values:
        traffic_segment_list[i]['class']='truck'
        traffic_segment_list[i]['lane'] = random.choice(range(lane_number-2,lane_number))
        vel_temp = choose(velocity_all_copy,'truck',flow_state,traffic_segment_list[i]['character'])
        traffic_segment_list[i]['velocity'] = vel_temp
        velocity_all_copy.remove(vel_temp)
        
print(len(velocity_all))
print(len(velocity_all_copy))

#在车道中的位置分布
lane_carnum = [0] * lane_number
segment_length = [0] * lane_number


for i in range(Traffic_Number):
    for j in range(lane_number):
        if traffic_segment_list[i]['lane'] == j:
            lane_carnum[j] += 1

for i in range(lane_number):
    if lane_carnum[i] != 0:
        segment_length[i] = lane_length/lane_carnum[i]
    elif lane_carnum[i] == 0:
        segment_length[i] = lane_length

#以 “与前车的车间时距小于0.7s” 为判断依据，判断车辆初始位置是否合理
#同时需判断车辆是否超出地图

headway = 0.7

for j in range(lane_number):
    count = 0
    position = [0] * max(lane_carnum)
    for i in range(Traffic_Number):
        if traffic_segment_list[i]['class'] == 'car':
            car_length = 6
        elif traffic_segment_list[i]['class'] == 'van':
             car_length = 8
        elif traffic_segment_list[i]['class'] == 'truck':
            car_length = 20
        if traffic_segment_list[i]['lane'] == j:
            if count == 0:
                position[count] = random.uniform(lane_length-(count+1)*segment_length[j], lane_length - count*segment_length[j] - car_length)
            if count != 0:
                #先判断是否能满足0.7s的车头时距
                if (position[count-1] - (lane_length-(count+1)*segment_length[j]) - car_length)/traffic_segment_list[i]['velocity'] < headway :
                    position[count] = lane_length-(count+1)*segment_length[j]
                else:
                    position[count] = random.uniform(lane_length-(count+1)*segment_length[j], lane_length - count*segment_length[j])
                    while (position[count-1]-position[count])/traffic_segment_list[i]['velocity'] < headway :
                        position[count] = random.uniform(lane_length-(count+1)*segment_length[j], lane_length - count*segment_length[j])
            traffic_segment_list[i]['position'] = position[count]
            count += 1

        
for i in range(Traffic_Number):
    print(traffic_segment_list[i])



#将traffic信息写入txt文件中
with open('Traffic.txt','w') as file:
    file.write(f'Traffic.IFF.FName = \n')
    file.write(f'Traffic.IFF.Time.Name = \n')
    file.write(f'Traffic.N = {Traffic_Number}\n')
    file.write(f'Traffic.SpeedUnit = kmh\n')
    for i in range(Traffic_Number):
        Traffic = Read_ob.ReadOb(objinfo_name=traffic_segment_list[i]['ob_name'])
        Traffic = Read_PreDriver.ReadPD(Driver_characters_list[i])
        for key in Traffic:
            if key == 'Name':
                Traffic[key] = 'T'+str(i)
            elif key == 'Info':
                Traffic[key] = 'UNNAMED Object '+ str(i)
            elif key == 'Route':
                Traffic[key] = str(traffic_segment_list[i]['lane']) + ' 1'
            elif key == 'StartPos':
                Traffic[key] = str(traffic_segment_list[i]['position']) + ' 0'
            elif key == 'Init.v':
                Traffic[key] = str(traffic_segment_list[i]['velocity'])

        #使车辆动力学性能、autonomous driving的参数 在±5%范围内扰动
        for j in range(len(noise_data_dict)):
            if noise_data_dict[j] in Traffic.keys():
                key = float(Traffic[noise_data_dict[j]])
                key = key + random.uniform(-0.05*key,0.05*key)
                Traffic[noise_data_dict[j]] = key

        junction_param = Traffic['AutoDrv.Long.Junction.Param'].split() 
        if len(junction_param) == 3:
            for j in range(len(junction_param)):
                key = float(junction_param[j])
                key = key + random.uniform(-0.05*key,0.05*key)
                junction_param[j] = key
        value = '' 
        for j in range(len(junction_param)):
            value = value + str(junction_param[j]) + ' '
        Traffic['AutoDrv.Long.Junction.Param'] =  value

        HDMbased_param = Traffic['AutoDrv.Lat.HDMbased.Param'].split() 
        if len(HDMbased_param) == 5:
            for j in range(len(HDMbased_param)):
                key = float(HDMbased_param[j])
                key = key + random.uniform(-0.05*key,0.05*key)
                HDMbased_param[j] = key
        value = '' 
        for j in range(len(HDMbased_param)):
            value = value + str(HDMbased_param[j]) + ' '
        Traffic['AutoDrv.Lat.HDMbased.Param'] =  value

        
        for key in Traffic:
            file.write(f'Traffic.{i}.{key} = {Traffic[key]}\n')
    
    for key1 in HDM_Expert:
        for key2 in HDM_Expert[key1]:
            file.write(f'Traffic.AutoDrv.{key1}.{key2} = {HDM_Expert[key1][key2]}\n')

#读取testrun并修改其中的traffic信息
with open('autonomous_parameters_test','r') as file:
    c = 0
    lines = file.readlines()
    for line in lines:
        c+= 1
        if line.startswith('Traffic'):
            break
    new_testrun = []
    a = 0
    for line in lines: 
        a+=1
        if a==c:
            with open ('Traffic.txt','r') as f:
                traffic_lines = f.readlines()
                for traffic_line in traffic_lines:
                    new_testrun.append(traffic_line)

        if not line.startswith('Traffic'):
            new_testrun.append(line)

with open('NewTestRun','w') as file:
    file.writelines(new_testrun)

# 绘制生成的数据的直方图
samples = []
for i in range(Traffic_Number):
    samples.append(traffic_segment_list[i]['velocity'])
plt.subplot(2, 1, 1)  # 创建第一个子图
plt.hist(samples, bins=30, density=True, alpha=0.7)
plt.xlabel('x1')
plt.ylabel('Probability')
plt.title('Data Generated from Weibull Distribution')

plt.subplot(2, 1, 2)  # 创建第二个子图
plt.hist(velocity_all, bins=30, density=True, alpha=0.7)
plt.xlabel('x2')
plt.ylabel('Probability')
plt.title('Data Generated from Weibull Distribution')

plt.grid(True)
plt.show()

