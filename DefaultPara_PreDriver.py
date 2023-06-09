Long = {
    'Generic': {
        'Car':{
            'Defensive':{
                'DistPreview': '200',              ##Default 200
                'DistStand':'6.0',
                'AccMax':'1.0',
                'DecComf': '-1.0',
                'PCtrlSpd':'0.25',
                'TimeGap': '2.0',
                'TAdaptDist': '6.0',
                'TAdaptRelSpd_low': '4.0',
                'TAdaptRelSpd_high':'2.0',
                'RelSpdRef': '1.0',             #Default 1.0
                'DecMax': '-10.0'               #Default -10
            },
            'Normal':{
                'DistPreview': '200',              ##Default 200
                'DistStand':'3.0',
                'AccMax':'2.0',
                'DecComf': '-2.0',
                'PCtrlSpd':'0.41',
                'TimeGap': '1.5',
                'TAdaptDist': '4.0',
                'TAdaptRelSpd_low': '2.6',
                'TAdaptRelSpd_high':'1.3',
                'RelSpdRef': '1.0',             #Default 1.0
                'DecMax': '-10.0'               #Default -10
            },
            'Aggressive':{
                'DistPreview': '200',              ##Default 200
                'DistStand':'1.5',
                'AccMax':'4.0',
                'DecComf': '-3.0',
                'PCtrlSpd':'0.55',
                'TimeGap': '1.0',
                'TAdaptDist': '2.0',
                'TAdaptRelSpd_low': '1.5',
                'TAdaptRelSpd_high':'0.8',
                'RelSpdRef': '1.0',             #Default 1.0
                'DecMax': '-10.0'               #Default -10
            }
        },
        'Truck': {
            'Defensive':{
                'DistPreview': '200',              ##Default 200
                'DistStand':'8.0',
                'AccMax':'0.8',
                'DecComf': '-0.8',
                'PCtrlSpd':'0.2',
                'TimeGap': '2.5',
                'TAdaptDist': '8.0',
                'TAdaptRelSpd_low': '5.0',
                'TAdaptRelSpd_high':'3.0',
                'RelSpdRef': '1.0',             #Default 1.0
                'DecMax': '-10.0'               #Default -10
            },
            'Normal':{
                'DistPreview': '200',              ##Default 200
                'DistStand':'4.5',
                'AccMax':'1.5',
                'DecComf': '-1.5',
                'PCtrlSpd':'0.35',
                'TimeGap': '1.75',
                'TAdaptDist': '5.0',
                'TAdaptRelSpd_low': '3.2',
                'TAdaptRelSpd_high':'1.7',
                'RelSpdRef': '1.0',             #Default 1.0
                'DecMax': '-10.0'               #Default -10
            },
            'Aggressive':{
                'DistPreview': '200',              ##Default 200
                'DistStand':'2.0',
                'AccMax':'2.5',
                'DecComf': '-2.5',
                'PCtrlSpd':'0.45',
                'TimeGap': '1.25',
                'TAdaptDist': '3.0',
                'TAdaptRelSpd_low': '2.0',
                'TAdaptRelSpd_high':'1.0',
                'RelSpdRef': '1.0',             #Default 1.0
                'DecMax': '-10.0'               #Default -10
            }
        }
        
    }
}

Lateral = {
    'Human_driver':{
        'Car': {
            'Defensive':{
                'HDMbased.Mode':'1 1',
                'HDMbased.AsymMode': 'ByCountry',
                'HDMbased.Param':'0.6 0.8 0.3 0.8 0.7 0.7'
            },
            'Normal':{
                'HDMbased.Mode':'1 1',
                'HDMbased.AsymMode': 'ByCountry',
                'HDMbased.Param':'0.4 0.5 0.5 0.5 0.5 0.5'
            },
            'Aggressive': {
                'HDMbased.Mode':'1 1',
                'HDMbased.AsymMode': 'ByCountry',
                'HDMbased.Param':'0.2 0.3 0.7 0.3 0.3 0.3'
            }
        },
        'Truck': {
            'Defensive':{
                'HDMbased.Mode':'1 1',
                'HDMbased.AsymMode': 'ByCountry',
                'HDMbased.Param':'0.8 0.8 0.2 0.8 0.8 0.8'
            },
            'Normal':{
                'HDMbased.Mode':'1 1',
                'HDMbased.AsymMode': 'ByCountry',
                'HDMbased.Param':'0.6 0.3 0.3 0.6 0.6 0.6'
            },
            'Aggressive': {
                'HDMbased.Mode':'1 1',
                'HDMbased.AsymMode': 'ByCountry',
                'HDMbased.Param':'0.4 0.4 0.6 0.4 0.4 0.4'
            }
        }
        
    }
}
    

Long_Junction = {
    'Car': {
        'Defensive': {
            'Junction.Param': '0.8 0.8 0.7',
        },
        'Normal': {
            'Junction.Param': '0.5 0.5 0.5',
        },
        'Aggressive': {
            'Junction.Param': '0.2 0.1 0.1',
        },
    },
    'Truck' : {
        'Defensive': {
            'Junction.Param': '0.9 0.9 0.8',
        },
        'Normal': {
            'Junction.Param': '0.6 0.7 0.6',
        },
        'Aggressive': {
            'Junction.Param': '0.3 0.5 0.4',
        },
    }
    
}


Lane_Change = {
    'Car': {
        'Defensive': {
            'AccLatMax': '2.0',
            'Cautious': '0.75'
        },
        'Normal': {
            'AccLatMax': '4.0',
            'Cautious': '0.5'
        },
        'Aggressive': {
            'AccLatMax': '5.0',
            'Cautious': '0.25'
        }
    },
    'Truck': {
        'Defensive': {
            'AccLatMax': '1.5',
            'Cautious': '0.6'
        },
        'Normal': {
            'AccLatMax': '3.0',
            'Cautious': '0.4'
        },
        'Aggressive': {
            'AccLatMax': '4.0',
            'Cautious': '0.2'
        }
    }
}