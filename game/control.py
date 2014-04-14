"""    control.py        Part of the game package. Provides an interface to control the rest of the package"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))os.sys.path.insert(0,parentdir)from resource import TEXTURES,FONTSimport euclidimport physicsworld.stateimport physicsworld.rayimport physicsworld.drawimport draw_serviceimport stateimport playerdef play ( level_filename ) :    """ sets the state of the package to play a level """    state._s.s.reset()    state._s.playing = True    # load the gameinfo file    state._s.g.load( level_filename , True )    # start physicsworld    physicsworld.state.start(100)    # load images    TEXTURES.level_background = state._s.g.fname_texture_background    state._s.background_texture = TEXTURES.level_background    TEXTURES.heart_black = "graphics/interface/heart_gone.png"    state._s.heart_black_texture = TEXTURES.heart_black    TEXTURES.heart_red = "graphics/interface/heart.png"    state._s.heart_red_texture = TEXTURES.heart_red    # add the player    p = player.player()    p.warp( state._s.g.player_x , state._s.g.player_y )    state._s.c.addObject( p )    # initialize the object factory    state._s.f.init( state._s.g , state._s.c )    state._s.f.start()    state._s.f.setPause( state._s.paused )#/def stop () :    """ sets the state of the package to be dormant and frees any memory used by the previous game played """    state._s.reset()    # reset physicsworld    physicsworld.state.clearObjects()#/def setPause ( p ) :    state._s.paused = p    # update context    state._s.c.setPause( p )    # update object factory    state._s.f.setPause( p )#/def events( event ) :    """ handles events for the game """    if not state._s.playing == True :        return    # perform context's events    state._s.c.events( event )    # perform object factory's events    state._s.f.events( event )#/def tick() :    """ updates the game """    if not state._s.playing == True :        return    # update the context    state._s.c.tick()    # update the object factory    state._s.f.tick( state._s.c )    """ live reduction logic """    for e in state._s.f.enemy_list :        if state._s.c.object_list[ e ].remove_life == True:            state._s.c.object_list[ e ].remove_life = False            state._s.lives -= 1    #/#/def draw ( wsurface ) :    """ draws the game """    if not state._s.playing == True :        return    """ queue depth drawing """    # level background    state._s.s.queueDrawCall( draw_service.draw( 0 , state._s.background_texture , 0 , 0 , None ) )    # HUD    queue_hud( wsurface )    """ draw """    # background images    state._s.s.drawBackground( wsurface )    # draw the context    state._s.c.draw( wsurface , state._s.s)    # object factory    state._s.f.draw( wsurface )    # foreground images    state._s.s.drawForeground( wsurface )    # debug physicsworld    physicsworld.draw.drawState( wsurface )#/def queue_hud ( wsurface ) :    # queue drawing lives    # draw right to left    for l in range( state._s.max_lives ) :        x_pos = 640 - 20 - (l * 18)        if l < state._s.lives :            state._s.s.queueDrawCall( draw_service.draw( 1 , state._s.heart_red_texture , x_pos , 4 , None ) )        else :            state._s.s.queueDrawCall( draw_service.draw( 1 , state._s.heart_black_texture , x_pos , 4 , None ) )#/