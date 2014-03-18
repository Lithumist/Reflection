"""    state_menu.py        main menu state"""import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom resource import TEXTURES,FONTSimport resourceimport utilimport gui.labelimport gui.button""" state vairbles """lbl_title = gui.label.label()btn_new = gui.button.button()btn_load = gui.button.button()btn_exit = gui.button.button()""" output vairables """change_state = "" # when this is set to something other than "" the calling code will change to that statedef menu_btn_pressed ( which ):    # use these globals    global lbl_title, btn_new, btn_load, btn_exit, change_state    # print the state change    if which == "new":        out.pl("going to new game state")    elif which == "load":        out.pl("going to load game state")    elif which == "exit":        out.pl("exit button pressed")    # switch state    change_state = which#def init ():    # use these globals    global lbl_title, btn_new, btn_load, btn_exit, change_state    # reset change_state    change_state = ""    # initialize lbl_title    lbl_title.x = 180    lbl_title.y = 30    lbl_title.font = FONTS.setnextloadsize(50).KarmaFuture50    lbl_title.text = "Reflection"    lbl_title.textcolour = (255,255,255)    lbl_title.drawback = False    lbl_title.wordwrap = False    lbl_title.update()    # initialize menu buttons    x = 296 # menu top left    y = 200 # menu top left    btn_y_space = 45    # initialize btn_new    btn_new.x = x    btn_new.y = y    btn_new.horpad = 8    btn_new.verpad = 4    btn_new.font = FONTS.setnextloadsize(16).Clacon16    btn_new.text = "new"    btn_new.textcolour = (255,255,255)    btn_new.backcolour = (40,40,40)    btn_new.hoverchange = True    btn_new.calculate()    btn_new.register_callback(menu_btn_pressed , "new")    # initialize btn_load    btn_load.x = x    btn_load.y = y + btn_y_space    btn_load.horpad = 4    btn_load.verpad = 4    btn_load.font = FONTS.setnextloadsize(16).Clacon16    btn_load.text = "load"    btn_load.textcolour = (255,255,255)    btn_load.backcolour = (40,40,40)    btn_load.hoverchange = True    btn_load.calculate()    btn_load.register_callback(menu_btn_pressed , "load")    # initialize btn_exit    btn_exit.x = x    btn_exit.y = y + btn_y_space * 2    btn_exit.horpad = 4    btn_exit.verpad = 4    btn_exit.font = FONTS.setnextloadsize(16).Clacon16    btn_exit.text = "exit"    btn_exit.textcolour = (255,255,255)    btn_exit.backcolour = (40,40,40)    btn_exit.hoverchange = True    btn_exit.calculate()    btn_exit.register_callback(menu_btn_pressed , "exit")#def update ():    # use these globals    global lbl_title, btn_new, btn_load, btn_exit, change_state    # mutate heading text colour    lbl_title.textcolour = util.mutate_colour_random( 30 , lbl_title.textcolour )    lbl_title.update()    # update the buttons    btn_new.update()    btn_load.update()    btn_exit.update()#def draw ( wsurface ):    # use these globals    global lbl_title, btn_new, btn_load, btn_exit, change_state    # draw heading label and buttons    lbl_title.draw( wsurface )    btn_new.draw( wsurface )    btn_load.draw( wsurface )    btn_exit.draw( wsurface )    pass#