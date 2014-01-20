"""    draw.py        methods to draw physicsworld"""import syssys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import euclidimport stateimport ray# drawState()def drawState( wsurface , linecol=(255,255,255) , circlecol=(255,255,255)):    for o in state.objects:        # check if we've reached the end of the object list        if o == None:            break        # render lines        if o.type == 0 and o.render == True:            pygame.draw.line( wsurface , linecol , (o.x1 , o.y1) , (o.x2 , o.y2) , 1 )        # render circles        if o.type == 1:            pygame.draw.circle( wsurface , circlecol ,  (o.x , o.y) , int(o.radius) , 1 )# drawRaySeq()def drawRaySeq( wsurface , rs , raycol=(255,0,0)):    import pdb; pdb.set_trace() # break point    for rr in rs.ray_list:            # get start point        start_point = rr.e_ray.p1        import pdb; pdb.set_trace() # break point                if rr.end_point == None:            # calculate end point if ray isn't restricted            uvec = rr.getUnitVector()            end_point = rr.e_ray.p1            end_point.x += uvec.x*1000            end_point.y += uvec.y*1000        else:            # if the ray is restricted just get it's end point            end_point = rr.end_point.x                # draw        pygame.draw.line( wsurface , raycol , (start_point.x,start_point.y) , (end_point.x,end_point.y) , 1 )