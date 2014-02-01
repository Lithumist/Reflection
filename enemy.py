"""    enemy.py        Defines a base class to make enemies"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport physicsworld.stateimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom app_constants import TEXTURESimport euclidimport rayimport environment# enemy classclass enemy:    """ pysiscs/game loop data """    #state = "idle"    #x_ = 0.0    #y_ = 0.0    #x_speed_ = 0.0    #y_speed_ = 0.0        """ general data to override """    #name_ = "enemy"    #max_health_ = 0        """ texture/audio references """            # __init__ ()    def __init__ ( self ):        self.state = "idle"        self.x_ = 0.0        self.y_ = 0.0        self.x_speed_ = 0.0        self.y_speed_ = 0.0        self.name_ = "enemy"        self.max_health_ = 0        self.dead = False                self.t = []        # override    # load ()    # should load all texture and audio data    # parent method should be called at the END of the child funciton:    # converts and set the colour key for all textures    def load ( self ):        for tex in self.t:            tex.convert()            tex.set_colorkey((255,0,255))        # override    # update ()    # called in the game loop, should do enemy logic and update the enemy    # should call the base method AT THE END    def update ( self ):        """ update x and y """        self.x_ += self.x_speed_        self.y_ += self.y_speed_                """ update pobj """        if hasattr(self , "pobj"):            physicsworld.state.objects[self.pobj].warp(self.x_ , self.y_)        # override    # draw ()    # called in the game loop, should draw the enemy w/ animation or whatever    def draw ( self , ws):        pass        # override    # die ()    # called when the enemy should die    # should be used to play death animations/sounds    # set self.dead to True when done with death stuff    # doesn't need to call base method    def die ( self ):        self.dead = True        # warp ()    def warp ( self , x , y ):        self.x_ = x        self.y_ = y# test enemy classclass test_dummy (enemy):    """ general data """        """ timer data """        # __init__ ()    def __init__ ( self ):        enemy.__init__( self )                self.state_ = "down"        self.name_ = "test dummy"        self.max_health_ = 10        self.time_save_ = pygame.time.get_ticks()        self.flag1_ = 0        self.state_time_delay_ = 1000 # milliseconds        # create the pobj        e = physicsworld.object.object( 1 , False , True , self.x_ , self.y_ , 20 )        self.pobj = physicsworld.state.addObject(e)        # laod ()    def load ( self ):        #self.textures_.append( pygame.image.load( makeRelativePath( "graphics/characters/test_dummy.png" ) ).convert() )        # load all textures        TEXTURES.test_dummy = "graphics/characters/test_dummy.png"        self.t.append( TEXTURES.test_dummy )        # parent method        enemy.load( self )        # die ()    def die ( self ):        self.dead = True        physicsworld.state.delObject( self.pobj )        # update ()    def update ( self ):        """ check if enemy has been hit by a laser """        if physicsworld.state.objects[self.pobj].hit == True:            self.die()            return                """ check if change of state is needed """        cur_time = pygame.time.get_ticks()        if cur_time - self.time_save_ >= self.state_time_delay_:            #import pdb; pdb.set_trace() # break point            self.time_save_ = cur_time            if self.state_ == "down":                if self.flag1_ == 0:                    self.state_ = "right"                elif self.flag1_ == 1:                    self.state_ = "left"            elif self.state_ == "right":                self.state_ = "down"                self.flag1_ = 1            elif self.state_ == "left":                self.state_ = "down"                self.flag1_ = 0                """ handle states """        if self.state_ == "down":            self.y_speed_ = 0.5            self.x_speed_ = 0.0        if self.state_ == "right":            self.y_speed_ = 0.0            self.x_speed_ = 0.5        if self.state_ == "left":            self.y_speed_ = 0.0            self.x_speed_ = -0.5                """ parent update. update x and y w/ speeds """        enemy.update( self )        # draw ()    def draw ( self , ws):        ws.blit(TEXTURES.test_dummy, (self.x_,self.y_))