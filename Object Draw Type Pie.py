
bl_info = {
    "name": "Object Draw Type Pie",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 76, 0),
    "location": "View3D > Alt + W",
    "description": "Adds a pie menu for changing the selected objects draw type between 'Solid' and 'Wire'",
    "category": "User Interface",
    }
    


import bpy
from bpy.types import Menu



class ChangeObjectDrawType(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "view3d.change_object_draw_type"
    bl_label = "Change Draw Type"
    
    draw_type = bpy.props.StringProperty()

    
    def execute(self, context):
        
        if(len(context.selected_objects) > 0):
                
            for object in bpy.context.selected_objects:
                    
                object.draw_type = self.draw_type
        
        else:
            
            self.report({"ERROR"}, "No objects selected")
        
        return {'FINISHED'}
    


class VIEW3D_PIE_OBJECT_DRAW_TYPE(Menu):
    bl_label = "Object Draw Type"
    bl_idname = "object_mode.object_draw_type"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
                    
        pie.operator("view3d.change_object_draw_type", text="Solid", icon="SOLID").draw_type = "SOLID"
        pie.operator("view3d.change_object_draw_type", text="Wire", icon="WIRE").draw_type = "WIRE" 


                                           
def register():
    bpy.utils.register_module(__name__)    
        
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    
    kmicarToolsMenu = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', alt=True)
    kmicarToolsMenu.properties.name = 'object_mode.object_draw_type'
    
    

def unregister():
    bpy.utils.unregister_module(__name__)        
    
    km.keymap_items.remove(kmiToggleModifiers)
    


if __name__ == "__main__":
    register()


#register()          
#bpy.ops.wm.call_menu_pie(name="object_mode.object_draw_type")
      