"""    context.py        Game object container."""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import draw_serviceimport objectparentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))os.sys.path.insert(0,parentdir)import physicsworld.stateclass context :        def __init__ ( self ) :        self.reset()    #/        def setPause ( self , p ) :        self.paused = p        # update game objects        for o in self.object_list :            if o is not None :                o.setPause( p )    #/        def reset ( self ) :        self.object_list = []        self.win_flag = False    #/        def events ( self , event ) :        for o in self.object_list :            if o is not None :                o.events( event )    #/        def tick ( self ) :        # update physicsworld objects        physicsworld.state.tick()        # update objects        self.win_flag = True        for o in self.object_list :            if o is not None :                o.tick()                if o.isEnemy == True and o.dead == False:                    self.win_flag = False    #/        def draw ( self , wsurface , ds ) :        # draw background        #ds.drawBackground( wsurface )        # draw objects        for o in self.object_list :            if o is not None and o.dead == False :                o.draw( wsurface )        # draw foreground        #ds.drawForeground( wsurface )    #/        def addObject ( self , new_object) :        """ adds an object to the object list, filling up any available empty spaces. Returns new object's position in the list """        # try to find an empty slot        for o , position in enumerate( self.object_list ) :            if o is None :                self.object_list[ position ] = new_object                self.object_list[ position ].load() # load the new object's resources                return position        # if we didn't find an empty space, append the new object at the end        self.object_list.append( new_object )        self.object_list[ -1 ].load() # load the new objects resources        return len( self.object_list ) - 1    #/    #/