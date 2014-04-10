"""    gameinfo.py        Class to load gameinfo files and provide it's data in useful formats for other classes"""import sysimport osimport mathimport xml.etree.ElementTree as etsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfclass gameinfo :    def __init__ ( self ) :        self.reset()    #/        def reset ( self ) :        # general instance info        self.filename = ""        self.bad = True # shouldn't access if this flag is true ('load' method sets to false on a successful load)        # general level info        self.title = ""        # asset filenames        self.fname_texture_background = ""    #/        def load ( self , filename , verbose = True) :        self.filename = filename        if verbose :            out.pl( "Loading level from gameinfo file '" + self.filename + "'" )        # open xml file and verify it's the correct type        tree = et.parse( self.filename )        root = tree.getroot()        if not (root.tag == "reflection_gameinfo"):            self.bad = True            if verbose:                out.pl("Error. File not Reflection gameinfo");            return False        # iterate over xml file and store data        for child1 in root :            if child1.tag == "title" :                self.title = child1.text                if verbose :                    out.pl( "<title> '" + self.title + "'" )            elif child1.tag == "art":                for child2 in child1 :                    if child2.tag == "bg" :                        self.fname_texture_background = child2.text                        if verbose :                            out.pl( "<bg> '" + self.fname_texture_background + "'" )                #end for loop/            #end elif/        #end for loop/        # if we got this far then everything was loaded        self.bad = False    #end 'load' method/#end class definition/