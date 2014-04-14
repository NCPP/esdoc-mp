"""
.. module:: esdoc_mp.generators.generator
   :platform: Unix, Windows
   :synopsis: Base class encapsulating functionality common to all cim code generators.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from abc import ABCMeta

from esdoc_mp.generators.generator_context import GeneratorContext
import esdoc_mp.generators.generator_utils as gu



class Generator(object):
    """Base class encapsulating functionality common to all code generators.

    """
    # Abstract Base Class module - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def execute(self, ontology, options):
        """Executes the code generator.

        :param ontology: Ontology being processed.
        :param options: Generation options.
        :type ontology: esdoc_mp.core.Ontology
        :type options: esdoc_mp.GeneratorOptions

        """
        # Instantiate context.
        ctx = GeneratorContext(ontology, options)
        
        # Emits generated code to file system.
        def emit_code(code):
            if code is not None:
                if not isinstance(code, list):
                    code = [code]
                for code, dir, file in code:
                    gu.write_file(gu.format_code(ctx, code), dir, file)

        # Notify start.
        self.on_start(ctx)

        # Raise parsing events and emit code accordingly.
        emit_code(self.on_ontology_parse(ctx))
        for pkg in ctx.ontology.packages:
            ctx.set_package(pkg)
            emit_code(self.on_package_parse(ctx))
        for cls in ctx.ontology.classes:
            ctx.set_class(cls)
            emit_code(self.on_class_parse(ctx))
        for enum in ctx.ontology.enums:
            ctx.set_enum(enum)
            emit_code(self.on_enum_parse(ctx))
            
        # Notify end.
        self.on_end(ctx)


    def on_start(self, ctx):
        """Event handler for the parsing start event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        pass


    def on_end(self, ctx):
        """Event handler for the parsing end event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        pass


    def on_ontology_parse(self, ctx):
        """Event handler for the ontology parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return None


    def on_package_parse(self, ctx):
        """Event handler for the package parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return None


    def on_class_parse(self, ctx):
        """Event handler for the class parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return None


    def on_enum_parse(self, ctx):
        """Event handler for the enum parse event.

        :param ctx: Generation context information.
        :type ctx: esdoc_mp.generators.generator.GeneratorContext

        """
        return None


