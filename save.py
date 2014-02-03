"""    save.py        An interface to load a save file and to access data from all 3 slots"""import sysimport osimport mathimport xml.etree.ElementTree as etsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom app_constants import TEXTURES""" state variables """current_slot_loaded = -1money = -1mission = -1""" clears the state (to no save file) """def clear ():    global current_slot_loaded    current_slot_loaded = -1""" reads the specified save slots and updates the state accordingly """def load ( slot_num ):    assert( slot_num >= 1 and slot_num <= 3 )    pass#""" saves the current state into the specified slot (or the current slot loaded if no slot is given) """def save ( slot=-1 ):    # validate slot (or assign the current)    global current_slot_loaded    if slot == -1:        slot = current_slot_loaded    else:        assert( slot_num >= 1 and slot_num <= 3 )    pass