"""    state.py        Declares a class that holds state information for the WHOLE package.    This is passed around to classes and functions to avoid having to use many 'global' declarations"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import gameinfoimport draw_serviceimport contextimport object_factoryclass state :        i = 0 # this will be a reference to the only instance of this class            def __init__ ( self ) :        self.playing = False        self.paused = False        self.s = draw_service.service()        self.g = gameinfo.gameinfo()        self.c = context.context()        #import pdb; pdb.set_trace() # break point        self.f = object_factory.factory()        #import pdb; pdb.set_trace() # break point                self.background_texture = None    #/        def reset ( self ) :        self.playing = False        self.paused = False        self.s.reset()        self.g.reset()        self.c.reset()        self.f.reset()        self.background_texture = None    #/#/# instance_s = state()state.i = _s