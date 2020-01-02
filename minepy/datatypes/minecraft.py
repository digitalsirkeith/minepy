""" Minecraft-specific datatypes
"""

from . import Type

class Chat(Type):
    def __init__(self):
        pass

class Identifier(Type):
    def __init__(self):
        pass

class VarInt(Type):
    def __init__(self, value: int):
        """
        TODO: create ByteArray from data
        """
        pass

class VarLong(Type):
    def __init__(self):
        pass

class EntityMetadata(Type):
    def __init__(self):
        pass

class Slot(Type):
    def __init__(self):
        pass

class NBTTag(Type):
    def __init__(self):
        pass

class Position(Type):
    def __init__(self):
        pass

class Angle(Type):
    def __init__(self):
        pass

class UUID(Type):
    def __init__(self):
        pass

class ByteArray(Type):
    def __init__(self, data):
        """
        TODO: create ByteArray from data
        """
        pass