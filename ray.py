"""    ray.py         - NOTES     individual rays do NOT interact with each other         - machine    A class to calculate and draw 2d rays that reflect off the environment.    If rays collide with any game objects in environment.py then their     appropriate methods are called.         - _slot     Class used by machine.     Represents a slot for a ray sequence in the ray machine, can      also be 'inactive'/not used.        - _ray    Class used by _slot.    Represents a ray with an endpoint comonent. Used for storing the     reflection point on a ray.        Depends on:        environment.py"""import sysimport euclidimport environmentimport mathsys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport pygamefrom pygame.locals import *import app_constantsclass _ray:    ray_ = euclid.Ray2( euclid.Point2() , euclid.Vector2(1,1) )    vec_ = euclid.Vector2(1,1)    end_ = euclid.Point2()    len_ = 0.0        def __init__( self , ray ):        self.ray_ = ray        self.vec_ = ray.v        self.end_ = euclid.Point2( ray.p.x + ray.v.x*10000 , ray.p.y + ray.v.y*10000 )        def restrict( self, end_point ):        self.end_ = end_point        x1 = self.ray_.p.x        y1 = self.ray_.p.y        x2 = self.end_.x        y2 = self.end_.y        self.len_ = math.sqrt( pow(x2-x1,2) + pow(y2-y1,2) )        def get_norm_vec( self ):        if (self.vec_.x>1 or self.vec_.x<-1 )and( self.vec_.y>1 or self.vec_.y<-1 ):            x1 = self.ray_.p.x            y1 = self.ray_.p.y            x2 = self.end_.x            y2 = self.end_.y            self.len_ = math.sqrt( pow(x2-x1,2) + pow(y2-y1,2) )            v = self.vec_            v.x /= self.len_            v.y /= self.len_            return v        else:            return self.vec_        def draw( self , window_surface ):        #import pdb; pdb.set_trace() # break point        x1 = self.ray_.p.x        y1 = self.ray_.p.y        x2 = self.end_.x        y2 = self.end_.y        pygame.draw.line( window_surface, (255,0,0), (x1,y1), (x2,y2), 1 )class _slot:    active_ = False    rays_ = []    colour_ = (255,255,255)        def __init__( self , ray_colour=(255,0,0) ):        self.active = False        colour_ = ray_colour        def clear( self ):        self.rays_ = []        self.colour = (255,255,255)        self.active_ = False;        def isActive( self ):        return self.active_        def isInactive( self ):        return ( not self.active_ )        def activate( self , start_point , direction_vector ):        if self.active_:            out.pl( "ray.py ERROR, _slot.activate() slot already active." )        else:            self.active_ = True            self.rays_ = []            #self.rays_[0] = _ray( euclid.Ray2( start_point, direction_vector ) )            self.rays_.append( _ray( euclid.Ray2( start_point, direction_vector ) ) )        def deactivate( self ):        self.active_ = False        self.clear()        def getRay( self , degree ):        return self.rays_[degree] # is this bad?        def draw( self , window_surface ):        if not self.active_:            return        pygame.draw.circle( window_surface, (255,255,255), self.rays_[0].ray_.p1, 5, 0 )        for ray in self.rays_:            ray.draw( window_surface )        def calculate( self , environment , degree=0 ): # degree used for recursion        # - OPTIMISATION        #   . currently for EVERY ray, all of the environment's line segs are looped through. Could possibly narrow the search down a bit?        #   . currently square root is being used to determine relative distance, not neccessary.                # - NOTES        #   . I might want to re-write this with more comments, better structure and better variable names        #   . Will crash if a ray is parallel with a ref-line-seg and it detects an intersection (player is inside a line)                # determine the closect intersection point between the incident ray and the environment        #import pdb; pdb.set_trace() # break point        if degree == 0:            self.rays_[1:] = []        closest_intsct = euclid.Point2(-1, -1)        closest_c_intsct = euclid.Point2(-1, -1)        intsct_type_is_line = True                closest_lineseg = -1        #import pdb; pdb.set_trace() # break point        for index, lineseg in enumerate( environment.reflectable_line_segment_list_ ):            intsct = lineseg.intersect( self.rays_[degree].ray_ )            #import pdb; pdb.set_trace() # break point            if type( intsct ) == euclid.Point2:                intsct_type_is_line = True                if closest_lineseg == -1:                    closest_intsct = intsct                    closest_lineseg = index                else:                    #import pdb; pdb.set_trace() # break point                    if (closest_intsct.distance( self.rays_[degree].ray_.p1 ))  >  (intsct.distance( self.rays_[degree].ray_.p1 )):                        closest_intsct = intsct                        closest_lineseg = index                # test for circle intersection        if app_constants.values.debug_flag_1 == True:            import pdb; pdb.set_trace() # break point        closest_circle = -1        closest_c_intersect = euclid.Point2(100,100)        circle_intsct = euclid.LineSegment2( euclid.Point2(9999,9999) , euclid.Point2(10000,10000) )        for index, circle in enumerate( environment.reflectable_circle_list_ ):            if app_constants.values.debug_flag_1 == True:                import pdb; pdb.set_trace() # break point            #import pdb; pdb.set_trace() # break point            circle_intsct = circle.intersect( self.rays_[degree].ray_ )            if app_constants.values.debug_flag_1 == True:                import pdb; pdb.set_trace() # break point            if type( circle_intsct ) == euclid.LineSegment2:                if app_constants.values.debug_flag_1 == True:                    import pdb; pdb.set_trace() # break point                if not circle_intsct.p1 == circle_intsct.p2: # prevent tangential intersections                    intsct_type_is_line = False                    # determine which of the intersection points is closer to the start of the incident ray                    if (circle_intsct.p1.distance( self.rays_[degree].ray_.p1 ))  >  (circle_intsct.p2.distance( self.rays_[degree].ray_.p1 )):                        circle_intsct_point = circle_intsct.p2                    else:                        circle_intsct_point = circle_intsct.p1                                            if closest_circle == -1:                        closest_circle = index                        closest_c_intersect = circle_intsct_point                    else:                        if (closest_c_intersect.distance( self.rays_[degree].ray_.p1 ))  >  (circle_intsct_point.distance( self.rays_[degree].ray_.p1 )):                            closest_circle = index                            closest_c_intersect = circle_intsct_point                                                                # if no intersection, exit the function        #import pdb; pdb.set_trace() # break point        if closest_lineseg == -1 and closest_circle == -1:            return                    if intsct_type_is_line == True:            final_closest_intsct = closest_intsct        else:            final_closest_intsct = closest_c_intersect                # if there are circle and line intersections, determine which is closer        if (not closest_lineseg == -1) and (not closest_circle == -1):            if ((closest_intsct.distance( self.rays_[degree].ray_.p1 ))  >  (closest_c_intersect.distance( self.rays_[degree].ray_.p1 ))):                final_closest_intsct = closest_c_intersect                intsct_type_is_line = False            else:                final_closest_intsct = closest_intsct                intsct_type_is_line = True                # restrict incident line draw length        self.rays_[degree].restrict( final_closest_intsct )                # exit functionn now if we're past the max recursion limit        if app_constants.values._max_reflection_depth == degree:            return                # found intersection point, get it out of the line to prevent it bouncing off the line it just touched.        final_closest_intsct += -self.rays_[degree].get_norm_vec() * 1        final_closest_intsct += -self.rays_[degree].get_norm_vec() * 1 # MIGHT WANT TO COMMENT THIS OUT?                #  calculate vector reflection                # definitions        ref_vec = euclid.Vector2(-1,-1) # the reflected vector        if intsct_type_is_line == True:            ls = environment.reflectable_line_segment_list_[closest_lineseg] # the line segment the incident ray is hitting        else:            # calculate tangent            cc_x = environment.reflectable_circle_list_[closest_circle].c.x            cc_y = environment.reflectable_circle_list_[closest_circle].c.y            vec_to_intsct_x = final_closest_intsct.x - cc_x            vec_to_intsct_y = final_closest_intsct.y - cc_y            tangent_line = euclid.Line2( final_closest_intsct , euclid.Vector2(-vec_to_intsct_y,vec_to_intsct_x) )            p1_x = final_closest_intsct.x + -vec_to_intsct_y            p1_y = final_closest_intsct.y + vec_to_intsct_x            ls = euclid.LineSegment2( final_closest_intsct , euclid.Point2(p1_x , p1_y) )                    dx = ls.p2.x - ls.p1.x        dy = ls.p2.y - ls.p1.y        len = math.sqrt( (dx**2) + (dy**2) )        norm_dx = float(dx)/len        norm_dy = float(dy)/len        normal = euclid.Vector2(norm_dx, norm_dy) # the normal to the line segment        incident_vec = self.rays_[degree].vec_        dot_incident_normal = ( (norm_dx*incident_vec.x) + (norm_dy*incident_vec.y) )                # calculation        ref_x = incident_vec.x - 2*dot_incident_normal*norm_dx        ref_y = incident_vec.y - 2*dot_incident_normal*norm_dy        ref_vec.x = -ref_x        ref_vec.y = -ref_y                # appending the reflected ray        self.rays_.append( _ray( euclid.Ray2( final_closest_intsct, ref_vec ) ) )                # recurse                if degree < app_constants.values._max_reflection_depth:            self.calculate(environment, degree+1)                  class machine:    ray_sequences_ = [_slot()]    ray_sequence_limit_ = 20    lowest_slot_free_ = 0        def __init__( self ):        self.initRaySeq()        def initRaySeq( self ):        self.ray_sequences_ = []        for r_ in range( self.ray_sequence_limit_ ):            self.ray_sequences_.append( _slot() )        def removeAllRaySequences( self ):        self.ray_sequences_ = []        self.ray_sequences_ = _slot()        self.lowest_slot_free_ = 0        def setLimit( self , new_limit ):        self.ray_sequence_limit_ = new_limit        self.initRaySeq()        def removeLimit( self ):        self.ray_sequence_limit_ = 20        self.initRaySeq()        def addRaySequence( self , start_point , direction_vector ): # start_point type euclid.Point2, direction_vector type euclid.Vector2        #import pdb; pdb.set_trace() # break point        if self.lowest_slot_free_ > self.ray_sequence_limit_:            out.pl("ERROR. ray.py machine addRaySequence() Exceeded ray limit ._.")            return        for pos, slot in enumerate( self.ray_sequences_ ):            #import pdb; pdb.set_trace() # break point            if slot.isInactive():                #import pdb; pdb.set_trace() # break point                self.lowest_slot_free_ = pos+1                slot.activate( start_point, direction_vector )                #import pdb; pdb.set_trace() # break point                break        return self.lowest_slot_free_ - 1        def appendRaySequence( self , index , start_point , direction_vector ):        self.ray_sequences_[index].deactivate()        self.ray_sequences_[index].activate( start_point, direction_vector )        def removeRaySequence( self , slot_number ):        if self.ray_sequences_[slot_number].isActive():            self.ray_sequences_[slot_number].deactivate()            if slot_number < self.lowest_slot_free_:                self.lowest_slot_free = slot_number        def draw( self , window_surface ):        # - OPTIMISATION        #   check weather ray seq. is active before calling draw function?        #import pdb; pdb.set_trace() # break point        for rayseq in self.ray_sequences_:            #import pdb; pdb.set_trace() # break point            if rayseq.isActive():                rayseq.draw(window_surface)        def calculate( self , environment ):        #import pdb; pdb.set_trace() # break point        for rayseqs in self.ray_sequences_:            #import pdb; pdb.set_trace() # break point            if rayseqs.isActive():                rayseqs.calculate( environment )