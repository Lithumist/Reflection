"""    state.py        Declares a class that holds state information for the WHOLE package.    This is passed around to classes and functions to avoid having to use many 'global' declarations"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import contextclass state :        i = 0 # this will be a reference to the only instance of this class        playing = False    c = context.context()    paused = False        def __init__ ( self ) :        pass    #/        def reset ( self ) :        self.playing = False        self.c.reset()    #/#/# instance_s = state()state.i = _s