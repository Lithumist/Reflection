"""    laser.py        A game object that represents a laser"""import sysimport osimport mathimport copysys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import objectparentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))os.sys.path.insert(0,parentdir)from resource import TEXTURES,FONTSimport euclidimport physicsworld.stateimport physicsworld.rayimport physicsworld.drawclass laser ( object.object ) :    def __init__ ( self , x , y , angle ) :        object.object.__init__( self )        self.angle = angle        self.x = x        self.y = y        rad = math.radians( self.angle )                p = euclid.Point2( self.x , self.y )        v = euclid.Vector2( float(math.sin( rad )) , float(math.cos( rad )) )        self.pw_ray = physicsworld.ray.calculateRaySequence( p , v )            #/        def tick ( self ) :        # calculate the ray        self.pw_ray.calculate()        # update position        object.object.tick( self )    #/        def draw ( self , wsurface ) :        physicsworld.draw.drawRaySeq( wsurface , self.pw_ray )    #/    #/