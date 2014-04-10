"""    control.py        Part of the game package. Provides an interface to control the rest of the package"""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *from state import stateimport playerdef play ( level_filename ) :    """ sets the state of the package to play a level """    state.playing = True    # load the gameinfo file    state.g.load( level_filename , True )    # add the player    p = player.player()    state.c.addObject( p )    # initialize the enemy factory    state.e.init( None ) # UPDATE THIS LATER WITH ACTUAL GAMEINFO OBJECT    state.e.start()#/def stop () :    """ sets the state of the package to be dormant and frees any memory used by the previous game played """    state.reset(state.i)#/def setPause ( p ) :    state.paused = p    # update context    state.c.setPause( p )    # update enemy factory    state.e.setPause( p )#/def events( event ) :    """ handles events for the game """    if not state.playing == True :        return    # perform context's events    state.c.events( event )    # perform enemy factor's events    state.c.events( event )#/def tick() :    """ updates the game """    if not state.playing == True :        return    # update the context    state.c.tick()    # update the enemy factory    state.e.tick( state.c )#/def draw ( wsurface ) :    """ draws the game """    if not state.playing == True :        return    # draw the context    state.c.draw( wsurface )    # draw the enemy manager    state.e.draw( wsurface )#/