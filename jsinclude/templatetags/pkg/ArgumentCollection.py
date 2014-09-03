from .VariableArgument import VariableArgument
from .StaticArgument import StaticArgument

def ArgumentCollection(context, arguments):
    """Dictionary of tag arguments by name: value.
    """
    collection = {}
    for key in arguments:
        try:
            # Look into template context for existing variable.
            arg = VariableArgument(key, context)
        except KeyError:
            # Static values are name=value format.
            arg = StaticArgument(key)
        collection.update(arg)
    return collection
