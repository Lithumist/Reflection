"""    game.py         - info     A class to hold info about the game that will be launched.      Can be loaded from xml files. (gameinfo)          - runner     Class to launch and manage a game. Needs gameinfo from the info class.          - player     Class that handles the player logic          - gameinfo objects:     - laser     - mirror          Also has a helper function to rotate surfaces      """import sysimport osimport mathimport xml.etree.ElementTree as etsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathimport euclidimport rayimport environment"""rotate an image while keeping its center and size"""def rot_center(image, angle):    orig_rect = image.get_rect()    rot_image = pygame.transform.rotate(image, angle)    rot_rect = orig_rect.copy()    rot_rect.center = rot_image.get_rect().center    rot_image = rot_image.subsurface(rot_rect).copy()    return rot_image# laserclass laser:    x_ = 0    y_ = 0    _angle = 0        def __init__( self, x=0, y=0, angle=0 ):        self.x_ = x        self.y_ = y        self._angle = angle        def changeAngle( self, angle ):        self._angle = angle# mirrorclass mirror:    x1_ = 7    y1_ = 0    x2_ = 0    y2_ = 0        def __init__( self, _x1=0, _y1=0, _x2=0, _y2=0 ):        self.x1_ = _x1        self.y1_ = _y1        self.x2_ = _x2        self.y2_ = _y2class info:    filename_ = ""    _ready = False # when true all game info is present        # game info    """ REMEMBER to update clear() when adding new properties """    title_ = ""    background_ = ""    player_sprite_ = ""    player_radius_ = 0    player_start_x = 0    player_start_y = 0    lasers_ = []    mirrors_ = []    # /game info        def __init__( self ):        self.clear()         # loadFromFile()    def loadFromFile( self, filename, verbose=False ):        """ store filename for later referral """        self.filename_ = filename        if verbose:            out.pl("Loading gameinfo from file '" + self.filename_ + "'")        """ verify file is the correct type """        tree_ = et.parse(self.filename_)        root_ = tree_.getroot()        if not (root_.tag == "reflection_gameinfo"):            _ready = False            if verbose:                out.pl("Error. File not Reflection gameinfo");            return False        """ iterate over the xml file and store all data """        laser_index_ = 0        mirror_index_ = 0        for child_ in root_:            if child_.tag == "title":                self.title_ = child_.text                if verbose:                    out.pl("Title: '" + self.title_ + "'")            if child_.tag == "art":                for art_ in child_:                    if art_.tag == "bg":                        self.background_ = art_.text                        if verbose:                            out.pl("Background: '" + self.background_ + "'")                    if art_.tag == "player":                        self.player_sprite_ = art_.text                        if verbose:                            out.pl("Player sprite: '" + self.player_sprite_ + "'")            if child_.tag == "player":                for player_ in child_:                    if player_.tag == "radius":                        self.player_radius_ = int( player_.text )                        if verbose:                            out.pl("Player radius: " + str( self.player_radius_ ))                    if player_.tag == "x1":                        self.player_start_x_ = int( player_.text )                        if verbose:                            out.pl("Player start x: " + str( self.player_start_x_ ))                    if player_.tag == "y1":                        self.player_start_y_ = int( player_.text )                        if verbose:                            out.pl("Player start y: " + str( self.player_start_y_ ))            if child_.tag == "laser":                xpos = 0                ypos = 0                angle = 0                for l_ in child_:                    if verbose:                        out.pl("Laser no. " + str( laser_index_ ))                    if l_.tag == "x1":                        xpos = int( l_.text )                        if verbose:                            out.pl("las " + str(laser_index_) + ": x: " + str(xpos))                    if l_.tag == "y1":                        ypos = int( l_.text )                        if verbose:                            out.pl("las " + str(laser_index_) + ": y: " + str(ypos))                    if l_.tag == "angle":                        angle = int( l_.text )                        if verbose:                            out.pl("las " + str(laser_index_) + ": angle: " + str(angle))                self.lasers_.append( laser(xpos,ypos,angle) )                laser_index_ += 1            if child_.tag == "mirror":                x1 = 0                y1 = 0                x2 = 0                y2 = 0                if verbose:                    out.pl("Mirror no. " + str( mirror_index_ ))                for m_ in child_:                    if m_.tag == "x1":                        x1 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": x1: " + str(x1))                    if m_.tag == "y1":                        y1 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": y1: " + str(y1))                    if m_.tag == "x2":                        x2 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": x2: " + str(x2))                    if m_.tag == "y2":                        y2 = int( m_.text )                        if verbose:                            out.pl("mir " + str(mirror_index_) + ": y2: " + str(y2))                self.mirrors_.append( mirror(x1,y1,x2,y2) )                mirror_index_ += 1                                                                            # checkReady()    # FIXME - add more checks with the new data loaded    def checkReady( self ):        if (self.title_ == ""):            self._ready = False            return False        if (self.background_ == ""):            self._ready = False            return False        """ gameinfo is ready """        _ready = True        return self._ready            # clear()    def clear( self ):        self.title_ = ""        self.background_ = ""        self.player_sprite_ = ""        self.player_radius_ = 0        self.player_start_x = 0        self.player_start_y = 0        self.lasers_ = []        self.mirrors_ = []class player:    x_ = 0.0    y_ = 0.0    x_speed_ = 0.0    y_speed_ = 0.0    rad_ = 0    angle_ = 0    enable_friction = False    friction_ = 0.2        _speed = 0.1    _max_speed = 2.0        _move_left = False    _move_right = False    _move_up = False    _move_down = False        texture_ = 0    wsurface_ = 0        # __init__()    def __init__( self , environment):        x_ = 0        y_ = 0        rad_ = 0        self.calculateNewPosition( environment )        # reset()    def reset( self ):        self.angle_ = 0        self.x_speed_ = 0.0        self.y_speed_ = 0.0        self._move_left = False        self._move_right = False        self._move_up = False        self._move_down = False        # events()    def events( self ):        """ movement """        keys = pygame.key.get_pressed()        if keys[pygame.K_a] or keys[pygame.K_LEFT]:            self._move_left = True        else:            self._move_left = False        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:            self._move_right = True        else:            self._move_right = False        if keys[pygame.K_w] or keys[pygame.K_UP]:            self._move_up = True        else:            self._move_up = False        if keys[pygame.K_s] or keys[pygame.K_DOWN]:            self._move_down = True        else:            self._move_down = False        # calculateNewPosition()    """ also updates the coordinates in environment.env """    def calculateNewPosition( self , environment ):        if self._move_left == True:            self.x_speed_ -= self._speed        elif self._move_right:            self.x_speed_ += self._speed        else:            if self.enable_friction:                if self.x_speed_ > 0:                    self.x_speed_ -= self.friction_                    if self.x_speed_ < 0:                        self.x_speed_ = 0                elif self.x_speed_ < 0:                    self.x_speed_ += self.friction_                    if self.x_speed_ > 0:                        self.x_speed_ = 0        if self._move_up:            self.y_speed_ -= self._speed        elif self._move_down:            self.y_speed_ += self._speed        else:            if self.enable_friction:                if self.y_speed_ > 0:                    self.y_speed_ -= self.friction_                    if self.y_speed_ < 0:                        self.y_speed_ = 0                elif self.y_speed_ < 0:                    self.y_speed_ += self.friction_                    if self.y_speed_ > 0:                        self.y_speed_ = 0                if self.x_speed_ > self._max_speed:            self.x_speed_ = self._max_speed        elif self.x_speed_ < -self._max_speed:            self.x_speed_ = -self._max_speed        if self.y_speed_ > self._max_speed:            self.y_speed_ = self._max_speed        elif self.y_speed_ < -self._max_speed:            self.y_speed_ = -self._max_speed                self.x_ += self.x_speed_        self.y_ += self.y_speed_                environment.reflectable_circle_list_[0].c.x = int(self.x_)        environment.reflectable_circle_list_[0].c.y = int(self.y_)        environment.reflectable_circle_list_[0].r = float( self.rad_ )        # calculateNewAngle()    def calculateNewAngle( self ):            self.angle_ -= self.x_speed_ * 3            if self.angle_ > 360:                self.angle_ = 0            if self.angle_ < 0:                self.angle_ = 360        # draw()    def draw( self, window_surface ):        #pygame.draw.circle( window_surface, (255,255,255), (int(self.x_),int(self.y_)), int(self.rad_), 1 )        rot_surface = rot_center(self.texture_, self.angle_)        self.wsurface_.blit(rot_surface, (int(self.x_)-self.rad_,int(self.y_)-self.rad_))        # warp()    def warp( self, x, y ):        self.x_ = x        self.y_ = yclass runner:    info_ = info()    running_ = False    wsurface_ = 0        env_ = environment.env()    ray_ = ray.machine()    player_ = player( env_ )        s_background_ = 0    s_player_ = 0            # __init__()    def __init__( self ):        running_ = False            def exit( self ):        self.running_ = False        self.info_.clear()        # ev() events    def ev( self ):        self._events()        self.player_.events()        # up() update    def up( self ):        self.ray_.calculate( self.env_ ) # calculate rays        self.player_.calculateNewPosition( self.env_ )        self.player_.calculateNewAngle()        # dr() draw    def dr( self ):        #self._clear_screen()                # - clear        self._draw_background()             # background        self.env_.draw( self.wsurface_ )     # physics environment        self.ray_.draw( self.wsurface_ )     # rays        self.player_.draw( self.wsurface_ )  # player        #self._update_screen()               # - update        # launch()    def launch( self , info , pygame_window_surface):        self.info_ = info        self.wsurface_ = pygame_window_surface                """ load shit """        self.s_background_ = pygame.image.load( makeRelativePath( self.info_.background_ ) ).convert()        self.s_player_ = pygame.image.load( makeRelativePath( self.info_.player_sprite_ ) ).convert()        self.s_player_.set_colorkey((255,0,255))                """ init ray system """        #self.ray_.addRaySequence( euclid.Point2(0,200) , euclid.Vector2(1,0.2) )        for laser_ in self.info_.lasers_:            rad_ = math.radians( laser_._angle )            self.ray_.addRaySequence(euclid.Point2( laser_.x_ , laser_.y_ ), euclid.Vector2( float(math.sin(rad_)) , float(math.cos(rad_)) ))                """ init reflectable environment """        for mirror_ in self.info_.mirrors_:            #import pdb; pdb.set_trace() # break point            self.env_.addReflectableLineSegment( mirror_.x1_, mirror_.y1_, mirror_.x2_, mirror_.y2_ )                """ init player """        self.player_.reset()        self.player_.rad_ = self.info_.player_radius_        self.player_.warp( self.info_.player_start_x_ , self.info_.player_start_y_ )        self.player_.wsurface_ = self.wsurface_        self.player_.texture_ = self.s_player_                self.running_ = True        #self._run()        # _run()    """    def _run( self ):                #main loop        while self.running_ == True:            #events            self._events()            self.player_.events()            #game logic            self.ray_.calculate( self.env_ ) # calculate rays            self.player_.calculateNewPosition( self.env_ )            # drawing            self._clear_screen()                # - clear            self._draw_background()             # background            self.env_.draw( self.wsurface_ )     # physics environment            self.ray_.draw( self.wsurface_ )     # rays            self.player_.draw( self.wsurface_ )  # player            self._update_screen()               # - update    """        # _clear_screen()    def _clear_screen( self ):        self.wsurface_.fill( pygame.Color( 0, 0, 0 ) )        # _update_screen()    def _update_screen( self ):        pygame.display.update()        pygame.time.Clock().tick( app_constants.values._frames_per_second )        def _draw_background( self ):        self.wsurface_.blit(self.s_background_, (0,0))        # _events()    def _events( self ):        pass        #for event in pygame.event.get():            #if event.type == QUIT:                #self.running_ = False