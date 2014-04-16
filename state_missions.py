"""    state_missions.py        mission select menu state.            This is a pile of shit.    If you can understand this, you are beyond human..    """import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom resource import TEXTURES,FONTSimport resourceimport missionimport utilimport saveimport gui.labelimport gui.button""" state vairbles """lbl_title = gui.label.label()btn_quit = gui.button.button()btn_nav = [gui.button.button() , gui.button.button()] # 0-up, 1-downbtn_play = gui.button.button()lbl_mission_names = []mission_count = 10""" input variables """mission_data_list = [] # list of 'missionData' objects""" output vairables """change_state = "" # when this is set to something other than "" the calling code will change to that stategi_filename = "levels/1.xml" # the gameinfo file to load when starting a gamecur_mission_num = 0 # the mission number to load minus one ( -1 )class listDisplay :    """        organises and displays the mission data                note - all the missions buttons are refered to as labels, "lbl"        This is because they were originally labels and I can't be fucked to change the names back.                        Deal with it                                        P.S, I'm so sorry                    """    def __init__ ( self ) :        global lbl_mission_names        self.top = 0 # index of the mission at the top of the display        self.ITEMS_ON_SCREEN_AT_ONCE = 5 # change this constant and the rest of the class will update        self.labels = []    #        def draw ( self , wsurface ):        global lbl_mission_names        for m in lbl_mission_names :            m.draw( wsurface )    #        def linkLabels ( self , list_of_labels ) :        global lbl_mission_names        """ gives the instance references to all of the lables to display onto """        self.labels = list_of_labels    #        def navigate ( self , delta ) :        global lbl_mission_names        """ scrolls the list by 'delta' ammount. make sure it doesn't go out of bounds """        global mission_data_list         self.top += delta        if self.top < 0 :            self.top = 0        if self.top > len( mission_data_list ) - self.ITEMS_ON_SCREEN_AT_ONCE :            self.top = len( mission_data_list ) - self.ITEMS_ON_SCREEN_AT_ONCE - 0    #        def navigateUp ( self ) :        global lbl_mission_names        """ scrolls the list up by one """        self.navigate( -1 )    #        def navigateDown ( self ) :        global lbl_mission_names        """ scrolls the list down by one """        self.navigate( 1 )    #        def updateLabels ( self ) :        global mission_data_list, lbl_mission_names        """ updates the labels with the correct info """        screen_label = -1        while screen_label < self.ITEMS_ON_SCREEN_AT_ONCE-1 :            screen_label += 1            # construct mission text            x_offset = ""            for i in range( mission_data_list[ self.top + screen_label ].name_x_offset ):                x_offset += " "            #            if save.mission > self.top + screen_label :                txt = x_offset + mission_data_list[ self.top + screen_label ].name            else :                txt = "?????"            # assign it to the label            self.labels[ screen_label ].text = txt            self.labels[ screen_label ].render_label()            self.labels[ screen_label ].update()            # lol            lbl_mission_names[ screen_label ].register_callback(set_cur_mission , self.top + screen_label)        #    ### listDisplay instancemission_display = listDisplay()# load all mission datafilename_prefix = "missions/"filename_suffix = ".xml"for i in range( mission_count ) :    m = mission.missionData()    m.loadFromFile( filename_prefix + str(i+1) + filename_suffix , False)    mission_data_list.append( m )"""    State control methods"""def quit_to_menu ():    save.clear()    out.pl("cleared current save state")#def menu_btn_pressed ( which ):    # use these globals    global change_state, lbl_title, btn_quit, btn_nav, lbl_mission_names, gi_filename, cur_mission_num    if which == "menu" :        out.pl("quit button pressed")        quit_to_menu()    if which == "game" :        if not (gi_filename == "nope") :            out.pl("play button pressed")        else :            return    # switch state    change_state = which#def navigate ( direction ):    global mission_display    if direction == "up":        mission_display.navigateUp()    elif direction == "down":        mission_display.navigateDown()#def set_cur_mission ( which ) :    global cur_mission_num, gi_filename, mission_data_list    cur_mission_num = which    if cur_mission_num < save.mission :        gi_filename = mission_data_list[ cur_mission_num ].level    else :        gi_filename = "nope"#"""    Mission state main methods"""def init ():    # use these globals    global mission_display    global change_state, lbl_title, btn_quit, btn_nav, lbl_mission_names, btn_play    lbl_mission_names = []    # reset change_state    change_state = ""    gi_filename = "levels/1.xml"    cur_mission_num = 0    # initialize lbl_title    lbl_title.x = 220    lbl_title.y = 10    lbl_title.font = FONTS.setnextloadsize(30).Clacon30    lbl_title.text = "Mission Select"    lbl_title.textcolour = (255,255,255)    lbl_title.drawback = False    lbl_title.wordwrap = False    lbl_title.update()    # initialize quit button    btn_quit.x = 10    btn_quit.y = 449    btn_quit.horpad = 4    btn_quit.verpad = 4    btn_quit.font = FONTS.setnextloadsize(16).Clacon16    btn_quit.text = "quit"    btn_quit.textcolour = (255,255,255)    btn_quit.backcolour = (40,40,40)    btn_quit.hoverchange = True    btn_quit.calculate()    btn_quit.register_callback(menu_btn_pressed , "menu")    # initialize up and down buttons    for i,b in enumerate(btn_nav):        b.x = 120        if i == 0:            b.y = 50        elif i == 1:            b.y = 400        b.horpad = 4        b.verpad = 4        b.font = FONTS.setnextloadsize(16).Clacon16        if i == 0:            b.text = "^"        elif i == 1:            b.text = "v"        b.textcolour = (255,255,255)        b.backcolour = (40,40,40)        b.hoverchange = True        b.calculate()        if i == 0:            b.register_callback(navigate , "up")        elif i == 1:            b.register_callback(navigate , "down")    # initialzie mission name display boxes    y_offset = 86    y_spacing = 65    for i in range( 5 ) : # !!!!!!!!!!!!!!! number of display items on screen at once !!!!!!!!!!!!!!!        lbl_mission_names.append( gui.button.button() )        lbl_mission_names[ i ].x = 30        lbl_mission_names[ i ].y = y_offset + ( y_spacing * i )        lbl_mission_names[ i ].horpad = 4        lbl_mission_names[ i ].verpad = 16        #lbl_mission_names[ i ].width = 200        #lbl_mission_names[ i ].height = 40        lbl_mission_names[ i ].font = FONTS.setnextloadsize(16).Clacon16        lbl_mission_names[ i ].text = "init"        lbl_mission_names[ i ].textcolour = (255,255,255)        lbl_mission_names[ i ].backcolour = (40,40,40)        lbl_mission_names[ i ].hoverchange = True        lbl_mission_names[ i ].calculate()    #    mission_display.linkLabels( lbl_mission_names )    # initialize play button    btn_play.x = 400    btn_play.y = 418    btn_play.horpad = 8    btn_play.verpad = 16    btn_play.font = FONTS.setnextloadsize(24).Clacon24    btn_play.text = "Play!"    btn_play.textcolour = (255,255,255)    btn_play.backcolour = (40,40,40)    btn_play.hoverchange = True    btn_play.calculate()    btn_play.register_callback(menu_btn_pressed , "game")#def update ():    # use these globals    global change_state, lbl_title, btn_quit, btn_nav, lbl_mission_names, btn_play    # update the buttons    btn_quit.update()    btn_play.update()    for b in btn_nav:        b.update()    #    # update the mission list labels    mission_display.updateLabels()    #def draw ( wsurface ):    # use these globals    global change_state, lbl_title, btn_quit, btn_nav, lbl_mission_names, btn_play    # draw heading label and main buttons    lbl_title.draw( wsurface )    btn_quit.draw( wsurface )    btn_play.draw( wsurface )    for b in btn_nav:        b.draw( wsurface )    #    mission_display.draw( wsurface )#