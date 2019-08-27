import bpy


class PrintOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.print_operator"
    bl_label = "Print operator test"

    def execute(self, context):
        scn = context.scene.Viewport
        state = scn.lock_activate

        print('Debug : {}'.format(state))

        scn.lock_activate = not state
        print('Value Update : {}'.format(state))

        return {'FINISHED'}
