"""    e_dummy.py        Game object that represents a 'test dummy' enemy"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import objectparentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))os.sys.path.insert(0,parentdir)from resource import TEXTURES,FONTSimport euclidimport physicsworld.stateimport physicsworld.rayimport physicsworld.drawclass e_dummy ( object.object ) :    def __init__ ( self , x , y ) :        object.object.__init__( self )        self.x = x        self.y = y        self.y_speed = 0.5                TEXTURES.blue_ball = "graphics/characters/blue_ball.png"        self.texture = -1        self.radius = 10                self.reflect = True                self.pw_object = -1 # index of the physicsworld object                self.dead = False # dead flag.    #/        def load ( self ) :        # load texture        self.texture = TEXTURES.blue_ball                # add physicsworld object        o = physicsworld.object.object( 1 , self.reflect , True , self.x , self.y , self.radius )        self.pw_object = physicsworld.state.addObject( o )    #/        def events ( self , events ):        pass    #/        def tick ( self ) :        if self.dead :            return        # update positions        object.object.tick( self )        physicsworld.state.objects[ self.pw_object ].x = int( self.x )        physicsworld.state.objects[ self.pw_object ].y = int( self.y )        physicsworld.state.objects[ self.pw_object ].radius = int( self.radius )        # check if now outside screen        if self.hasBeenOnScreen == True and self.isOnScreen == False :            out.pl("killing enemy")            self.dead = True            physicsworld.state.delObject( self.pw_object )                #/        def draw ( self , wsurface ) :        # draw texture        wsurface.blit( self.texture , (self.x-self.radius , self.y-self.radius) )    #/#/