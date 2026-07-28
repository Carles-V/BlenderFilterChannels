bl_info = {
    "name": "Filter Channels Addon",
    "blender": (4, 2, 0),
    "category": "Animation",
    "description": "Filter channels in Graph Editor for animation",
    "author": "Carles Vallbona",
    "version": (1, 0, 9),
    "support": "COMMUNITY",
}

import bpy

# -------------------------------------------------------------------
# Addon Preferences
# -------------------------------------------------------------------

# Define the Addon Preferences class
class FilterChannelsPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

# Quaternion and Compact mode from prefs
    quaternion_mode: bpy.props.BoolProperty(
        name="Quaternion Mode",
        description="Enable Quaternion Mode",
        default=False
    )

    compact_icons: bpy.props.BoolProperty(
        name="Compact Icons",
        description="Use emoji + special icon buttons",
        default=False
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "quaternion_mode", text="Quaternion Mode")
        layout.prop(self, "compact_icons", text="Compact Icons")


# -------------------------------------------------------------------
# Base Operator (Shift/Ctrl logic)
# -------------------------------------------------------------------

# Define a base operator class to handle Shift and Ctrl key detection
class BaseSelectChannelOperator(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        self.shift_pressed = event.shift
        self.ctrl_pressed = event.ctrl
        return self.execute(context)

    def select_channel(self, context, data_path, array_index):
        #Reset everything if there's no shift or ctrl
        if not self.shift_pressed and not self.ctrl_pressed:
            bpy.ops.graph.reset_channels()

        #Iterate over selected objects
        for obj in context.selected_objects:
            ad = obj.animation_data
            if not ad or not ad.action:
                continue
            action = ad.action

            #If action uses slots (Blender 4.4+)
            if hasattr(action, "slots"):
                for slot in action.slots:
                    for layer in action.layers:
                        for strip in layer.strips:
                            cb = strip.channelbag(slot)
                            if not cb:
                                continue

                            for fc in cb.fcurves:
                                match = (data_path in fc.data_path and
                                         fc.array_index == array_index)

                                if match:
                                    if self.ctrl_pressed:
                                        fc.select = False
                                    else:
                                        fc.select = True
                                elif not self.shift_pressed and not self.ctrl_pressed:
                                    fc.select = False

            #Fallback for classic actions without slots
            else:
                for fcurve in action.fcurves:
                    match = (data_path in fcurve.data_path and
                             fcurve.array_index == array_index)
                    if match:
                        if self.ctrl_pressed:
                            fcurve.select = False if match else fcurve.select
                        else:
                            fcurve.select = True if match else False
                    elif not self.shift_pressed and not self.ctrl_pressed:
                        fcurve.select = False

                        
        #Hide all non-selected curves
        bpy.ops.graph.hide(unselected=True)
        return {'FINISHED'}


# -------------------------------------------------------------------
# Operators (Location)
# -------------------------------------------------------------------

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


# -------------------------------------------------------------------
# Operators (Rotation)
# -------------------------------------------------------------------

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


# -------------------------------------------------------------------
# Operators (Quaternion)
# -------------------------------------------------------------------

# Define the operators for selecting quaternion channels
class SelectWQuaternionChannelOperator(BaseSelectChannelOperator):
    """Select W Quaternion channel for selected controls"""
    bl_idname = "graph.select_w_quaternion_channel"
    bl_label = "Select W Quaternion Channel"
    def execute(self, context):
        return self.select_channel(context, 'rotation_quaternion', 0)

class SelectXQuaternionChannelOperator(BaseSelectChannelOperator):
    """Select X Quaternion channel for selected controls"""
    bl_idname = "graph.select_x_quaternion_channel"
    bl_label = "Select X Quaternion Channel"
    def execute(self, context):
        return self.select_channel(context, 'rotation_quaternion', 1)

class SelectYQuaternionChannelOperator(BaseSelectChannelOperator):
    """Select Y Quaternion channel for selected controls"""
    bl_idname = "graph.select_y_quaternion_channel"
    bl_label = "Select Y Quaternion Channel"
    def execute(self, context):
        return self.select_channel(context, 'rotation_quaternion', 2)

class SelectZQuaternionChannelOperator(BaseSelectChannelOperator):
    """Select Z Quaternion channel for selected controls"""
    bl_idname = "graph.select_z_quaternion_channel"
    bl_label = "Select Z Quaternion Channel"
    def execute(self, context):
        return self.select_channel(context, 'rotation_quaternion', 3)


# -------------------------------------------------------------------
# Operators (Scale)
# -------------------------------------------------------------------

# Define the operators for selecting scale channels
class SelectXScaleChannelOperator(BaseSelectChannelOperator):
    """Select X Scale channel for selected controls"""
    bl_idname = "graph.select_x_scale_channel"
    bl_label = "Select X Scale Channel"
    def execute(self, context):
        return self.select_channel(context, 'scale', 0)

class SelectYScaleChannelOperator(BaseSelectChannelOperator):
    """Select X Scale channel for selected controls"""
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


# -------------------------------------------------------------------
# Utility Operators
# -------------------------------------------------------------------

# Define the operator to hide all non-selected channels
class HideRestOperator(bpy.types.Operator):
    bl_idname = "graph.hide_rest_channels"
    bl_label = "Hide Rest"
    def execute(self, context):
        bpy.ops.graph.hide(unselected=True)
#      bpy.ops.graph.select_all(action='DESELECT')
        return {'FINISHED'}
        
# Define the operator to reset and unhide all channels
class ResetChannelsOperator(bpy.types.Operator):
    bl_idname = "graph.reset_channels"
    bl_label = "Reset Channels"
    def execute(self, context):
        if bpy.ops.graph.reveal.poll():
            bpy.ops.graph.reveal()
        else:
            self.report({'INFO'}, "No hidden F-Curves to reveal.")

        if bpy.ops.graph.select_all.poll():
            bpy.ops.graph.select_all(action='DESELECT')
        else:
            self.report({'INFO'}, "No F-Curves to deselect.")
        return {'FINISHED'}


# Define the operator to unselect all selected channels
class UnselectChannelsOperator(bpy.types.Operator):
    bl_idname = "graph.unselect_channels"
    bl_label = "Unselect Channels"  
    def execute(self, context):
        if bpy.ops.graph.select_all.poll():
            bpy.ops.graph.select_all(action='DESELECT')
        else:
            self.report({'INFO'}, "No visible F-Curves to deselect.")
        return {'FINISHED'}



# -------------------------------------------------------------------
# Panel
# -------------------------------------------------------------------

# Define the panel
class GraphEditorPanel(bpy.types.Panel):
    bl_label = "Filter Channels"
    bl_idname = "GRAPH_EDITOR_PT_custom_panel"
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Filter Channels'

    def draw(self, context):
        layout = self.layout
        prefs = context.preferences.addons[__name__].preferences
        use_compact = prefs.compact_icons

        col = layout.column(align=True)
        col.label(text="Filter Selections")
        col.separator()

        # -------------------------
        # Location
        # -------------------------
        if not use_compact:
            col.label(text="Location")

        row = col.row(align=True)
        if use_compact:
            row.operator("graph.select_x_location_channel", text="X ↔️", icon="KEYTYPE_EXTREME_VEC")
            row.operator("graph.select_y_location_channel", text="Y ↔️", icon="KEYTYPE_JITTER_VEC")
            row.operator("graph.select_z_location_channel", text="Z ↔️", icon="KEYTYPE_BREAKDOWN_VEC")
        else:
            row.operator("graph.select_x_location_channel", text="X")
            row.operator("graph.select_y_location_channel", text="Y")
            row.operator("graph.select_z_location_channel", text="Z")

        # -------------------------
        # Rotation
        # -------------------------
        col.separator()
        if not use_compact:
            col.label(text="Rotation")

        row = col.row(align=True)
        if use_compact:
            row.operator("graph.select_x_rotation_channel", text="X 🌐", icon="KEYTYPE_EXTREME_VEC")
            row.operator("graph.select_y_rotation_channel", text="Y 🌐", icon="KEYTYPE_JITTER_VEC")
            row.operator("graph.select_z_rotation_channel", text="Z 🌐", icon="KEYTYPE_BREAKDOWN_VEC")
        else:
            row.operator("graph.select_x_rotation_channel", text="X")
            row.operator("graph.select_y_rotation_channel", text="Y")
            row.operator("graph.select_z_rotation_channel", text="Z")

        # -------------------------
        # Quaternion (If mode is selected)
        # -------------------------
        if prefs.quaternion_mode:
            col.separator()
            if not use_compact:
                col.label(text="Quaternion Rotation")

            row = col.row(align=True)
            if use_compact:
                row.operator("graph.select_w_quaternion_channel", text="W 🔘", icon='KEYTYPE_MOVING_HOLD_VEC')
                row.operator("graph.select_x_quaternion_channel", text="X 🔘", icon='KEYTYPE_EXTREME_VEC')
                row.operator("graph.select_y_quaternion_channel", text="Y 🔘", icon='KEYTYPE_JITTER_VEC')
                row.operator("graph.select_z_quaternion_channel", text="Z 🔘", icon='KEYTYPE_BREAKDOWN_VEC')
            else:
                row.operator("graph.select_w_quaternion_channel", text="W")
                row.operator("graph.select_x_quaternion_channel", text="X")
                row.operator("graph.select_y_quaternion_channel", text="Y")
                row.operator("graph.select_z_quaternion_channel", text="Z")

        # -------------------------
        # Scale
        # -------------------------
        col.separator()
        if not use_compact:
            col.label(text="Scale")

        row = col.row(align=True)
        if use_compact:
            row.operator("graph.select_x_scale_channel", text="X 📐", icon="KEYTYPE_EXTREME_VEC")
            row.operator("graph.select_y_scale_channel", text="Y 📐", icon="KEYTYPE_JITTER_VEC")
            row.operator("graph.select_z_scale_channel", text="Z 📐", icon="KEYTYPE_BREAKDOWN_VEC")
        else:
            row.operator("graph.select_x_scale_channel", text="X")
            row.operator("graph.select_y_scale_channel", text="Y")
            row.operator("graph.select_z_scale_channel", text="Z")

        # -------------------------
        # Filter / Reset / Unselect
        # -------------------------
        col.separator()

        if not use_compact:
            col.label(text="Filter")
            col.operator("graph.hide_rest_channels", text="Hide Rest")
            col.operator("graph.reset_channels", text="Reset Channels")
            col.operator("graph.unselect_channels", text="Unselect Channels")

        else:
            row = col.row(align=True)
            row.operator("graph.hide_rest_channels", text="", icon='HIDE_ON')
            row.operator("graph.reset_channels", text="", icon='FILE_REFRESH')
            row.operator("graph.unselect_channels", text="", icon='CANCEL')


# -------------------------------------------------------------------
# Registration
# -------------------------------------------------------------------

# Register and unregister classes
classes = (
    FilterChannelsPreferences,
    SelectXLocationChannelOperator, SelectYLocationChannelOperator, SelectZLocationChannelOperator,
    SelectXRotationChannelOperator, SelectYRotationChannelOperator, SelectZRotationChannelOperator,
    SelectWQuaternionChannelOperator, SelectXQuaternionChannelOperator,
    SelectYQuaternionChannelOperator, SelectZQuaternionChannelOperator,
    SelectXScaleChannelOperator, SelectYScaleChannelOperator, SelectZScaleChannelOperator,
    HideRestOperator, ResetChannelsOperator, UnselectChannelsOperator,
    GraphEditorPanel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
