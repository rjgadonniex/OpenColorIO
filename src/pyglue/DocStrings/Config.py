
class Config:
    """
    Config
    """
    
    def __init__(self):
        pass

    def CreateFromEnv(self):
        """
        CreateFromEnv()
        
        Create a :py:class:`PyOpenColorIO.Config` object using the environment variable.
                     
        :returns: Config object
        """
        pass

    def CreateFromFile(self):
        """
        CreateFromFile(filename)
        
        Create a :py:class:`PyOpenColorIO.Config` object using the information in a file.
        
        :param filename: name of file
        :type filename: string
        :return: Config object
        """
        pass

    def isEditable(self):
        """
        isEditable()
        
        Returns whether Config is editable.
        
        The configurations returned from
        :py:function:`PyOpenColorIO.GetCurrentConfig` are not editable, and if
        you want to edit them you can use
        :py:method:`PyOpenColorIO.Config.createEditableCopy`.
           
        If you attempt to call any of the set functions on a noneditable
        Config, an exception will be thrown.
           
        :return: state of :py:class:`PyOpenColorIO.Config`'s editability
        :rtype: bool
        """
        pass

    def createEditableCopy(self):
        """
        createEditableCopy()
        
        Returns an editable copy of :py:class:`PyOpenColorIO.Config`.
        
        :return: editable copy of :py:class:`PyOpenColorIO.Config`
        :rtype: Config object
        """
        pass

    def sanityCheck(self):
        """
        sanityCheck()
        
        This will throw an exception if :py:class:`PyOpenColorIO.Config` is
        malformed. The most common error occurs when references are made to
        colorspaces that do not exist.
        """
        pass

    def getDescription(self):
        """
        getDescription()
        
        Returns the stored description of :py:class:`PyOpenColorIO.Config`.
           
        :return: stored description of :py:class:`PyOpenColorIO.Config`
        :rtype: string
        """
        pass

    def setDescription(self):
        """
        setDescription(desc)
        
        Sets the description of :py:class:`PyOpenColorIO.Config`.
        
        :param desc: description of :py:class:`PyOpenColorIO.Config`
        :type desc: string
        """
        pass

    def serialize(self):
        """
        serialize()
        
        Returns the string representation of :py:class:`PyOpenColorIO.Config`
        in YAML text form. This is typically stored on disk in a file with the
        .ocio extension.
        
        :return: :py:class:`PyOpenColorIO.Config` in YAML text form
        :rtype: string
        """
        pass

    def getCacheID(self):
        """
        getCacheID([, pycontext])
        
        This will produce a hash of the all colorspace definitions, etc.
        
        All external references, such as files used in FileTransforms, etc.,
        will be incorporated into the cacheID. While the contents of the files
        are not read, the file system is queried for relavent information
        (mtime, inode) so that the :py:class:`PyOpenColorIO.Config`'s cacheID
        will change when the underlying luts are updated.
        
        If a context is not provided, the current Context will be used. If a
        null context is provided, file references will not be taken into
        account (this is essentially a hash of :py:method:`PyOpenColorIO.Config.serialize`).
           
        :param pycontext: optional
        :type pycontext: object
        :return: hash of :py:class:`PyOpenColorIO.Config`
        :rtype: string
        """
        pass

    def getSearchPath(self):
        """
        getSearchPath()
        
        Returns the search path.
        
        :return: search path
        :rtype: string
        """
        pass

    def setSearchPath(self):
        """
        setSearchPath(path)
        
        Sets the search path.
        
        :param path: the search path
        :type path: string
        """
        pass

    def getWorkingDir(self):
        """
        getWorkingDir()
        
        Returns the working directory.
        
        :return: the working directory
        :rtype path: string
        """
        pass

    def setWorkingDir(self):
        """
        setWorkingDir(path)
        
        Sets the working directory.
        
        :param path: the working directory
        :type path: string
        """
        pass

    def getColorSpaces(self):
        """
        getColorSpaces()
        
        Returns all the ColorSpaces defined in :py:class:`Config`.
           
        :return: ColorSpaces in :py:class:`PyOpenColorIO.Config`
        :rtype: tuple
        """
        pass

    def getColorSpace(self):
        """
        getColorSpace(name)
        
        Returns the data for the specified color space in :py:class:`Config`.
        
        This will return null if the specified name is not found.
        
        :param name: name of color space
        :type name: string
        :return: data for specified color space
        :rtype: pyColorSpace object
        """
        pass

    def addColorSpace(self):
        """
        addColorSpace(pyColorSpace)
        
        Add a specified color space to :py:class:`PyOpenColorIO.Config`.
        
        :param pyColorSpace: color space
        :type pyColorSpace: object
        
        .. note::
           If another color space is already registered with the same name,
           this will overwrite it.
        """
        pass

    def clearColorSpaces(self):
        """
        clearColorSpaces()
        
        Clear the color spaces in :py:class:`PyOpenColorIO.Config`.
        """
        pass

    def parseColorSpaceFromString(self):
        """
        parseColorSpaceFromString(str)
        
        Parses out the color space from a string.
        
        Given the specified string, gets the longest, right-most color space substring.
        * If strict parsing is enabled, and no color space is found, return an empty string.
        * If strict parsing is disabled, return the default role, if defined.
        * If the default role is not defined, return an empty string.
        
        :param str: ColorSpace data
        :type str: string
        :return: parsed data
        :rtype: string
        """
        pass

    def setRole(self):
        """
        setRole(role, csname)
        
        Set a role's ColorSpace.
        
        Setting the colorSpaceName name to a null string unsets it.
        
        :param role: role whose ColorSpace will be set
        :type role: string
        :param csname: name of ColorSpace
        :type csname: string
        """
        pass
        
    def getDefaultDisplay(self):
        """
        getDefaultDisplay()
        
        Returns the default display set in :py:class:`PyOpenColorIO.Config`.
        
        :return: default display
        :rtype: string 
        """
        pass

    def getDisplays(self):
        """
        getDisplays()
        
        Returns all the displays defined in :py:class:`PyOpenColorIO.Config`.
        
        :return: displays in :py:class:`Config`
        :rtype: list of strings
        """
        pass

    def getDefaultView(self):
        """
        getDefaultView(display)
        
        Returns the default view of :py:class:`PyOpenColorIO.Config`.
        
        :param display: default view
        :type display: string
        :return: view
        :rtype: string
        """
        pass

    def getViews(self):
        """
        getViews(display)
        
        Returns all the views defined in :py:class:`PyOpenColorIO.Config`.
        
        :param display: views in :py:class:`Config`
        :type display: string
        :return: views in :py:class:`Config`.
        :rtype: list of strings
        """
        pass

    def getDisplayColorSpaceName(self):
        """
        getDisplayColorSpaceName(display, view)
        
        Returns the ColorSpace name corresponding to the display and view
        combination in :py:class:`PyOpenColorIO.Config`.
        
        :param display: display
        :type display: string
        :param view: view
        :type view: string
        :return: display color space name
        :rtype: string
        """
        pass
    def getDisplayLooks(self):
        """
        getDisplayLooks(display, view)
        
        Returns the looks corresponding to the display and view combination in
        :py:class:`PyOpenColorIO.Config`.
        
        :param display: display
        :type display: string
        :param view: view
        :type view: string
        :return: looks
        :rtype: string
        """
        pass
    def addDisplay(self):
        """
        addDisplay(display, view, colorSpaceName[, looks])
        
        NEEDS WORK
        
        :param display:
        :type display: string
        :param view: 
        :type view: string
        :param colorSpaceName: 
        :type colorSpaceName: string
        :param looks: optional
        :type looks: string
        """
        pass

    def clearDisplays(self):
        """
        clearDisplays()
        """
        pass

    def setActiveDisplays(self):
        """
        setActiveDisplays(displays)
        
        Sets the active displays in :py:class:`PyOpenColorIO.Config`.
        
        :param displays: active displays
        :type displays: string
        """
        pass

    def getActiveDisplays(self):
        """
        getActiveDisplays()
        
        Returns the active displays in :py:class:`PyOpenColorIO.Config`.
        
        :return: active displays
        :rtype: string
        """
        pass

    def setActiveViews(self):
        """
        setActiveViews(views)
        
        Sets the active views in :py:class:`PyOpenColorIO.Config`.
        
        :param views: active views
        :type views: string
        """
        pass

    def getActiveViews(self):
        """
        getActiveViews()
        
        Returns the active views in :py:class:`PyOpenColorIO.Config`.
        
        :return: active views
        :rtype: string
        """
        pass

    def getDefaultLumaCoefs(self):
        """
        getDefaultLumaCoefs()
        
        Returns the default luma coefficients in :py:class:`PyOpenColorIO.Config`.
           
        :return: luma coefficients
        :rtype: list of floats
        """
        pass

    def setDefaultLumaCoefs(self):
        """
        setDefaultLumaCoefs(pyCoef)
        
        Sets the default luma coefficients in :py:class:`PyOpenColorIO.Config`.
        
        :param pyCoef: luma coefficients
        :type pyCoef: object
        """
        pass

    def getLook(self):
        """
        getLook(str)
        
        Returns the information of a specified look in
        :py:class:`PyOpenColorIO.Config`.
        
        :param str: look
        :type str: string
        :return: specified look
        :rtype: look object
        """
        pass

    def getLooks(self):
        """
        getLooks()
        
        Returns a list of all the looks defined in
        :py:class:`PyOpenColorIO.Config`.
        
        :return: looks
        :rtype: tuple of look objects
        """
        pass

    def addLook(self):
        """
        addLook(pylook)
        
        Adds a look to :py:class:`PyOpenColorIO.Config`.
        
        :param pylook: look
        :type pylook: look object
        """
        pass

    def clearLook(self):
        """
        clearLook()
        
        Clear look in :py:class:`PyOpenColorIO.Config`.
        """
        pass

    def getProcessor(self):
        """
        getProcessor(arg1[, arg2[, direction[, context]])
        
        Returns a processor for a specified transform.
        
        Although this is not often needed, it allows for the reuse of atomic
        OCIO functionality, such as applying an individual LUT file.
        
        There are two canonical ways of creating a
        :py:class:`PyOpenColorIO.Processor`:
        
        #. Pass a transform into arg1, in which case arg2 will be ignored. 
        #. Set arg1 as the source and arg2 as the destination. These can be
           ColorSpace names, objects, or roles.
        
        Both arguments, ``direction`` (of transform) and ``context``, are
        optional and respected for both methods of
        :py:class:`PyOpenColorIO.Processor` creation.
        
        This will fail if either the source or destination color space is null.
        
        See Python: Processor for more details.
        
        .. note::
            This may provide higher fidelity than anticipated due to internal
            optimizations. For example, if inputColorSpace and outputColorSpace
            are members of the same family, no conversion will be applied, even
            though, strictly speaking, quantization should be added.
            
            If you wish to test these calls for quantization characteristics,
            apply in two steps; the image must contain RGB triples (though
            arbitrary numbers of additional channels can be optionally
            supported using the pixelStrideBytes arg). ???
        
        :param arg1: 
        :type arg1: object
        :param arg2: ignored if arg1 is a transform
        :type arg2: object
        :param direction: optional
        :type direction: string
        :param context: optional
        :type context: object
        """
        pass