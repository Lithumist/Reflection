"""    state_missions.py        mission select menu state"""import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom app_constants import TEXTURESimport utilimport saveimport gui.labelimport gui.button""" state vairbles """lbl_title = gui.label.label()btn_quit = gui.button.button()""" output vairables """change_state = "" # when this is set to something other than "" the calling code will change to that statedef quit_to_menu ():    save.clear()#def menu_btn_pressed ( which ):    # use these globals    global change_state, lbl_title, btn_quit    if which == "menu":        out.pl("quit button pressed")        quit_to_menu()    # switch state    change_state = which#def init ():    # use these globals    global change_state, lbl_title, btn_quit    # reset change_state    change_state = ""    # initialize lbl_title    lbl_title.x = 220    lbl_title.y = 10    lbl_title.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 30 )    lbl_title.text = "Mission Select"    lbl_title.textcolour = (255,255,255)    lbl_title.drawback = False    lbl_title.wordwrap = False    lbl_title.update()    # initialize quit button    btn_quit.x = 10    btn_quit.y = 449    btn_quit.horpad = 4    btn_quit.verpad = 4    btn_quit.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )    btn_quit.text = "quit"    btn_quit.textcolour = (255,255,255)    btn_quit.backcolour = (40,40,40)    btn_quit.hoverchange = True    btn_quit.calculate()    btn_quit.register_callback(menu_btn_pressed , "menu")    """    x = 296 # menu top left    y = 200 # menu top left    btn_y_space = 45    # initialize btn_new    btn_new.x = x    btn_new.y = y    btn_new.horpad = 8    btn_new.verpad = 4    btn_new.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )    btn_new.text = "new"    btn_new.textcolour = (255,255,255)    btn_new.backcolour = (40,40,40)    btn_new.hoverchange = True    btn_new.calculate()    btn_new.register_callback(menu_btn_pressed , "new")    # initialize btn_load    btn_load.x = x    btn_load.y = y + btn_y_space    btn_load.horpad = 4    btn_load.verpad = 4    btn_load.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )    btn_load.text = "load"    btn_load.textcolour = (255,255,255)    btn_load.backcolour = (40,40,40)    btn_load.hoverchange = True    btn_load.calculate()    btn_load.register_callback(menu_btn_pressed , "load")    # initialize btn_exit    btn_exit.x = x    btn_exit.y = y + btn_y_space * 2    btn_exit.horpad = 4    btn_exit.verpad = 4    btn_exit.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )    btn_exit.text = "exit"    btn_exit.textcolour = (255,255,255)    btn_exit.backcolour = (40,40,40)    btn_exit.hoverchange = True    btn_exit.calculate()    btn_exit.register_callback(menu_btn_pressed , "exit")    """#def update ():    # use these globals    global change_state, lbl_title, btn_quit    # update the buttons    btn_quit.update()#def draw ( wsurface ):    # use these globals    global change_state, lbl_title, btn_quit    # draw heading label and main buttons    lbl_title.draw( wsurface )    btn_quit.draw( wsurface )#