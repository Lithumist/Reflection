"""    devconsole.py        Set of functions that create a developer console accepting different commands.            changelvl [level filename]              loads and switches to                                             the specified level.        #    """import sysimport ossys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsfrom app_constants import cwdfrom app_constants import makeRelativePathimport game# globalsstr_text_entered = ""console_font = Nonestr_ren_heading = "Developer Console. Press ` (tilde) to close"str_ren_base_cmd = "> "str_ren_outbase_cmd = "> "str_ren_final_cmd = ""str_out = ""str_ren_final_out = ""suf_heading = 0suf_cmd = 0suf_out = 0dontquit = Truedopython = Falsepycode = ""str_finish = ""# init()def init():    global console_font    pygame.font.init()    console_font = pygame.font.Font( makeRelativePath("graphics/fonts/clacon.ttf"), 20 )# execute_python_code()def execute_python_code( code , done_text):    """ actual code executing is done in app.py """    """ To make the scope 'global' or application wide """    global dopython    global pycode    global str_finish        dopython = True    pycode = code    str_finish = done_text# events()def events( ev ):        global str_text_entered        if ev.type == KEYDOWN:            if ev.key == pygame.K_RETURN:                _interpret_command()            elif ev.key == pygame.K_BACKSPACE:                str_text_entered = str_text_entered[0:-1]            elif ev.key == pygame.K_BACKQUOTE:                pass            else:                char = ev.unicode                str_text_entered += char                #out.pr(char)# update()def update():    global str_ren_final_cmd    global str_ren_base_cmd    global str_text_entered    global str_ren_final_out    global str_out    global str_ren_outbase_cmd    global dontquit        """ update the final strings """    str_ren_final_cmd = str_ren_base_cmd + str_text_entered    str_ren_final_out = str_ren_outbase_cmd + str_out        return dontquit# draw()def draw( pss ):    #import pdb; pdb.set_trace() # break point    global suf_heading    global suf_cmd    global console_font    suf_heading = console_font.render( str_ren_heading , False , (255,255,255) , (0,0,0))    suf_cmd = console_font.render( str_ren_final_cmd , False , (255,255,255) , (0,0,0))    suf_out = console_font.render( str_ren_final_out , False , (255,255,255) , (0,0,0))        pss.blit(suf_heading, (0,0))    pss.blit(suf_cmd, (0,16))    pss.blit(suf_out, (0,464))# _interpret_command()def _interpret_command():    global str_text_entered    global str_out    global dontquit    global dopython    global pycode            ss = str_text_entered.split(" ")    ss[0] = ss[0].lower()    success = False        if ss[0] == "hello":        success = True        str_out = "Hello World!"        if ss[0] == "clear" or ss[0] == "cls":        success = True        str_out = ""        if ss[0] == "write" or ss[0] == "print":        success = True        for index, word in enumerate(ss):            if not index == 0:                str_out += word + " "        if ss[0] == "exit" or ss[0] == "quit":        success = True        str_out = ":( "        dontquit = False        if ss[0] == "python" or ss[0] == "execute":        success = True        str_out = "Executing python code..."        ss.pop(0)        execute_python_code(' '.join(ss), "Python code executed")        if ss[0] == "givemoney" or ss[0] == "addmoney":        success = True        str_out = "Giving money..."        execute_python_code("save.money += " + ss[1], ss[1] + " money given")        if ss[0] == "toggle" or ss[0] == "flip":        success = True        if ss[1] == "objarr":            execute_python_code("physicsworld.draw.debug_draw = not physicsworld.draw.debug_draw", "object array debug draw toggled")        else:            str_out = "Unknown setting " + ss[1]        if ss[0] == "endgame" or ss[0] == "end":        success = True        str_out = "Ending game..."        execute_python_code('end_game()', "Current game ended")        if ss[0] == "startgame" or ss[0] == "start":        success = True        str_out = "Starting game " + ss[1]        execute_python_code('start_game("' + ss[1] + '")', "Started game " + ss[1])                        if not success:        str_out = "Unknown command, '" + str_text_entered + "'"    str_text_entered = ""