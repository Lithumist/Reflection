"""    control.py        Part of the game package. Provides an interface to control the rest of the package"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *from state import statedef play ( s , level_filename ) :    """ sets the state of the package to play a level """# /def stop ( s ) :    """ sets the state of the package to be dormant and frees any memory used by the previous game played """# /