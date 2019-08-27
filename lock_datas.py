import bpy


# def update_grid(self, context):
#     bpy.ops.view.grid_control()
#     return


class ViewportControl(bpy.types.PropertyGroup):
    lock_activate: bpy.props.BoolProperty(
        name="Lock Viewport",
        description="Simple boolean to lock/unlock the viewport",
        default=True,
        # update=update_grid
    )
