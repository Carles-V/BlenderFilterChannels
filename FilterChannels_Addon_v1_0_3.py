bl_info = {
    "name": "Filter Channels Addon",
    "blender": (4, 2, 0),
    "category": "Animation",
    "description": "Filter channels in Graph Editor for animation",
    "author": "Carles Vallbona",
    "version": (1, 0, 3),
    "support": "COMMUNITY",
}

import bpy

# Define a base operator class to handle Shift and Ctrl key detection
class BaseSelectChannelOperator(bpy.types.Operator):
    """Base class to handle Shift and Ctrl key detection"""
    bl_options = {'REGISTER', 'UNDO'}

    def __init__(self):
        self.shift_pressed = False
        self.ctrl_pressed = False

    def invoke(self, context, event):
        self.shift_pressed = event.shift
        self.ctrl_pressed = event.ctrl
        return self.execute(context)

    def select_channel(self, context, data_path, array_index):
        if not self.shift_pressed and not self.ctrl_pressed:
            bpy.ops.graph.reset_channels()

        for obj in context.selected_objects:
            if obj.animation_data:
                action = obj.animation_data.action
                if action:
                    for fcurve in action.fcurves:
                        if data_path in fcurve.data_path and fcurve.array_index == array_index:
                            if self.ctrl_pressed:
                                fcurve.select = False  # Deselect if Ctrl is pressed
                            else:
                                fcurve.select = True  # Select if Shift is pressed or neither is pressed

        bpy.ops.graph.hide_rest_channels()  # Hide the rest
        return {'FINISHED'}

# Define the operators for selecting location channels
class SelectXLocationChannelOperator(BaseSelectChannelOperator):
    """Select X Location channel for selected controls"""
    bl_idname = "graph.select_x_location_channel"
    bl_label = "Select X Location Channel"

    def execute(self, context):
        return self.select_channel(context, 'location', 0)

class SelectYLocationChannelOperator(BaseSelectChannelOperator):
    """Select Y Location channel for selected controls"""
    bl_idname = "graph.select_y_location_channel"
    bl_label = "Select Y Location Channel"

    def execute(self, context):
        return self.select_channel(context, 'location', 1)

class SelectZLocationChannelOperator(BaseSelectChannelOperator):
    """Select Z Location channel for selected controls"""
    bl_idname = "graph.select_z_location_channel"
    bl_label = "Select Z Location Channel"

    def execute(self, context):
        return self.select_channel(context, 'location', 2)

# Define the operators for selecting rotation channels
class SelectXRotationChannelOperator(BaseSelectChannelOperator):
    """Select X Rotation channel for selected controls"""
    bl_idname = "graph.select_x_rotation_channel"
    bl_label = "Select X Rotation Channel"

    def execute(self, context):
        return self.select_channel(context, 'rotation_euler', 0)

class SelectYRotationChannelOperator(BaseSelectChannelOperator):
    """Select Y Rotation channel for selected controls"""
    bl_idname = "graph.select_y_rotation_channel"
    bl_label = "Select Y Rotation Channel"

    def execute(self, context):
        return self.select_channel(context, 'rotation_euler', 1)

class SelectZRotationChannelOperator(BaseSelectChannelOperator):
    """Select Z Rotation channel for selected controls"""
    bl_idname = "graph.select_z_rotation_channel"
    bl_label = "Select Z Rotation Channel"

    def execute(self, context):
        return self.select_channel(context, 'rotation_euler', 2)

# Define the operators for selecting scale channels
class SelectXScaleChannelOperator(BaseSelectChannelOperator):
    """Select X Scale channel for selected controls"""
    bl_idname = "graph.select_x_scale_channel"
    bl_label = "Select X Scale Channel"

    def execute(self, context):
        return self.select_channel(context, 'scale', 0)

class SelectYScaleChannelOperator(BaseSelectChannelOperator):
    """Select Y Scale channel for selected controls"""
    bl_idname = "graph.select_y_scale_channel"
    bl_label = "Select Y Scale Channel"

    def execute(self, context):
        return self.select_channel(context, 'scale', 1)

class SelectZScaleChannelOperator(BaseSelectChannelOperator):
    """Select Z Scale channel for selected controls"""
    bl_idname = "graph.select_z_scale_channel"
    bl_label = "Select Z Scale Channel"

    def execute(self, context):
        return self.select_channel(context, 'scale', 2)

