import bpy


class PrintOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.print_operator"
    bl_label = "Print operator test"

    def execute(self, context):
        print('Call Me !')
        return {'FINISHED'}
