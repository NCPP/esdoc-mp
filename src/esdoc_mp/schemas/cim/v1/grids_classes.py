"""
CIM v1 grids package classes.
"""



def _coordinate_list():
    """Creates and returns instance of coordinate_list class."""
    return {
        'type' : 'class',
        'name' : 'coordinate_list',
        'base' : None,
        'is_abstract' : False,
        'doc' : 'The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.',
        'properties' : [
            ('has_constant_offset', 'bool', '0.1', 'Set to true if coordinates in the built array have constant offset.'),
            ('length', 'int', '0.1', 'Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.'),
            ('uom', 'str', '0.1', 'Units of measure used by the coordinates.'),
        ],
        'decodings' : [
            ('has_constant_offset', '@hasConstantOffset'),
            ('length', '@length'),
            ('uom', '@uom'),
        ]
    }


def _grid_extent():
    """Creates and returns instance of grid_extent class."""
    return {
        'type' : 'class',
        'name' : 'grid_extent',
        'base' : None,
        'is_abstract' : False,
        'doc' : 'DataType for recording the geographic extent of a gridMosaic or gridTile.',
        'properties' : [
            ('minimum_latitude', 'str', '1.1', None),
            ('maximum_latitude', 'str', '1.1', None),
            ('minimum_longitude', 'str', '1.1', None),
            ('maximum_longitude', 'str', '1.1', None),
            ('units', 'str', '0.1', None),
        ],
        'decodings' : [
            ('minimum_latitude', 'child::cim:latMin'),
            ('maximum_latitude', 'child::cim:latMax'),
            ('minimum_longitude', 'child::cim:lonMin'),
            ('maximum_longitude', 'child::cim:lonMax'),
            ('units', 'child::cim:units'),
        ]
    }


def _grid_mosaic():
    """Creates and returns instance of grid_mosaic class."""
    return {
        'type' : 'class',
        'name' : 'grid_mosaic',
        'base' : None,
        'is_abstract' : False,
        'doc' : 'The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.',
        'properties' : [
            ('citations', 'shared.citation', '0.N', 'Optional container element for specifying a list of references that describe the grid.'),
            ('description', 'str', '0.1', 'A free-text description of a grid mosaic.'),
            ('extent', 'grids.grid_extent', '0.1', None),
            ('has_congruent_tiles', 'bool', '0.1', 'Indicates whether or not all the tiles contained within a grid mosaic are congruent, that is, of the same size and shape.'),
            ('id', 'str', '1.1', 'Specifies a globally unique identifier for a grid mosaic instance. By globally we mean across all GridSpec instances/records within a given modelling activity (such as CMIP5).'),
            ('is_leaf', 'bool', '1.1', 'Indicates whether or not a grid mosaic is a leaf mosaic, that is, it only contains child grid tiles not further mosaics.'),
            ('long_name', 'str', '0.1', 'Specifies the long name associated with a grid mosaic. The long name will typically be a human-readable string, with acronyms expanded, used for labelling purposes.'),
            ('mnemonic', 'str', '0.1', None),
            ('mosaic_count', 'int', '0.1', 'Specifies the number of mosaics associated with a non-leaf grid mosaic. Set to zero if the grid mosaic is a leaf mosaic, i.e. it contains child grid tiles not mosaics.'),
            ('mosaics', 'grids.grid_mosaic', '0.N', None),
            ('short_name', 'str', '1.1', 'Specifies the short name associated with a grid mosaic. The short name will typically be a convenient abbreviation used to refer to a grid mosaic, e.g. \'UM ATM N96\'.'),
            ('tile_count', 'int', '0.1', 'Specifies the number of tiles associated with a leaf grid mosaic. Set to zero if the grid mosaic is not a leaf mosaic, i.e. it contains child grid mosaics rather than tiles. (Added to align with equivalent ESG/Curator property.)'),
            ('tiles', 'grids.grid_tile', '0.N', None),
            ('type', 'str', '1.1', 'Specifies the type of all the grid tiles contained in a grid mosaic. It is assumed that all of the tiles comprising a given grid mosaic are of the same type. The value domain is as per the specified enumeration list.'),
        ],
        'decodings' : [
            ('citations', 'child::cim:citationList/cim:citation'),
            ('description', 'child::cim:description'),
            ('has_congruent_tiles', '@congruentTiles'),
            ('id', '@id'),
            ('is_leaf', '@isLeaf'),
            ('long_name', 'child::cim:longName'),
            ('mnemonic', 'child::cim:mnemonic'),
            ('mosaic_count', '@numMosaics'),
            ('mosaics', 'child::cim:gridMosaic'),
            ('short_name', 'child::cim:shortName'),
            ('tile_count', '@numTiles'),
            ('tiles', 'child::cim:gridTile'),
            ('type', '@gridType'),
        ]
    }


