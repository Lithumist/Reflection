"""    save.py        An interface to load a save file and to access data from all 3 slots"""import sysimport osimport mathimport xml.etree.ElementTree as etsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePath""" state variables """current_slot_loaded = -1money = -1mission = -1""" clears the state (to no save file) """def clear ():    global current_slot_loaded    current_slot_loaded = -1""" reads the specified save slots and updates the state accordingly """def load ( slot_num , verbose=False):    # use global variables    global current_slot_loaded    global money    global mission    # validate slot_num    assert( slot_num >= 1 and slot_num <= 3 )    # construct file name    filename = "saves/slot" + str(slot_num) + ".xml"    # verbose print    if verbose:        out.pl("Loading savefile from '" + filename + "'")    # open file and verify it's type    tree = et.parse(self.filename_)        root = tree_.getroot()        if not (root.tag == "reflection_savefile"):            if verbose:                out.pl("Error. File not Reflection savefile");            return False    # traverse savefile and store all data    for child in root:        if child.tag == "money":            money = int(child.text)        if child.tag == "mission":            mission = int(child.text)    # done""" saves the current state into the specified slot (or the current slot loaded if no slot is given) """def save ( slot=-1 ):    # validate slot (or assign the current)    global current_slot_loaded    if slot == -1:        slot = current_slot_loaded    else:        assert( slot_num >= 1 and slot_num <= 3 )