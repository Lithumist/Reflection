"""    state_loose.py        lost level state"""import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom resource import TEXTURES,FONTSimport resourceimport utilimport gui.labelimport gui.buttonimport saveimport game""" state vairbles """lbl_heading = gui.label.label()btn_restart = gui.button.button()btn_missions = gui.button.button()""" output vairables """change_state = "" # when this is set to something other than "" the calling code will change to that statedef menu_btn_pressed ( data1 ):    # use these globals    global lbl_heading, btn_restart, btn_missions, change_state    # switch state    if data1 == "game" :        out.pl("going to game state")        game.control.stop()    if data1 == "missions" :        out.pl("going to mission select state")        game.control.stop()    change_state = data1    pass#def init ():    # use these globals    global lbl_heading, btn_restart, btn_missions, change_state    # reset change_state    change_state = ""    # initialize lbl_heading    lbl_heading.x = 175    lbl_heading.y = 30    lbl_heading.font = FONTS.setnextloadsize(50).KarmaFuture50    lbl_heading.text = "You Lost :("    lbl_heading.textcolour = (255,255,255)    lbl_heading.drawback = False    lbl_heading.wordwrap = False    lbl_heading.update()    # initialize btn_restart    btn_restart.x = 100    btn_restart.y = 420    btn_restart.horpad = 4    btn_restart.verpad = 4    btn_restart.font = FONTS.setnextloadsize(16).Clacon16    btn_restart.text = "restart"    btn_restart.textcolour = (255,255,255)    btn_restart.backcolour = (40,40,40)    btn_restart.hoverchange = True    btn_restart.calculate()    btn_restart.register_callback( menu_btn_pressed , "game" )    # initialize btn_missions    btn_missions.x = 420    btn_missions.y = 420    btn_missions.horpad = 4    btn_missions.verpad = 4    btn_missions.font = FONTS.setnextloadsize(16).Clacon16    btn_missions.text = "mission select"    btn_missions.textcolour = (255,255,255)    btn_missions.backcolour = (40,40,40)    btn_missions.hoverchange = True    btn_missions.calculate()    btn_missions.register_callback( menu_btn_pressed , "missions" )#def update ():    # use these globals    global lbl_heading, btn_restart, btn_missions, change_state    # update the buttons    btn_restart.update()    btn_missions.update()#def draw ( wsurface ):    # use these globals    global lbl_heading, btn_restart, btn_missions, change_state    # draw heading label and buttons    lbl_heading.draw( wsurface )    btn_missions.draw( wsurface )    btn_restart.draw( wsurface )#