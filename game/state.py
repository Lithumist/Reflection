"""    state.py        Declares a class that holds state information for the WHOLE package.    This is passed around to classes and functions to avoid having to use many 'global' declarations"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *class state :        self.playing = False        def __init__ ( self ) :    # /        def reset ( self ) :        self.playing = False    # /# /# instance_s = state()