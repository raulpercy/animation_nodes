import bpy
from .. data_structures import EdgeIndicesList
from .. base_types import AnimationNodeSocket, CythonListSocket

class EdgeIndicesSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_EdgeIndicesSocket"
    bl_label = "Edge Indices Socket"
    dataType = "Edge Indices"
    allowedInputTypes = ["Edge Indices"]
    drawColor = (0.4, 0.6, 0.6, 1)
    comparable = True
    storable = True

    @classmethod
    def getDefaultValue(cls):
        return (0, 1)

    @classmethod
    def getDefaultValueCode(cls):
        return "(0, 1)"

    @classmethod
    def getCopyExpression(cls):
        return "value[:]"

    @classmethod
    def correctValue(cls, value):
        if isEdge(value): return value, 0
        else: return cls.getDefaultValue(), 2


class EdgeIndicesListSocket(bpy.types.NodeSocket, CythonListSocket, AnimationNodeSocket):
    bl_idname = "an_EdgeIndicesListSocket"
    bl_label = "Edge Indices List Socket"
    dataType = "Edge Indices List"
    baseDataType = "Edge Indices"
    allowedInputTypes = ["Edge Indices List"]
    drawColor = (0.4, 0.6, 0.6, 0.5)
    storable = True
    comparable = False
    listClass = EdgeIndicesList