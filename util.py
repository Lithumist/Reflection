"""    util.py        set of useful functions to assist the rest of the game"""import randomdef mutate_colour_random ( intensity , colour ):    """        mutates a given colour's r,g,b components by +- 'intensity'        returns the result                colour must be in (red,green,blue) format        returned colour is also in this format    """    # get current colour    (r_cur,g_cur,b_cur) = colour    # generate the preliminary new colour components    cmat = [r_cur+random.randint(-intensity,intensity) , g_cur+random.randint(-intensity,intensity) , b_cur+random.randint(-intensity,intensity)]    # cap the components off at 0-255    for i,c in enumerate(cmat):        if c > 255:            cmat[i] = 255        if c < 0:            cmat[i] = 0    # return the final colour matrix as a colour triple    return (cmat[0],cmat[1],cmat[2])