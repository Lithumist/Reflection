"""    mission.py        contains classes and variables to represent and manipulate missions and mission data         - 'missionData'     holds data for all missions. Can be loaded from files    """import sysimport osimport mathimport xml.etree.ElementTree as etsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePath# difficulty constantsD_EASY        =  0 D_MEDIUM      =  1D_CHALLENGE   =  2D_HARD        =  3D_INSANE      =  4D_NOPE        =  5D_names = [ "easy" , "medium" , "challenging" , "hard" , "insane" , "nope" ]class missionData:    """        Holds save state independent mission data.        Will be able to load from files.    """    def __init__ ( self ):        global D_EASY,D_MEDIUM,D_CHALLENGE,D_HARD,D_INSANE,D_NOPE        self.name = "Unknown"        self.name_x_offset = 0        self.desc = "This mission appears to be broken! Oh dear :( "        self.level = "levels/default.xml"        self.reward = 0        self.difficulty = D_MEDIUM        self.par = 1000        def reset ( self ) :        """ resets the instance to it's default state """        global D_EASY,D_MEDIUM,D_CHALLENGE,D_HARD,D_INSANE,D_NOPE        self.name = "Unknown"        self.name_x_offset = 0        self.desc = "This mission appears to be broken! Oh dear :( "        self.level = "levels/default.xml"        self.reward = 0        self.difficulty = D_MEDIUM        self.par = 1000        def loadFromFile ( self , filename , verbose=True ) :        if verbose :            out.pl("Loading mission from '" + filename + "'")        # open xml file and verify it's the correct type        tree = et.parse( filename )        root = tree.getroot()        if not (root.tag == "reflection_mission"):            self.bad = True            if verbose:                out.pl("Error. File not Reflection mission")            return False        # loop though xml elements        for child1 in root :            if child1.tag == "name" :                self.name = child1.text                if verbose :                    out.pl("name '" + self.name + "'")            if child1.tag == "gameinfo" :                self.level = child1.text                if verbose :                    out.pl("gameinfo '" + self.level + "'")            if child1.tag == "desc" :                self.desc = child1.text                if verbose :                    out.pl("desc '" + self.desc + "'")        #end for loop/        self.bad = False        out.pl("Finished loading mission file")#