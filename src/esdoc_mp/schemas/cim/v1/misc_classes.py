"""
CIM v1 miscellaneous package classes.
"""

def _document_set():
    """Creates and returns instance of document_set class."""
    return {
        'type' : 'class',
        'name' : 'document_set',
        'base' : None,
        'is_abstract' : False,
        'is_entity' : True,
        'doc' : 'Encapsulates a set of documents.',
        'properties' : [
            ('meta', 'shared.doc_meta_info', '1.1', None),
            ('data', 'data.dataObject', '0.N', 'Associated input/output data.'),
            ('ensembles', 'activity.ensemble', '0.N', 'Associated ensemble runs.'),
            ('experiment', 'activity.numerical_experiment', '0.1', 'Associated numerical experiment.'),
            ('grids', 'grids.grid_spec', '0.N', 'Associated grid-spec.'),
            ('model', 'software.model_component', '0.1', 'Associated model component.'),
            ('platform', 'shared.platform', '0.1', 'Associated simulation execution platform.'),
            ('simulation', 'activity.simulation_run', '0.1', 'Associated simulation run.'),
        ],
        'decodings' : [
            ('data', 'child::cim:dataObject'),
            ('ensembles', 'child::cim:ensemble'),
            ('experiment', 'child::cim:numericalExperiment'),
            ('model', 'child::cim:modelComponent'),
            ('grids', 'child::cim:gridSpec'),
            ('platform', 'child::cim:platform'),
            ('simulation', 'child::cim:simulationRun'),
        ]
    }


# Set of package classes.
classes = [
    _document_set(),
]
