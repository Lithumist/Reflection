"""    main_menu.py        title and main menu state        My face when I look at this code..    ._."""import sysimport osimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathfrom app_constants import TEXTURES# internal state# 0  title screen# 1  main menustate = 0# stringstitle_msg = "Press any key to continue."# animationdraw_title_msg = Truedraw_title_msg_delay = 1000 # millisecondsdraw_title_msg_delay_last = 0 # milliseconds# font(s)font_title = -1# surfacessurf_title_text = -1surf_title_background = -1# event variablesany_key_pressed = False""" init """# should be called before any other functionsdef init ():    # use these global variables    global state    global draw_title_msg_delay_last    global font_title    global surf_title_text    global surf_title_background    # make sure we're in the title screen    state = 0    # init animation    draw_title_msg_delay_last = pygame.time.get_ticks()    # load textures    TEXTURES.title_background = "graphics/backgrounds/blue.png"    surf_title_background = TEXTURES.title_background    surf_title_background.convert()    # load fonts    font_title = pygame.font.Font( makeRelativePath("graphics/fonts/clacon.ttf"), 20 )    # pre render some surfaces (mainly text)    surf_title_text = font_title.render( title_msg , False , (255,255,255) , (255,0,255))    surf_title_text.set_colorkey((255,0,255))""" events """# handles all eventsdef events ( ev ):    # use these global variables    global any_key_pressed    # update the any key variables    if ev.type == KEYDOWN:        any_key_pressed = True    else:        any_key_pressed = False""" draw """# draws the current statedef draw ( wsurface ):    # use these global variables    global state    global title_msg    global draw_title_msg    global font_title    global surf_title_text    # title menu    if state == 0:        wsurface.blit(TEXTURES.title_background, (0,0))        if draw_title_msg:            wsurface.blit(surf_title_text, (190,430))""" animation """# does logic for all animated thingsdef animation ():    # use these global variables    global state    global draw_title_msg    global draw_title_msg_delay    global draw_title_msg_delay_last    # update draw_title_msg_delay    if pygame.time.get_ticks() > draw_title_msg_delay_last + draw_title_msg_delay:        draw_title_msg = not draw_title_msg        draw_title_msg_delay_last = pygame.time.get_ticks()""" logic """# does the main state logicdef logic ():    # use these globals    global state    global any_key_pressed    # title screen logic    if state == 0:        if any_key_pressed:            state = 1    elif state == 1:        pass