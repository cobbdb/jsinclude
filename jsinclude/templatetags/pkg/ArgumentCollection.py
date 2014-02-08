from .VariableArgument import VariableArgument
from .StaticArgument import StaticArgument

def ArgumentCollection(arguments, context):
    data = {}
    for key in arguments:
        try:
            # Template variables.
            arg = VariableArgument(key, context)
        except KeyError:
            # Static values are name=value format.
            arg = StaticArgument(key)
        data.update(arg)
    return data
