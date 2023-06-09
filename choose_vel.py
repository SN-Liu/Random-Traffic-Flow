import random

speed_range = {
    'car':{
        'free':{
            'min':60,
            'max':130
        },
        'stable':{
            'min':40,
            'max':120
        },
        'unstable':{
            'min':10,
            'max':50
        }
    },
    'van':{
        'free':{
            'min':70,
            'max':110
        },
        'stable':{
            'min':45,
            'max':95
        },
        'unstable':{
            'min':15,
            'max':45
        }
    },
    'truck':{
        'free':{
            'min':50,
            'max':90
        },
        'stable':{
            'min':20,
            'max':70
        },
        'unstable':{
            'min':0,
            'max':30
        }
    }
}

def choose(vel,type,traffic_state,character):
    min = speed_range[type][traffic_state]['min']
    max = speed_range[type][traffic_state]['max']
    segment_length_vel = (max - min)/2
    
    if character == 'Defensive':
        start_num = 0
    elif character == 'Normal':
        start_num = 0.5
    elif character == 'Aggressive':
        start_num = 1

    select_vel = []
    for i in range(len(vel)):
        if vel[i] > min + start_num*segment_length_vel and vel[i] < min + (start_num+1)*segment_length_vel:
            select_vel.append(vel[i])

    choose_data = random.choice(select_vel)

    return choose_data

