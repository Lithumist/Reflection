"""    state_title.py        title screen state"""import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom app_constants import TEXTURESimport utilimport gui.labelimport gui.button""" state vairbles """lbl_title = gui.label.label()btn_start = gui.button.button()""" output vairables """change_state = "" # when this is set to something other than "" the calling code will change to that statedef start_btn_pressed ( data1 ):    # use these globals    global lbl_title, btn_start, change_state    # switch state    out.pl("going to menu state")    change_state = "menu"    pass#def init ():    # use these globals    global lbl_title, btn_start, change_state    # initialize lbl_title    lbl_title.x = 180    lbl_title.y = 30    lbl_title.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/KarmaFuture.ttf"), 50 )    lbl_title.text = "Reflection"    lbl_title.textcolour = (255,255,255)    lbl_title.drawback = False    lbl_title.wordwrap = False    lbl_title.update()    # initialize btn_start    btn_start.x = 290    btn_start.y = 440    btn_start.horpad = 4    btn_start.verpad = 4    btn_start.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )    btn_start.text = "start"    btn_start.textcolour = (255,255,255)    btn_start.backcolour = (40,40,40)    btn_start.hoverchange = True    btn_start.calculate()    btn_start.register_callback(start_btn_pressed)#def update ():    # use these globals    global lbl_title, btn_start, change_state    # mutate heading text colour    lbl_title.textcolour = util.mutate_colour_random( 30 , lbl_title.textcolour )    lbl_title.update()    # update the start button    btn_start.update()#def draw ( wsurface ):    # use these globals    global lbl_title, btn_start, change_state    # draw heading label and start button    lbl_title.draw( wsurface )    btn_start.draw( wsurface )    pass#