import pandas as pd 

cols_dict = {'relation' : ['household_head','spouse/partner','son/daughter','stepson/daughter','son/daughter_inlaw',
                           'grandson/daughter','mother/father','father/mother_inlaw','brother/sister',
                           'brother/sister_inlaw','other_family_member','other_non_family_member'],
             
             'marital_status' : ['free_or_coupled', 'married', 'divorced', 'separated', 'widow/er', 'single'],
             
             'education' : ['no_education','incomplete_primary','complete_primary','incomplete_secondary',
                           'complete_secondary', 'incomplete_technical', 'complete_technical','undergraduate',
                           'postgraduate'],
             
             'region' : ['central', 'chorotega','pacific_central','brunca','huetar_atlantic','huetar_norte'],
             
             'house_ownership' : ['own', 'own_installments','rented','precarious','other_house'],
             
             'sewage' : ['no_toilet', 'sewer_cesspool', 'septic_tank', 'letrine', 'other_sewage'],
             
             'thrash_disposal' : ['tanker truck', 'hollow_buried', 'burning', 'throwing_space', 'throwing_water',
                                'other_disposal'],
             
             'elec_provider' : ['public', 'private_plant', 'none_electricity', 'cooperative'],
             
             'wall_material' : ['block_brick', 'wood_zinc_absbesto', 'prefabricated_cement', 'waste_material', 'wood',
                            'zink', 'natural_fibers', 'other_wall'],
             
             'floor_material' : ['tile','cement', 'other_floor', 'natural_material_floor', 'none_floor', 'wood_floor'],
             
             'roof_material' : ['metal', 'fiber_cement', 'natural_fibers_roof', 'other_roof'],
             
             'cooking_supply' : ['energy_none', 'electricity', 'gas', 'charcoal'],
             
             'water_supply' : ['inside', 'outside', 'water_none']
            }

def undummy(d):
    return d.dot(d.columns)

def get_condition(df, cols, fortification):
    t_df = df[cols]
    t_df.columns = ['bad', 'regular', 'good']
    t_df = t_df.assign(temp = t_df.pipe(undummy))
    t_df = t_df.rename(columns={'temp': '{}' .format(fortification)})
    t_df.drop(['bad', 'regular', 'good'], axis = 1, inplace = True)
    df.drop(cols, axis = 1, inplace = True)
    return t_df

def undummy_df(df):
    df['wall_condition'] = get_condition(df, ['wall_bad', 'wall_regular', 'wall_good'], 'wall_condition')
    df['roof_condition'] = get_condition(df, ['roof_bad', 'roof_regular', 'roof_good'], 'roof_condition')
    df['floor_condition'] = get_condition(df, ['floor_bad', 'floor_regular', 'floor_good'], 'floor_condition')
    
    for k in cols_dict.keys():
        t_df = df[cols_dict[k]]
        df = df.assign(temp = t_df.pipe(undummy))
        df.rename(columns = {'temp': k}, inplace = True)
        
    df['household_head'] = df['household_head']
        
    df.drop(['rural', 'male', 'tablet', 'mobile_phone', 'household_size', 'total_in_household'], axis = 1, inplace = True)
        
    for col in cols_dict:
        df.drop(cols_dict[col], axis = 1, inplace =True)
    
    return df