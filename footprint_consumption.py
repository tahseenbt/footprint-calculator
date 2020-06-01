# Part 4
# Footprint of computing and diet
# Author: Tahseen Bin Taj

import doctest
from unit_conversion import *

INCOMPLETE = -1

def fp_from_online(daily_online_use):
    ''' (num) -> float
    Returns the annual metric tonnes of CO2E from online use
    >>> fp_from_online(0)
    0.0
    >>> round(fp_from_online(1),4)
    0.0201
    >>> round(fp_from_online(5),4)
    0.1004
    '''
    tonnes_of_CO2E_from_online_use_annually = kg_to_tonnes(daily_to_annual(daily_online_use * 55 / 1000))
    return tonnes_of_CO2E_from_online_use_annually

def fp_from_phone(daily_phone_use):
    ''' (num) -> float
    Returns the annual metric tonnes of CO2E from phone use
    >>> fp_from_phone(0)
    0.0
    >>> round(fp_from_phone(1),4)
    1.25
    >>> round(fp_from_phone(5),4)
    6.25
    '''
    tonnes_of_CO2E_from_phone_use_annually = kg_to_tonnes(daily_phone_use * 1250)
    return tonnes_of_CO2E_from_phone_use_annually

def fp_from_new_light_devices(new_light_devices):
    ''' (num) -> float
    Returns the annual metric tonnes of CO2E from new light devices
    >>> fp_from_new_light_devices(0)
    0.0
    >>> round(fp_from_new_light_devices(1),4)
    0.075
    >>> round(fp_from_new_light_devices(5),4)
    0.375
    '''
    tonnes_of_CO2E_from_new_light_devices_annually = kg_to_tonnes(new_light_devices * 75)
    return tonnes_of_CO2E_from_new_light_devices_annually

def fp_from_new_medium_devices(new_medium_devices):
    ''' (num) -> float
    Returns the annual metric tonnes of CO2E from new medium devices
    >>> fp_from_new_medium_devices(0)
    0.0
    >>> round(fp_from_new_medium_devices(1),4)
    0.2
    >>> round(fp_from_new_medium_devices(5),4)
    1.0
    '''
    tonnes_of_CO2E_from_new_medium_devices_annually = kg_to_tonnes(new_medium_devices * 200)
    return tonnes_of_CO2E_from_new_medium_devices_annually

def fp_from_new_heavy_devices(new_heavy_devices):
    ''' (num) -> float
    Returns the annual metric tonnes of CO2E from new heavy devices
    >>> fp_from_new_heavy_devices(0)
    0.0
    >>> round(fp_from_new_heavy_devices(1),4)
    0.8
    >>> round(fp_from_new_heavy_devices(5),4)
    4.0
    '''
    tonnes_of_CO2E_from_new_heavy_devices_annually = kg_to_tonnes(new_heavy_devices * 800)
    return tonnes_of_CO2E_from_new_heavy_devices_annually

######################################

def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    total_CO2E = fp_from_online(daily_online_use) + fp_from_phone(daily_phone_use) + fp_from_new_light_devices(new_light_devices) + fp_from_new_medium_devices(new_medium_devices) + fp_from_new_heavy_devices(new_heavy_devices)
    return total_CO2E


######################################

vegan_diet = daily_to_annual(kg_to_tonnes(2.89))

def fp_from_meat(daily_g_meat):
    ''' (num) -> float
    Returns annual CO2E footprint from consuming meat.
    >>> fp_from_meat(0)
    0.0
    >>> round(fp_from_meat(25), 4)
    0.2447
    >>> round(fp_from_meat(3), 4)
    0.0294
    '''
    tonnes_of_CO2E_from_meat_annually = daily_to_annual(kg_to_tonnes(daily_g_meat*0.0268))
    return tonnes_of_CO2E_from_meat_annually

def fp_from_cheese(daily_g_cheese):
    ''' (num) -> float
    Returns annual CO2E footprint from consuming cheese.
    >>> fp_from_cheese(0)
    0.0
    >>> round(fp_from_cheese(25), 4)
    0.1096
    >>> round(fp_from_cheese(3), 4)
    0.0131
    '''
    tonnes_of_CO2E_from_cheese_annually = daily_to_annual(kg_to_tonnes(daily_g_cheese*0.012))
    return tonnes_of_CO2E_from_cheese_annually

def fp_from_milk(daily_L_milk):
    ''' (num) -> float
    Returns annual CO2E footprint from consuming cheese.
    >>> fp_from_milk(0)
    0.0
    >>> round(fp_from_milk(25), 4)
    2.4451
    >>> round(fp_from_milk(3), 4)
    0.2934
    '''
    tonnes_of_CO2E_from_milk_annually = daily_to_annual(kg_to_tonnes(daily_L_milk*0.2677777))
    return tonnes_of_CO2E_from_milk_annually

def fp_from_eggs(daily_num_eggs):
    ''' (num) -> float
    Returns annual CO2E footprint from consuming cheese.
    >>> fp_from_eggs(0)
    0.0
    >>> round(fp_from_eggs(25), 4)
    2.7393
    >>> round(fp_from_eggs(3), 4)
    0.3287
    '''
    tonnes_of_CO2E_from_eggs_annually = daily_to_annual(kg_to_tonnes(daily_num_eggs*0.3))
    return tonnes_of_CO2E_from_eggs_annually

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    total_tonnes_of_CO2E_from_diet = vegan_diet + fp_from_meat(daily_g_meat) + fp_from_cheese(daily_g_cheese) + fp_from_milk(daily_L_milk) + fp_from_eggs(daily_num_eggs) 
    return total_tonnes_of_CO2E_from_diet


#################################################

if __name__ == '__main__':
    doctest.testmod()