# Define the operator to hide all non-selected channels
class HideRestOperator(bpy.types.Operator):
    """Hide all non-selected channels"""
    bl_idname = "graph.hide_rest_channels"
    bl_label = "Hide Rest"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.animation_data:
                action = obj.animation_data.action
                if action:
                    for fcurve in action.fcurves:
                        if not fcurve.select:
                            fcurve.hide = True
                        else:
                            fcurve.hide = False  # Ensure selected channels are not hidden
        return {'FINISHED'}

# Define the operator to reset and unhide all channels
class ResetChannelsOperator(bpy.types.Operator):
    """Reset and unhide all channels"""
    bl_idname = "graph.reset_channels"
    bl_label = "Reset Channels"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.animation_data:
                action = obj.animation_data.action
                if action:
                    for fcurve in action.fcurves:
                        fcurve.hide = False
                        fcurve.select = False  # Unselect all channels
        return {'FINISHED'}

# Define the operator to unselect all selected channels
class UnselectChannelsOperator(bpy.types.Operator):
    """Unselect all selected channels"""
    bl_idname = "graph.unselect_channels"
    bl_label = "Unselect Channels"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.animation_data:
                action = obj.animation_data.action
                if action:
                    for fcurve in action.fcurves:
                        fcurve.select = False
        return {'FINISHED'}

# Define the panel
class GraphEditorPanel(bpy.types.Panel):
    bl_label = "Filter Channels"
    bl_idname = "GRAPH_EDITOR_PT_custom_panel"
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Filter Channels'

    def draw(self, context):
        layout = self.layout

        # Filter Selections section
        col = layout.column(align=True)
        col.label(text="Filter Selections")
        col.separator()

        # Location section
        col.label(text="Location")
        row = col.row(align=True)
        row.operator("graph.select_x_location_channel", text="X")
        row.operator("graph.select_y_location_channel", text="Y")
        row.operator("graph.select_z_location_channel", text="Z")

        # Rotation section
        col.separator()
        col.label(text="Rotation")
        row = col.row(align=True)
        row.operator("graph.select_x_rotation_channel", text="X")
        row.operator("graph.select_y_rotation_channel", text="Y")
        row.operator("graph.select_z_rotation_channel", text="Z")

        # Scale section
        col.separator()
        col.label(text="Scale")
        row = col.row(align=True)
        row.operator("graph.select_x_scale_channel", text="X")
        row.operator("graph.select_y_scale_channel", text="Y")
        row.operator("graph.select_z_scale_channel", text="Z")

        # Filter section
        col.separator()
        col.label(text="Filter")
        col.operator("graph.hide_rest_channels", text="Hide Rest")

        # Reset Channels section
        col.operator("graph.reset_channels", text="Reset Channels")
        col.operator("graph.unselect_channels", text="Unselect Channels", icon='NONE')  # No icon

# Register and unregister classes
def register():
    bpy.utils.register_class(SelectXLocationChannelOperator)
    bpy.utils.register_class(SelectYLocationChannelOperator)
    bpy.utils.register_class(SelectZLocationChannelOperator)
    bpy.utils.register_class(SelectXRotationChannelOperator)
    bpy.utils.register_class(SelectYRotationChannelOperator)
    bpy.utils.register_class(SelectZRotationChannelOperator)
    bpy.utils.register_class(SelectXScaleChannelOperator)
    bpy.utils.register_class(SelectYScaleChannelOperator)
    bpy.utils.register_class(SelectZScaleChannelOperator)
    bpy.utils.register_class(HideRestOperator)
    bpy.utils.register_class(ResetChannelsOperator)
    bpy.utils.register_class(UnselectChannelsOperator)
    bpy.utils.register_class(GraphEditorPanel)

def unregister():
    bpy.utils.unregister_class(SelectXLocationChannelOperator)
    bpy.utils.unregister_class(SelectYLocationChannelOperator)
    bpy.utils.unregister_class(SelectZLocationChannelOperator)
    bpy.utils.unregister_class(SelectXRotationChannelOperator)
    bpy.utils.unregister_class(SelectYRotationChannelOperator)
    bpy.utils.unregister_class(SelectZRotationChannelOperator)
    bpy.utils.unregister_class(SelectXScaleChannelOperator)
    bpy.utils.unregister_class(SelectYScaleChannelOperator)
    bpy.utils.unregister_class(SelectZScaleChannelOperator)
    bpy.utils.unregister_class(HideRestOperator)
    bpy.utils.unregister_class(ResetChannelsOperator)
    bpy.utils.unregister_class(UnselectChannelsOperator)
    bpy.utils.unregister_class(GraphEditorPanel)

if __name__ == "__main__":
    register()