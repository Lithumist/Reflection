"""    physicsworld/state.py        a group of variables and methods to manage the physicsworld state    also has methods for performing the physics calaulcations"""unittest = Falseimport syssys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport object# list of physics objects w/ methodsobjects = []objects_full = Falselowest_free_index = 0def addObject ( obj ): # returns index of newly added object or -1 if full    global objects    global objects_full    global lowest_free_index    if objects_full:        return -1    objects[lowest_free_index] = obj    return_index = lowest_free_index    updateLowestFreeIndex( True )    return return_indexdef delObject ( index ):    global objects    objects[index] = None    updateLowestFreeIndex()def updateLowestFreeIndex ( add=False ):    global objects    global objects_full    global lowest_free_index    global max_physics_objects    # optimisation:    # if we've just added an element we don't have to search though the whole    # list bottom up, just from where the previous free space was    if add:        for x in range( max_physics_objects - lowest_free_index-1 ):            if objects[x + lowest_free_index+1] == None:                lowest_free_index += x + 1                return        # if we didn't find any free space        objects_full = True    # for other cases:    # where we do have to search though the whole list bottom up    else:        for i in range (max_physics_objects):            if objects[i] == None:                lowest_free_index = i                return        # if we didn't find any free space        objects_full = True# initialzation and settingsmax_physics_objects = -1def start ( mpo ):    global objects    global max_physics_objects    # reserve space in the object list    max_physics_objects = mpo    objects = [None]*mpo# unit testif unittest:    a = object.object( 0 , True , False , 1 , 2 , 3 , 4 )    b = object.object( 1 , False , False , 1 , 2 , 3 )        start( 10 )        import pdb; pdb.set_trace() # break point        a1index = addObject( a )        import pdb; pdb.set_trace() # break point        a2index = addObject( a )        import pdb; pdb.set_trace() # break point        delObject( a1index )        import pdb; pdb.set_trace() # break point        b1index = addObject( b )        import pdb; pdb.set_trace() # break point