def _grid_property():
    """Creates and returns instance of grid_property class."""
    return {
        'type' : 'class',
        'name' : 'grid_property',
        'base' : 'shared.property',
        'is_abstract' : False,
        'doc' : None,
        'properties' : [ ],
        'decodings' : [ ]
    }


def _grid_spec():
    """Creates and returns instance of grid_spec class."""
    return {
        'type' : 'class',
        'name' : 'grid_spec',
        'base' : None,
        'is_abstract' : False,
        'is_entity' : True,
        'doc' : 'This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML\'s AbstractGeometryType it can, and should, be identified using a gml:id attribute.',
        'properties' : [
            ('meta', 'shared.doc_meta_info', '1.1', None),
            ('esm_model_grids', 'grids.grid_mosaic', '0.N', None),
            ('esm_exchange_grids', 'grids.grid_mosaic', '0.N', None),
        ],
        'decodings' : [
            ('meta', 'self::cim:gridSpec'),
            ('esm_model_grids', 'child::cim:esmModelGrid'),
            ('esm_exchange_grids', 'child::cim:esmExchangeGrid'),
        ]
    }


def _grid_tile():
    """Creates and returns instance of grid_tile class."""
    return {
        'type' : 'class',
        'name' : 'grid_tile',
        'base' : None,
        'is_abstract' : False,
        'doc' : 'The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.',
        'properties' : [
            # TODO define types
            ('area', 'str', '0.1', 'gml:MeasureType:Specifies the area of the grid tile in the units defined by the uom attribute that is attached to the GML MeasureType data type.'),
            ('cell_array', 'str', '0.1', 'GridCellArray:This property may be used to specify an array of grid cell definitions which together define the coordinate geometry of a grid tile. Depending on context, any of the existing sub-types of GridCell may be used. Mixing types is, however, not currently permitted.'),
            ('cell_ref_array', 'str', '0.1', 'GridCellArray:This property may be used to define the coordinate geometry of a grid tile by specifying an array of references to remotely defined grid cells. Depending on context, any of the existing sub-types of GridCell may be referenced.'),
            ('coord_file', 'str', '0.1', 'This property may be used to specify the URI of a file containing grid coordinates that define the geometry of a a grid tile. It is envisaged that this will be the preferred mechanism for specifying the geometry of complex grids.'),
            ('coordinate_pole', 'str', '0.1', 'gml:PointType:The coordinatePole property may be used to specify the lat-long position of any coordinate poles (in the mathematical sense) that form part of the definition of a grid tile. Not to be confused with the gridNorthPole property.  If required, two or more coordinate pole definitions may be distinguished by setting the gml:id attribute to appropriate values, such as spole, npole, etc.'),
            ('horizontal_crs', 'str', '0.1', 'gml:CRSPropertyType:Specifies the horizontal coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external horizontal CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.'),
            ('grid_north_pole', 'str', '0.1', 'gml:PointType:If required, defines the lat-long position of the north pole used by the grid tile in the case of rotated/displaced pole grids. Not to be confused with the coordinatePole property.'),
            ('simple_grid_geom', 'str', '0.1', 'SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.'),
            ('vertical_crs', 'str', '0.1', 'gml:CRSPropertyType:Specifies the vertical coordinate reference system used in the definition of the grid tile coordinates. This property should normally be an xlink reference to an external vertical CRS definition (e.g. in a separate CRS dictionary). If required, however, the property may be defined in situ within a CIM document.'),

            ('description', 'str', '0.1', 'A free-text description of a grid tile.'),
            ('discretization_type', 'grids.discretization_enum', '0.1', 'Indicates the type of discretization applied to the grid tile, e.g. "logically_rectangular".'),
            ('extent', 'grids.grid_extent', '0.1', None),
            ('geometry_type', 'grids.geometry_type_enum', '0.1', 'Indicates the geometric figure used to approximate the figure of the Earth, e.g. "sphere".'),
            ('horizontal_resolution', 'grids.grid_tile_resolution_type', '0.1', 'Provides an indication of the approximate spatial sampling size of the grid tile, i.e. the size of the underlying grid cells. (Note: the maximum spatial resolution of the grid is twice the sampling size (e.g. 2 km for a 1 km x 1 km grid pitch).'),
            ('id', 'str', '0.1', 'Specifies an identifer for a grid tile that is unique within its parent grid mosaic. It is not required for this identifier to be unique either across all mosaics in a GridSpec or across all GridSpecs, though if that were the case it would not be detrimental.'),
            ('is_conformal', 'bool', '0.1', 'This property is used to indicate if the grid tile is conformal, i.e. angle-preserving. If so, angles measured on the grid are equal to the equivalent angles on the Earth.'),
            ('is_regular', 'bool', '0.1', 'If true, indicates that the horizontal coordinates of the grid can be defined using 1D arrays (vectors). This means that grid node locations are defined by the cartesian product of the X/Lon and Y/Lat coordinate vectors. It also means that grid cells are logically rectangular (they may also be physically rectangular in the case of projected coordinates).'),
            ('is_terrain_following', 'bool', '0.1', 'Set to true if the vertical coordinate system is terrain-following even if, as is often the case, this only applies to the lower levels of the grid.'),
            ('is_uniform', 'bool', '0.1', 'If true, indicates that horizontal coordinates have fixed offsets in the X and Y directions. If the offset is the same in both directions then the grids are logically square, otherwise they are logically rectangular. The offsets can be specified by two scalar values (or three values in the case of 3D grids).'),
            ('long_name', 'str', '0.1', None),
            ('mnemonic', 'str', '0.1', None),
            ('nx', 'int', '0.1', 'Specifies the length of the X, or longitude, dimension of the grid tile.'),
            ('ny', 'int', '0.1', 'Specifies the length of the Y, or latitude, dimension of the grid tile.'),
            ('nz', 'int', '0.1', 'Specifies the length of the Z, or height/level, dimension of the grid tile. The zcoords coordinate list property, if specified, should have this length.'),
            ('refinement_scheme', 'grids.refinement_type_enum', '0.1', None),
            ('short_name', 'str', '0.1', None),
            ('vertical_resolution', 'grids.grid_tile_resolution_type', '0.1', 'Provides an indication of the approximate resolution of the grid tile in the vertical dimension. (Added to align with corresponding ESG/Curator and DIF property).'),
            ('zcoords', 'grids.vertical_coordinate_list', '0.1', 'This optional property may be used to specify the vertical coordinates (e.g. heights or model levels) at which a grid tile is utilised or realised. In the case of simple grid tiles the equivalent zcoords property on the SimpleGridGeometry data type would be used instead. The current property is intended to be used when the horizontal grid coordinates are defined by one of the other methods.')
        ],
        'decodings' : [
            ('description', 'child::cim:description'),
            ('discretization_type', '@discretizationType'),
            ('extent', 'child::cim:extent'),
            ('geometry_type', '@geometryType'),
            ('horizontal_resolution', 'child::cim:horizontalResolution'),
            ('id', '@id'),
            ('is_conformal', '@isConformal'),
            ('is_regular', '@isRegular'),
            ('is_terrain_following', '@isTerrainFollowing'),
            ('is_uniform', '@isUniform'),
            ('long_name', 'child::cim:longName'),
            ('mnemonic', 'child::cim:mnemonic'),
            ('nx', '@nx'),
            ('ny', '@ny'),
            ('nz', '@nz'),
            ('refinement_scheme', '@refinementScheme'),
            ('short_name', 'child::cim:shortName'),
            ('vertical_resolution', 'child::cim:verticalResolution'),
            ('zcoords', 'child::cim:zcoords'),
        ]
    }


