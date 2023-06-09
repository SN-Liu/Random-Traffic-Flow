Traffic = {
    #Gerenal Parameters
    'ObjectKind': '', 
    'ObjectClass': '',
    'Name': '',
    'Info': '',                 #traffic object description
    'Movie.Geometry': '',       #traffic object model name
    'Color': '1.0 0.0 0.0',
    'Basics.Dimension': '',
    'Basics.Offset': '',
    'Basics.Fr12CoM': '',       #Specifies the x coordinate of the center of mass
    'Init.Orientation': '0 0 0',     #Default: 0.0 0.0 0.0.
    'RCSClass': '',             #Specifies the radar cross section class for the Radar Sensor
    'DetectMask': '',           #Default: 1 1
    #Start Conditions
    'Route': '0 1',                #<Route: Id or Name> bool <UsePath>
    'StartPos.Kind': 'Route',        #Default: Route
    'StartPos.ObjId': '-1',       #
    'StartPos': '0 0',             #sRoad tRoad
    'Init.v': '0',                  #Default : 0
    'FreeMotion': '0',           #Default:0
    'Lighting': '0',             #Default:0
    #Motion
    'Motion.Kind': '',
    'Motion.mass': '',
    'Motion.I': '',             #指定转动惯量
    'Motion.Overhang': '',
    'Motion.Cf': '',
    'Motion.Cr': '',
    'Motion.C_roll': '',
    'Motion.D_roll': '',
    'Motion.C_pitch': '',
    'Motion.D_pitch': '',
    'Motion.SteerCtrl.Ang_max': '40',       #Default:40
    'Motion.AnimateHitch': '1',              #Specifies if the hitch of a car should be animated
    #Maneuver
    'Man.TreatAtEnd': '0',       
    'Man.TreatAtEnd': 'FreezePos',
    'Man.N': '1',
    'Man.0.Limit': 't 100',
    'Man.0.LongDyn': 'auto 100',            #自动驾驶车速
    'Man.0.LatDyn': 'auto',
    #Autonomous driving 
    'AutoDrv.UpdRate': '100',
    #Longitudinal motion
    'AutoDrv.Long.Kind': 'Generic',
    'AutoDrv.Long.Gen.DistPreview':  '',
    'AutoDrv.Long.Gen.DistStand': '',
    'AutoDrv.Long.Gen.AccMax': '',
    'AutoDrv.Long.Gen.DecComf': '',
    'AutoDrv.Long.Gen.PCtrlSpd': '',
    'AutoDrv.Long.Gen.TimeGap': '',
    'AutoDrv.Long.Gen.TAdaptDist': '',
    'AutoDrv.Long.Gen.TAdaptRelSpd_low': '',
    'AutoDrv.Long.Gen.TAdaptRelSpd_high': '',
    'AutoDrv.Long.Gen.RelSpdRef': '',
    'AutoDrv.Long.Gen.DecMax': '-10',
    #curve driving
    'AutoDrv.AccLatMax': '',
    #lane change
    'AutoDrv.Cautious': '',
    #junction behavior
    'AutoDrv.Long.Junction.Param': '',
    #consider
    'AutoDrv.Long.ConsiderRoadElm': '1 1 1',
    #Vehicle Dynamics
    'LVD.AxMax': '',
    'LVD.vMax' : '',
    'LVD.Pmax': '',
    'LVD.tBuildUp': '',
    #Lateral motion
    'AutoDrv.Lat.HDMbased.Mode': '',                
    #Specifies whether the model is active for overtaking on lanes in driving direction (Multi-lane)(bool0) and on lanes against driving direction (Single-lane) (bool1).
    'AutoDrv.Lat.HDMbased.Param': '',
    'AutoDrv.Lat.HDMbased.AsymMode': 'ByCountry',
    'UpdRate': '200'
}