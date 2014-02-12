"""        Reflection        Pedro Custodio 2013 & 2014    """#import pdb; pdb.set_trace() # break pointimport sysimport timeimport stringimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport physicsworld.stateimport physicsworld.rayimport physicsworld.drawimport gui.labelimport pygamefrom pygame.locals import *import euclidimport app_constantsimport rayimport environmentimport gameimport devconsoleimport save# version/build infoversion_name =          "pre alpha 2"version_name_short =    "pr2"# 'global' variablespygame_window_surface_ = 0  # only call it's methodsmain_loop_running_ = Falsein_devconsole = Falsestate = "none"gameinfo = None # the current gameinfo fileg = game.runner()"""    state table        "none"      no state    "game"      running a game    "menu"      main menu    """# start_game()""" called by the devconsole to start a game """def start_game( gameinfo_file ):    global state        gameinfo = game.info()    gameinfo.loadFromFile( gameinfo_file, False)    g.launch(gameinfo, pygame_window_surface_)    state = "game"# end_game()""" called by the devconsole to end a game """def end_game():    global state        state = "none"    g.exit()# application logic starts here# initialize pygamepygame.init()pygame_window_surface_ = pygame.display.set_mode( ( app_constants.values._window_width, app_constants.values._window_height ) )pygame.display.set_caption( app_constants.values._window_caption )pygame.mouse.set_visible( 1 )# init dev consoledevconsole.init()# initialise physicsworldphysicsworld.state.start(100)# rest of initialization goes here...# print version name and help messageout.pl( "Version: " + version_name )out.pl( "press ` to toggle developer console." )# test gui systemlbl = gui.label.label()lbl.x = 60lbl.y = 60lbl.width = 200lbl.height = 300lbl.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 20 )lbl.size = 20#lbl.text = "Hello World! This is a test of the label class in the gui package. Hopefully this is all word-wrapping? The unrelenting orgasms from his clunger raiding my mound of love pudding made me come so hard, I began sweating like a blind lesbian in a fish shop. Leaving my panties sunny side up on the floor was the least of my worries as his sperminator probed deeper into my balloon knot. With my fishy flaps now much like a hippo's yawn, he thought it was time to start ramming my shit winker. Is now the time to tell him I really need to ease a Mr. Hanky, I wondered? Now, I've seen more helmets than Hitler, but the sight of his meaty member made my beige slime slime like a broken fridge freezer. Inserting an egg timer into my clunge pool got me spritzing shrimp sap faster than greased shit off a shiny shovel."lbl.text = "a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a"lbl.textcolour = (255,0,0)lbl.backcolour = (255,255,255)lbl.drawback = Truelbl.wordwrap = Truelbl.update()# start in test levelstart_game("levels/test_old.xml")# main loopfirst_pass = Truemain_loop_running_ = Truewhile main_loop_running_ == True:        """ check for python code to execute from the dev console """    if devconsole.dopython:        exec devconsole.pycode        devconsole.dopython = False        devconsole.str_out = devconsole.str_finish        for event in pygame.event.get():        if event.type == QUIT:            main_loop_running_ = False        if in_devconsole:            devconsole.events( event )        if state == "game":            g.ev()        if state == "menu":            pass        if event.type == KEYDOWN:            #if event.key == pygame.K_m:                #app_constants.values.debug_flag_1 = not app_constants.values.debug_flag_1            """ toggle in_lvlchange """            if event.key == pygame.K_BACKQUOTE:                in_devconsole = ( not in_devconsole )                if in_devconsole:                    out.pl("Opened developer console.")                    pygame.key.set_repeat(500,20)                else:                    out.pl("Closed developer console.")                    pygame.key.set_repeat()        keys = pygame.key.get_pressed()    if keys[pygame.K_a]:        pass                # update ray angle so it faces the mouse position    """    if not first_pass:        xpos, ypos = pygame.mouse.get_pos()        len_mouse_vec = math.sqrt( pow(xpos-rx,2) + pow(ypos-ry,2) )        n_vec_x = float((xpos-rx)/len_mouse_vec)        n_vec_y = float((ypos-ry)/len_mouse_vec)        machine.appendRaySequence( r , euclid.Point2(rx,ry) , euclid.Vector2(n_vec_x,n_vec_y) )    """        if in_devconsole:        main_loop_running_ = devconsole.update()    elif state == "game":        g.up()        if not g.exit_code == -1:            if g.exit_code == 1:                out.pl("YOU DIED!!")            if g.exit_code == 0:                out.pl("YOU WON!!")            end_game()    elif state == "menu":        pass        pygame_window_surface_.fill( pygame.Color( 0, 0, 0 ) )    # drawing code starts here        if state == "game":        g.dr()        lbl.draw(pygame_window_surface_)    elif state == "menu":        pass    if in_devconsole:        devconsole.draw(pygame_window_surface_)        # drawing code finishes here    pygame.display.update()    pygame.time.Clock().tick( app_constants.values._frames_per_second )        first_pass = Falsepygame.quit()