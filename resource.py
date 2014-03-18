"""    resource.py        tvm http://www.pygame.org/wiki/LazyImageLoading?parent=CookBook         - ResourceController    Should not be used directly. Other resource managers inherit from this base    class to manage resources    """import pygameimport weakrefimport syssys.path.append("C:/Python27/proj/BetterConsoleFunctions/V3")import bcfout = bcfimport app_constantsunit_test = Falseload_data = [] class ResourceController(object):    def __init__(self, loader):        self.__dict__.update(dict(            names = {},            cache = weakref.WeakValueDictionary(),            loader = loader        ))            def __setattr__(self, name, value):        self.names[name] = value            def __getattr__(self, name):        global load_data        try:            img = self.cache[name]        except KeyError:            img = self.loader(self.names[name],load_data)            load_data = []            self.cache[name] = img            if app_constants.values.print_loading:                out.pl("~~[RESOURCE LOAD] '" + str(name) + "'")        return img            class textureManager(ResourceController):    def __init__(self):        ResourceController.__init__(self, textureManager.loadtexture)    @staticmethod    def loadtexture ( filename , data=[] ):        return pygame.image.load( filename )class fontManager(ResourceController):    def __init__(self):        pygame.font.init()        ResourceController.__init__(self, fontManager.loadfont)    @staticmethod    def loadfont ( filename , data=[] ):        if data == []:            data.append( 16 ) # default font size        return pygame.font.Font(filename , data[0])        def setnextloadsize ( self , size ):        global load_data        """            returns the module for chaining of sized font loading:                            'myfont = FONTS.setnextloadsize(16).SomeFont'                    """        load_data = [ size ]        return self## used by the rest of the programTEXTURES = textureManager()FONTS = fontManager()## define all fonts that the program uses (for easy access)KarmaFuture_file = "graphics/fonts/KarmaFuture.ttf"FONTS.KarmaFuture = KarmaFuture_fileFONTS.KarmaFuture50 = KarmaFuture_fileClacon_file = "graphics/fonts/clacon.ttf"FONTS.Clacon = Clacon_fileFONTS.Clacon16 = Clacon_fileFONTS.Clacon22 = Clacon_fileFONTS.Clacon30 = Clacon_file#if unit_test:    # test the resource module    FONTS.load_data = [8]    FONTS.clacon8 = "graphics/fonts/clacon.ttf"    FONTS.load_data = [16]    FONTS.clacon16 = "graphics/fonts/clacon.ttf"    FONTS.load_data = [32]    FONTS.clacon32 = "graphics/fonts/clacon.ttf"    f1 = FONTS.clacon8    f2 = FONTS.clacon16    f3 = FONTS.clacon32    sys.exit() # terminate program