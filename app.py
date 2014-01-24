"""        Reflection        Pedro Custodio 2013 & 2014    """#import pdb; pdb.set_trace() # break pointimport sysimport timeimport stringimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport physicsworld.stateimport physicsworld.rayimport physicsworld.drawimport pygamefrom pygame.locals import *import euclidimport app_constantsimport rayimport environmentimport gameimport devconsole# version/build infobuild_number = 5version_name = "b" + str(build_number)# 'global' variablespygame_window_surface_ = 0  # only call it's methodsmain_loop_running_ = Falsein_devconsole = Falsestate = "none"gameinfo = None # the current gameinfo fileg = game.runner()"""    state table        "none"      no state    "game"      running a game    "title"     title screen    "menu"      main menu    """# start_game()""" called by the devconsole to start a game """def start_game( gameinfo_file ):    global state        gameinfo = game.info()    gameinfo.loadFromFile( gameinfo_file, False)    g.launch(gameinfo, pygame_window_surface_)    state = "game"# end_game()""" called by the devconsole to end a game """def end_game():    global state        state = "none"    g.exit()# application logic starts here# initialize pygamepygame.init()pygame_window_surface_ = pygame.display.set_mode( ( app_constants.values._window_width, app_constants.values._window_height ) )pygame.display.set_caption( app_constants.values._window_caption )pygame.mouse.set_visible( 1 )# init dev consoledevconsole.init()# rest of initialization goes here...# test physicsworldphysicsworld.state.start(100)a = physicsworld.object.object( 1 , True , True , 100 , 100 , 50 )b = physicsworld.object.object( 1 , True , True , 400 , 400 , 20 )c = physicsworld.object.object( 0 , True , True , 35 , 150 , 500 , 400 )physicsworld.state.addObject(a)physicsworld.state.addObject(b)#physicsworld.state.addObject(c)pt = euclid.Point2(260,240)assert isinstance(pt,euclid.Point2)rrs = physicsworld.ray.calculateRaySequence(pt , euclid.Vector2(1.0 , 1.0))#import pdb; pdb.set_trace() # break point# /test physicsworld# print version name and help messageout.pl( "Version: " + version_name )out.pl( "press ` to toggle developer console." )# start in test levelstart_game("levels/test.xml")# main loopfirst_pass = Truemain_loop_running_ = Truewhile main_loop_running_ == True:        """ check for python code to execute from the dev console """    if devconsole.dopython:        exec devconsole.pycode        devconsole.dopython = False        devconsole.str_out = devconsole.str_finish        for event in pygame.event.get():        if event.type == QUIT:            main_loop_running_ = False        if in_devconsole:            devconsole.events( event )        if state == "game":            g.ev()        if event.type == KEYDOWN:            #if event.key == pygame.K_m:                #app_constants.values.debug_flag_1 = not app_constants.values.debug_flag_1            """ toggle in_lvlchange """            if event.key == pygame.K_BACKQUOTE:                in_devconsole = ( not in_devconsole )                if in_devconsole:                    out.pl("Opened developer console.")                    pygame.key.set_repeat(500,20)                else:                    out.pl("Closed developer console.")                    pygame.key.set_repeat()        keys = pygame.key.get_pressed()    if keys[pygame.K_a]:        pass                # update ray angle so it faces the mouse position    """    if not first_pass:        xpos, ypos = pygame.mouse.get_pos()        len_mouse_vec = math.sqrt( pow(xpos-rx,2) + pow(ypos-ry,2) )        n_vec_x = float((xpos-rx)/len_mouse_vec)        n_vec_y = float((ypos-ry)/len_mouse_vec)        machine.appendRaySequence( r , euclid.Point2(rx,ry) , euclid.Vector2(n_vec_x,n_vec_y) )    """        if in_devconsole:        main_loop_running_ = devconsole.update()    elif state == "game":        g.up()        pygame_window_surface_.fill( pygame.Color( 0, 0, 0 ) )    # drawing code starts here        if state == "game":        g.dr()        #physicsworld.draw.drawState(pygame_window_surface_)        #physicsworld.draw.drawRaySeq(pygame_window_surface_ , rrs)    if in_devconsole:        devconsole.draw(pygame_window_surface_)        # drawing code finishes here    pygame.display.update()    pygame.time.Clock().tick( app_constants.values._frames_per_second )        first_pass = Falsepygame.quit()