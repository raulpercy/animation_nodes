import bpy, random
from ... base_types.node import AnimationNode

class FloatClamp(bpy.types.Node, AnimationNode):
    bl_idname = "mn_FloatClamp"
    bl_label = "Clamp"
    isDetermined = True

    inputNames = {  "Value" : "value",
                    "Min" : "minValue",
                    "Max" : "maxValue" }

    outputNames = { "Value" : "value" }

    def create(self):
        self.inputs.new("mn_FloatSocket", "Value")
        self.inputs.new("mn_FloatSocket", "Min").value = 0.0
        self.inputs.new("mn_FloatSocket", "Max").value = 1.0
        self.outputs.new("mn_FloatSocket", "Value")

    def getExecutionCode(self):
        return "$value$ = min(max(%value%, %minValue%), %maxValue%)"