"""        Reflection        Pedro Custodio 2013 & 2014    """#import pdb; pdb.set_trace() # break pointimport sysimport timeimport stringimport mathimport randomsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport physicsworld.stateimport physicsworld.rayimport physicsworld.drawimport gui.labelimport gui.buttonimport pygamefrom pygame.locals import *import utilimport euclidimport app_constantsimport rayimport environmentimport gameimport devconsoleimport saveimport state_titleimport state_menuimport state_slotimport state_missions# version/build infoversion_name =          "alpha 1"version_name_short =    "a1"# 'global' variablespygame_window_surface_ = 0  # only call it's methodsmain_loop_running_ = Falsein_devconsole = Falsestate = "none"gameinfo = None # the current gameinfo fileg = game.runner()"""    state table        "none"      no state    "game"      running a game    "menu"      main menu    """# start_game()""" called by the devconsole to start a game """def start_game( gameinfo_file ):    global state        gameinfo = game.info()    gameinfo.loadFromFile( gameinfo_file, False)    g.launch(gameinfo, pygame_window_surface_)    state = "game"# end_game()""" called by the devconsole to end a game """def end_game():    global state        state = "none"    g.exit()#def new_game ( slotnum ):    global state    """ starts a new game and goes to the mission screen """    out.pl("starting new game in slot " + str(slotnum))    save.clear()    save.mission = 1    save.money = 0    save.save(slotnum)    state = "missions"    state_missions.init()#def load_game ( slotnum ):    global state    """ loads a game and goes to the mission screen """    out.pl("loading game in slot " + str(slotnum))    save.clear()    save.load(slotnum)    state = "missions"    state_missions.init()#def state_change ( change_state_value ):    global state, main_loop_running_    if not change_state_value == "":        state = change_state_value        # initialize the new state        # ya.. pretty bad        if state == "exit":            main_loop_running_ = False        if state == "title":            state_title.init()        elif state == "menu":            state_menu.init()        elif state == "new":            state_slot.init("new")        elif state == "load":            state_slot.init("load")        elif state == "newslot1":            new_game(1)        elif state == "newslot2":            new_game(2)        elif state == "newslot3":            new_game(3)        elif state == "loadslot1":            load_game(1)        elif state == "loadslot2":            load_game(2)        elif state == "loadslot3":            load_game(3)# application logic starts here# initialize pygamepygame.init()pygame_window_surface_ = pygame.display.set_mode( ( app_constants.values._window_width, app_constants.values._window_height ) )pygame.display.set_caption( app_constants.values._window_caption )pygame.mouse.set_visible( 1 )# init dev consoledevconsole.init()# initialise physicsworldphysicsworld.state.start(100)# rest of initialization goes here...# print version name and help messageout.pl( "Version: " + version_name )out.pl( "press ` to toggle developer console." )# start in test level#start_game("levels/test_old.xml")# start in the title screenstate = "title"state_title.init()# main loopfirst_pass = Truemain_loop_running_ = Truewhile main_loop_running_ == True:        """ check for python code to execute from the dev console """    if devconsole.dopython:        exec devconsole.pycode        devconsole.dopython = False        devconsole.str_out = devconsole.str_finish        for event in pygame.event.get():        if event.type == QUIT:            main_loop_running_ = False        if in_devconsole:            devconsole.events( event )        if state == "game":            g.ev()        if state == "title":            pass        if state == "menu":            pass        if state == "new" or state == "load":            pass        if state == "missions":            pass        if event.type == KEYDOWN:            #if event.key == pygame.K_m:                #app_constants.values.debug_flag_1 = not app_constants.values.debug_flag_1            """ toggle in_devconsole """            if event.key == pygame.K_BACKQUOTE:                in_devconsole = ( not in_devconsole )                if in_devconsole:                    out.pl("Opened developer console.")                    pygame.key.set_repeat(500,20)                else:                    out.pl("Closed developer console.")                    pygame.key.set_repeat()        keys = pygame.key.get_pressed()    if keys[pygame.K_y]:        pass                # update ray angle so it faces the mouse position    """    if not first_pass:        xpos, ypos = pygame.mouse.get_pos()        len_mouse_vec = math.sqrt( pow(xpos-rx,2) + pow(ypos-ry,2) )        n_vec_x = float((xpos-rx)/len_mouse_vec)        n_vec_y = float((ypos-ry)/len_mouse_vec)        machine.appendRaySequence( r , euclid.Point2(rx,ry) , euclid.Vector2(n_vec_x,n_vec_y) )    """        if in_devconsole:        main_loop_running_ = devconsole.update()        g.up()        if not g.exit_code == -1:            if g.exit_code == 1:                out.pl("YOU DIED!!")            if g.exit_code == 0:                out.pl("YOU WON!!")            end_game()    elif state == "title":        state_title.update()        state_change(state_title.change_state)    elif state == "menu":        state_menu.update()        state_change(state_menu.change_state)    elif state == "new" or state == "load":        state_slot.update()        state_change(state_slot.change_state)    elif state == "missions":        state_missions.update()        state_change(state_missions.change_state)        pygame_window_surface_.fill( pygame.Color( 0, 0, 0 ) )    # drawing code starts here        if state == "game":        g.dr()    elif state == "title":        state_title.draw( pygame_window_surface_ )    elif state == "menu":        state_menu.draw( pygame_window_surface_ )    elif state == "new" or state == "load":        state_slot.draw( pygame_window_surface_ )    elif state == "missions":        state_missions.draw( pygame_window_surface_ )    if in_devconsole:        devconsole.draw(pygame_window_surface_)        # drawing code finishes here    pygame.display.update()    pygame.time.Clock().tick( app_constants.values._frames_per_second )        first_pass = Falsepygame.quit()