def _grid_tile_resolution_type():
    """Creates and returns instance of grid_tile_resolution_type class."""
    return {
        'type' : 'class',
        'name' : 'grid_tile_resolution_type',
        'base' : None,
        'is_abstract' : False,
        'doc' : 'Provides a description and set of named properties for the horizontal or vertical resolution.',
        'properties' : [
            ('description', 'str', '0.1', 'A description of the resolution.'),
            ('properties', 'grids.grid_property', '0.N', None),
        ],
        'decodings' : [
            ('description', '@description'),
            ('properties', 'child::cim:property'),
        ]
    }


def _vertical_coordinate_list():
    """Creates and returns instance of coordinate_list class."""
    return {
        'type' : 'class',
        'name' : 'vertical_coordinate_list',
        'base' : 'grids.coordinate_list',
        'is_abstract' : False,
        'doc' : 'There are some specific attributes that are associated with vertical coordinates.',
        'properties' : [
            ('properties', 'grids.grid_property', '0.N', None),
            ('type', 'str', '0.1', 'Specifies the length of the coordinate array. This should always be the final, as-built length of the array if the hasConstantOffset property is set to true and the compact notation (start coordinate plus offset) is used.'),
            ('form', 'str', '0.1', 'Units of measure used by the coordinates.'),
        ],
        'decodings' : [
            ('properties', 'child::cim:property'),
            ('type', '@coordinateType'),
            ('form', '@coordinateForm'),
        ]
    }
    

# Set of package classes.
classes = [
    _coordinate_list(),
    _grid_extent(),
    _grid_mosaic(),
    _grid_property(),
    _grid_spec(),
    _grid_tile(),
    _grid_tile_resolution_type(),
    _vertical_coordinate_list(),
]
