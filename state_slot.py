"""    state_slot.py        new/load game state"""import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom resource import TEXTURESimport resourceimport utilimport saveimport gui.labelimport gui.button""" state vairbles """lbl_title = gui.label.label()btn_back = gui.button.button()btn_slots = [gui.button.button() , gui.button.button() , gui.button.button()]lbl_slots = [gui.label.label() , gui.label.label() , gui.label.label()]save_data = [(-1,-1) , (-1,-1) , (-1,-1)] # (mission,money)""" output vairables """output_prefix = ""change_state = "" # when this is set to something other than "" the calling code will change to that statedef menu_btn_pressed ( which ):    # use these globals    global lbl_title, btn_back, btn_slots, lbl_slots, save_data, change_state, output_prefix    # print the state change    if which == "menu":        out.pl("going to main menu state")        output_prefix = ""    elif which == "slot1":        out.pl("slot1 chosen")    elif which == "slot2":        out.pl("slot2 chosen")    elif which == "slot3":        out.pl("slot3 chosen")    # switch state    change_state = output_prefix + which#def init ( out_pre ):    # use these globals    global lbl_title, btn_back, btn_slots, lbl_slots, save_data, change_state, output_prefix    # store output prefix    output_prefix = out_pre    # reset change_state    change_state = ""    # get save data    save.clear()    for i,d in enumerate(save_data):        save.load(i+1,True)        save_data[i] = (save.mission , save.money)        save.clear()    #    # initialize lbl_title    lbl_title.x = 180    lbl_title.y = 30    lbl_title.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/KarmaFuture.ttf"), 50 )    lbl_title.text = "Reflection"    lbl_title.textcolour = (255,255,255)    lbl_title.drawback = False    lbl_title.wordwrap = False    lbl_title.update()    # initialize back button    btn_back.x = 15    btn_back.y = 445    btn_back.horpad = 4    btn_back.verpad = 4    btn_back.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )    btn_back.text = "back"    btn_back.textcolour = (255,255,255)    btn_back.backcolour = (40,40,40)    btn_back.hoverchange = True    btn_back.calculate()    btn_back.register_callback( menu_btn_pressed , "menu")    # initialize new game menu buttons    x = 110 # menu top left    y = 220 # menu top left    btn_x_space = 180    btn_y_offset = 60    lbl_x_space = 180    lbl_x_offset = -40    # initialize all slot buttons    for i,btn in enumerate(btn_slots):        btn.x = x + (i*btn_x_space)        btn.y = y + btn_y_offset        btn.horpad = 4        btn.verpad = 4        btn.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 16 )        btn.text = "slot " + str(i+1)        btn.textcolour = (255,255,255)        btn.backcolour = (40,40,40)        btn.hoverchange = True        btn.calculate()        btn.register_callback( menu_btn_pressed , ("slot"+str(i+1)) )    #    # initialize all slot labels    for i,lbl in enumerate(lbl_slots):        lbl.x = x + (i*lbl_x_space) + lbl_x_offset        lbl.y = y        lbl.width = 140        lbl.height = 60        lbl.font = pygame.font.Font( app_constants.makeRelativePath("graphics/fonts/clacon.ttf"), 22 )        (cur_mission,cur_money) = save_data[i]        out.pl("cur_mission=" + str(cur_mission))        out.pl("cur_money=" + str(cur_money))        lbl.text = "Mission: " + str(cur_mission) + " Money: " + str(cur_money)        lbl.textcolour = (0,255,255)        lbl.backcolour = (100,100,100)        lbl.drawback = False        lbl.wordwrap = True        lbl.update()    ##def update ():    # use these globals    global lbl_title, btn_back, btn_slots, lbl_slots, save_data, change_state, output_prefix    # mutate heading text colour    lbl_title.textcolour = util.mutate_colour_random( 30 , lbl_title.textcolour )    lbl_title.update()    # update the buttons    btn_back.update()    for btn in btn_slots:        btn.update()#def draw ( wsurface ):    # use these globals    global lbl_title, btn_back, btn_slots, lbl_slots, save_data, change_state, output_prefix    # draw heading label, back button, slot buttons and slot labels    btn_back.draw( wsurface )    lbl_title.draw( wsurface )    for btn in btn_slots:        btn.draw( wsurface )    for lbl in lbl_slots:        lbl.draw( wsurface )#