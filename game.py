"""    game.py         - info     A class to hold info about the game that will be launched.      Can be loaded from xml files. (gameinfo)          - runner     Class to launch and manage a game. Needs gameinfo from the info class.          - player     Class that handles the player logic          - enemyFactory     Class that handles the creation, deletion and management of enemies      from the enemy module. The runner will feed it the enemy wave info      from the gameinfo object and the enemyFactory will handle it      accordingly.          - gameinfo objects:     - laser     - mirror     - wave          Also has a helper function to rotate surfaces      """import sysimport osimport mathimport xml.etree.ElementTree as etsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import physicsworld.stateimport physicsworld.rayimport physicsworld.drawimport app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom resource import TEXTURES,FONTSimport resourceimport euclidimport rayimport environmentimport enemy# livesstarting_lives = 3lives = starting_livesTEXTURES.heart =        "graphics/interface/heart.png"TEXTURES.heart_gone =   "graphics/interface/heart_gone.png"th = TEXTURES.heartthg = TEXTURES.heart_gone"""reset the lives"""def reset_lives ():    global starting_lives    global lives        lives = starting_lives        th.convert()    th.set_colorkey((255,0,255))    thg.convert()    thg.set_colorkey((255,0,255))"""draws lives in the top right of the screen"""def draw_lives (wsurface):    global starting_lives    global lives    for l in range(starting_lives):        if ( lives >= (l+1) ) :            wsurface.blit(TEXTURES.heart, ( 624 - (l*16) , 0 ))        else:            wsurface.blit(TEXTURES.heart_gone, ( 624 - (l*16) , 0 ))"""rotate an image while keeping its center and size"""def rot_center(image, angle):    orig_rect = image.get_rect()    rot_image = pygame.transform.rotate(image, angle)    rot_rect = orig_rect.copy()    rot_rect.center = rot_image.get_rect().center    rot_image = rot_image.subsurface(rot_rect).copy()    return rot_image# laserclass laser:    x_ = 0    y_ = 0    _angle = 0        def __init__( self, x=0, y=0, angle=0 ):        self.x_ = x        self.y_ = y        self._angle = angle        def changeAngle( self, angle ):        self._angle = angle# mirrorclass mirror:        def __init__( self, _x1=0, _y1=0, _x2=0, _y2=0 ):        self.x1_ = _x1        self.y1_ = _y1        self.x2_ = _x2        self.y2_ = _y2# waveclass wave:            def __init__ ( self , delay=0):        self.delay_ = int(math.floor(delay))        self.e_delay_ = []        self.e_type_ = []        self.e_x_ = []        self.e_y_ = []        # add ()    # delay in milliseconds    def add ( self , delay , type , x , y ):        self.e_delay_.append( int(math.floor(delay)) )        self.e_type_.append( type )        self.e_x_.append( x )        self.e_y_.append( y )class info:    filename_ = ""    _ready = False # when true all game info is present        # game info    """ REMEMBER to update clear() when adding new properties """    title_ = ""    background_ = ""    player_sprite_ = ""    player_radius_ = 0    player_start_x = 0    player_start_y = 0    lasers_ = []    mirrors_ = []    waves_ = []    # /game info        def __init__( self ):        self.clear()         # loadFromFile()    def loadFromFile( self, filename, verbose=False ):        """ store filename for later referral """        self.filename_ = filename        if verbose:            out.pl("Loading gameinfo from file '" + self.filename_ + "'")        """ verify file is the correct type """        tree_ = et.parse(self.filename_)        root_ = tree_.getroot()        if not (root_.tag == "reflection_gameinfo"):            _ready = False            if verbose:                out.pl("Error. File not Reflection gameinfo");            return False        """ iterate over the xml file and store all data """        laser_index_ = 0        mirror_index_ = 0        wave_index_ = 0        for child_ in root_:            if child_.tag == "title":                self.title_ = child_.text                if verbose:                    out.pl("Title: '" + self.title_ + "'")            if child_.tag == "art":                for art_ in child_:                    if art_.tag == "bg":                        self.background_ = art_.text                        if verbose:                            out.pl("Background: '" + self.background_ + "'")                    if art_.tag == "player":                        self.player_sprite_ = art_.text                        if verbose:                            out.pl("Player sprite: '" + self.player_sprite_ + "'")            if child_.tag == "player":                for player_ in child_:                    if player_.tag == "radius":                        self.player_radius_ = int( player_.text )                        if verbose:                            out.pl("Player radius: " + str( self.player_radius_ ))                    if player_.tag == "x1":                        self.player_start_x_ = int( player_.text )                        if verbose:                            out.pl("Player start x: " + str( self.player_start_x_ ))                    if player_.tag == "y1":                        self.player_start_y_ = int( player_.text )                        if verbose:                            out.pl("Player start y: " + str( self.player_start_y_ ))            if child_.tag == "laser":                xpos = 0                ypos = 0                angle = 0                for l_ in child_:                    if verbose:                        out.pl("Laser no. " + str( laser_index_ ))                    if l_.tag == "x1":                        xpos = int( l_.text )                        if verbose:                            out.pl("las " + str(laser_index_) + ": x: " + str(xpos))                    if l_.tag == "y1":                        ypos = int( l_.text )                        if verbose:                            out.pl("las " + str(laser_index_) + ": y: " + str(ypos))                    if l_.tag == "angle":                        angle = int( l_.text )                        if verbose:                            out.pl("las " + str(laser_index_) + ": angle: " + str(angle))                self.lasers_.append( laser(xpos,ypos,angle) )                laser_index_ += 1            if child_.tag == "mirror":                x1 = 0                y1 = 0                x2 = 0                y2 = 0                if verbose:                    out.pl("Mirror no. " + str( mirror_index_ ))                for m_ in child_:                    if m_.tag == "x1":                        x1 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": x1: " + str(x1))                    if m_.tag == "y1":                        y1 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": y1: " + str(y1))                    if m_.tag == "x2":                        x2 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": x2: " + str(x2))                    if m_.tag == "y2":                        y2 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": y2: " + str(y2))                self.mirrors_.append( mirror(x1,y1,x2,y2) )                mirror_index_ += 1            if child_.tag == "wave":                #import pdb; pdb.set_trace() # break point                delay = 0                if verbose:                    out.pl("Wave no. " + str( wave_index_ ))                if "delay" in child_.attrib:                    delay = int(child_.attrib["delay"])                enemy_index_ = 0                #import pdb; pdb.set_trace() # break point                self.waves_.append( wave(delay) )                #import pdb; pdb.set_trace() # break point                for e_ in child_:                    if verbose:                        out.pl("Enemy no. " + str(enemy_index_))                    xx = 0                    yy = 0                    delayy = 0                    typee = "none"                    if "delay" in e_.attrib:                        delayy = int(e_.attrib["delay"])                    if verbose:                        out.pl("ene " + str(enemy_index_) + ": delay: " + str(delayy))                    xx = int(e_.attrib["x"]) # raises an error if this isn't included                    if verbose:                        out.pl("ene " + str(enemy_index_) + ": x: " + str(xx))                    yy = int(e_.attrib["y"]) # ditto                    if verbose:                        out.pl("ene " + str(enemy_index_) + ": yy: " + str(yy))                    typee = e_.text     # ditto                    if verbose:                        out.pl("ene " + str(enemy_index_) + ": type: " + str(typee))                    #import pdb; pdb.set_trace() # break point                    self.waves_[-1].add(delayy,typee,xx,yy)                    enemy_index_ += 1                wave_index_ += 1                                                                            # checkReady()    # FIXME - add more checks with the new data loaded    def checkReady( self ):        if (self.title_ == ""):            self._ready = False            return False        if (self.background_ == ""):            self._ready = False            return False        """ gameinfo is ready """        _ready = True        return self._ready            # clear()    def clear( self ):        self.title_ = ""        self.background_ = ""        self.player_sprite_ = ""        self.player_radius_ = 0        self.player_start_x = 0        self.player_start_y = 0        self.lasers_ = []        self.mirrors_ = []        self.waves_ = []class enemyFactory:    """    # do not delete. documentation!    enemies_screen_ = [] # list of enemies on screen atm    waves_ = [] # list of wave info    st_ = 0 # saved time    wave_started_ = False    wave_index_ = 0 # the index of the wave we're currently on    wave_time_delay = 0 # milliseconds to wait until wave starts    enemy_index_ = 0 # the index of the enemy we're currently on    finished_spawning_ = False    """        # __init__ ()    def __init__ ( self , ws):        self.wsurface_ = ws        self.enemies_screen_ = []        self.waves_ = []        self.st_ = 0        self.wave_started_ = False        self.wave_index_ = 0        self.wave_time_delay = 0        self.enemy_index_ = 0        self.finished_spawning_ = False        self.all_dead = False        # reset ()    def reset ( self ):        self.enemies_screen_ = []        self.waves_ = []        self.st_ = 0        self.wave_started_ = False        self.wave_index_ = 0        self.wave_time_delay = 0        self.enemy_index_ = 0        self.finished_spawning_ = False        self.all_dead = False        # waveInfo ()    def waveInfo ( self , wv):        self.waves_ = wv        self.ts_ = pygame.time.get_ticks()                """ add a test enemy to the scren """        """        self.enemies_screen_.append( enemy.test_dummy() )        self.enemies_screen_[0].warp(300,10)        """        # load ()    def load ( self ):        for e in self.enemies_screen_:            e.load()        # update ()    def update ( self ):        """ add new enemies if needed """        if not self.finished_spawning_:            t = pygame.time.get_ticks()            if not self.wave_started_:                if t - self.st_ >= self.waves_[self.wave_index_].delay_:                    self.wave_started_ = True                    self.st_ = t                    self.enemy_index_ = 0                    out.pl("Wave " + str(self.wave_index_) + " started")            else:                if t - self.st_ >= self.waves_[self.wave_index_].e_delay_[self.enemy_index_] and (self.enemy_index_ < len(self.waves_[self.wave_index_].e_x_)-1):                    self.st_ = t                    etype = self.waves_[self.wave_index_].e_type_[self.enemy_index_]                    if etype == "test_dummy":                        self.enemies_screen_.append( enemy.test_dummy() )                        self.enemies_screen_[-1].load()                        self.enemies_screen_[-1].warp(self.waves_[self.wave_index_].e_x_[self.enemy_index_] , self.waves_[self.wave_index_].e_y_[self.enemy_index_])                        out.pl("Enemy " + str(self.enemy_index_) + " '" + etype + "' spawned")                    else:                        out.pl("Unknown enemy number " + str(self.enemy_index_) + " '" + etype + "'" )                    self.enemy_index_ += 1                    #import pdb; pdb.set_trace() # break point                """ check for change of wave """                if not (self.enemy_index_ < len(self.waves_[self.wave_index_].e_x_)-1):                    out.pl("Wave " + str(self.wave_index_) + " finished")                    self.enemy_index_ = 0                    self.wave_index_ += 1                    self.wave_started_ = False                    self.st_ = t                    """ check for last wave """                    if self.wave_index_ > len(self.waves_)-1:                        self.finished_spawning_ = True                """ update all enemies on screen """        aldd = True        for e in self.enemies_screen_:            if not e.dead:                e.update()                aldd = False            else:                """ decrease a life if the enemy has just gone off the screen """                if e.bottom == True:                    e.bottom = False                    global lives                    lives = lives-1        if aldd == True and self.finished_spawning_ == True:            """ all enemies dead """            self.all_dead = True            out.pl("ALL DEAD LAL")        # draw ()    def draw ( self , ws):        for e in self.enemies_screen_:            if not e.dead:                e.draw( ws )class player:    x_ = 0.0    y_ = 0.0    x_speed_ = 0.0    y_speed_ = 0.0    rad_ = 0    angle_ = 0    enable_friction = False    friction_ = 0.2        _speed = 0.1    _max_speed = 2.0        _move_left = False    _move_right = False    _move_up = False    _move_down = False        texture_ = 0    wsurface_ = 0        state_circle = -2        # __init__()    def __init__( self ):        x_ = 0        y_ = 0        rad_ = 0        self.state_circle = -2        # reset()    def reset( self ):        self.angle_ = 0        self.x_speed_ = 0.0        self.y_speed_ = 0.0        self._move_left = False        self._move_right = False        self._move_up = False        self._move_down = False        # events()    def events( self ):        """ movement """        keys = pygame.key.get_pressed()        if keys[pygame.K_a] or keys[pygame.K_LEFT]:            self._move_left = True        else:            self._move_left = False        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:            self._move_right = True        else:            self._move_right = False        if keys[pygame.K_w] or keys[pygame.K_UP]:            self._move_up = True        else:            self._move_up = False        if keys[pygame.K_s] or keys[pygame.K_DOWN]:            self._move_down = True        else:            self._move_down = False        # calculateNewPosition()    """ also updates the coordinates in physicsworld.state """    def calculateNewPosition( self ):        self.state_circle        if self._move_left == True:            self.x_speed_ -= self._speed        elif self._move_right:            self.x_speed_ += self._speed        else:            if self.enable_friction:                if self.x_speed_ > 0:                    self.x_speed_ -= self.friction_                    if self.x_speed_ < 0:                        self.x_speed_ = 0                elif self.x_speed_ < 0:                    self.x_speed_ += self.friction_                    if self.x_speed_ > 0:                        self.x_speed_ = 0        if self._move_up:            self.y_speed_ -= self._speed        elif self._move_down:            self.y_speed_ += self._speed        else:            if self.enable_friction:                if self.y_speed_ > 0:                    self.y_speed_ -= self.friction_                    if self.y_speed_ < 0:                        self.y_speed_ = 0                elif self.y_speed_ < 0:                    self.y_speed_ += self.friction_                    if self.y_speed_ > 0:                        self.y_speed_ = 0                if self.x_speed_ > self._max_speed:            self.x_speed_ = self._max_speed        elif self.x_speed_ < -self._max_speed:            self.x_speed_ = -self._max_speed        if self.y_speed_ > self._max_speed:            self.y_speed_ = self._max_speed        elif self.y_speed_ < -self._max_speed:            self.y_speed_ = -self._max_speed                self.x_ += self.x_speed_        self.y_ += self.y_speed_                """        environment.reflectable_circle_list_[0].c.x = int(self.x_)        environment.reflectable_circle_list_[0].c.y = int(self.y_)        environment.reflectable_circle_list_[0].r = float( self.rad_ )        """        physicsworld.state.objects[self.state_circle].x = int(self.x_)        physicsworld.state.objects[self.state_circle].y = int(self.y_)        physicsworld.state.objects[self.state_circle].radius = int(self.rad_)        # calculateNewAngle()    def calculateNewAngle( self ):            self.angle_ -= self.x_speed_ * 3            if self.angle_ > 360:                self.angle_ = 0            if self.angle_ < 0:                self.angle_ = 360        # draw()    def draw( self, window_surface ):        #pygame.draw.circle( window_surface, (255,255,255), (int(self.x_),int(self.y_)), int(self.rad_), 1 )        rot_surface = rot_center(self.texture_, self.angle_)        self.wsurface_.blit(rot_surface, (int(self.x_)-self.rad_,int(self.y_)-self.rad_))        # warp()    def warp( self, x, y ):        self.x_ = x        self.y_ = yclass runner:    info_ = info()    running_ = False    wsurface_ = 0    exit_code = -1    """        exit code                -1  prematurely ended        0   player won        1   player died    """        #env_ = environment.env()    #ray_ = ray.machine()    player_ = player()    ene_ = enemyFactory(0)    rays_ = []        #s_background_ = None    #s_player_ = None            # __init__()    def __init__( self ):        self.running_ = False        self.s_background_ = None        self.s_player_ = None        physicsworld.state.clearObjects()        self.rays_ = []        self.exit_code = -1            def exit( self ):        self.running_ = False        self.ene_.reset()        self.info_.clear()        physicsworld.state.clearObjects()        self.rays_ = []        self.exit_code = -1        # ev() events    def ev( self ):        self._events()        self.player_.events()        # up() update    def up( self ):        for rr in self.rays_:            rr.calculate()        self.player_.calculateNewPosition()        self.player_.calculateNewAngle()        self.ene_.update()                """ check for win/loss """        global lives        if lives <= 0:            self.exit_code = 1                if self.ene_.all_dead:            self.exit_code = 0        # dr() draw    def dr( self ):        self._draw_background()                     # background        physicsworld.draw.drawState(self.wsurface_) # pysics environment        for rr in self.rays_:            physicsworld.draw.drawRaySeq(self.wsurface_ , rr) # lasers        self.ene_.draw( self.wsurface_ )            # enemies        self.player_.draw( self.wsurface_ )         # player        draw_lives( self.wsurface_ )                # lives        # launch()    def launch( self , info , pygame_window_surface):        self.info_ = info        self.wsurface_ = pygame_window_surface                """ load level background and player textures """        # background        TEXTURES.level_background = self.info_.background_        self.s_background_ = TEXTURES.level_background        self.s_background_.convert()        # player        TEXTURES.player = makeRelativePath( self.info_.player_sprite_ )        self.s_player_ = TEXTURES.player        self.s_player_.convert()        self.s_player_.set_colorkey((255,0,255))                """ Init enemys """        self.ene_.waveInfo(info.waves_)                """ Load enemy textures """        self.ene_.load()                """ Init interface textures """        reset_lives()                """ init ray system """        for laser_ in self.info_.lasers_:            rad_ = math.radians( laser_._angle )            self.rays_.append(physicsworld.ray.calculateRaySequence(  euclid.Point2( laser_.x_ , laser_.y_ )  ,  euclid.Vector2( float(math.sin(rad_)) , float(math.cos(rad_)) )  ))                """ init reflectable environment """        for mirror_ in self.info_.mirrors_:            #self.env_.addReflectableLineSegment( mirror_.x1_, mirror_.y1_, mirror_.x2_, mirror_.y2_ )            o = physicsworld.object.object(  0 , True , True , mirror_.x1_ , mirror_.y1_ , mirror_.x2_ , mirror_.y2_  )            physicsworld.state.addObject( o )                """ init player """        self.player_.reset()        self.player_.rad_ = self.info_.player_radius_        self.player_.warp( self.info_.player_start_x_ , self.info_.player_start_y_ )        self.player_.wsurface_ = self.wsurface_        self.player_.texture_ = self.s_player_        p = physicsworld.object.object( 1 , True , False , 0 , 0 , 0 )        self.player_.state_circle = physicsworld.state.addObject( p )                self.running_ = True        #self._run()        # _run()    """    def _run( self ):                #main loop        while self.running_ == True:            #events            self._events()            self.player_.events()            #game logic            self.ray_.calculate( self.env_ ) # calculate rays            self.player_.calculateNewPosition( self.env_ )            # drawing            self._clear_screen()                # - clear            self._draw_background()             # background            self.env_.draw( self.wsurface_ )     # physics environment            self.ray_.draw( self.wsurface_ )     # rays            self.player_.draw( self.wsurface_ )  # player            self._update_screen()               # - update    """        # _clear_screen()    def _clear_screen( self ):        self.wsurface_.fill( pygame.Color( 0, 0, 0 ) )        # _update_screen()    def _update_screen( self ):        pygame.display.update()        pygame.time.Clock().tick( app_constants.values._frames_per_second )        def _draw_background( self ):        self.wsurface_.blit(self.s_background_, (0,0))        # _events()    def _events( self ):        pass        #for event in pygame.event.get():            #if event.type == QUIT:                #self.running_ = False