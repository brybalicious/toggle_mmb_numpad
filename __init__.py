bl_info = {
    "name": "Toggle 'Emulate 3 Button Mouse' & 'Emulate Numpad'",
    "author": "brybalicious courtesy Robert Guetzkow",
    "version": (1, 0),
    "blender": (2, 90, 1),
    "location": "Edit > Operator Search",
    "description": "Operator for toggling the 'Emulate 3 Button Mouse' & 'Emulate Numpad' options",
    "warning": "",
    "wiki_url": "",
    "category": "Preferences"}

import bpy
import rna_keymap_ui
from bpy.utils import register_class, unregister_class

class PREFERENCES_OT_toggle_emulate_3_button_mouse(bpy.types.Operator):
    bl_idname = "preferences.toggle_emulate_3_button_mouse"
    bl_label = "Toggle 'Emulate 3 Button Mouse'"

    def execute(self, context):
        context.preferences.inputs.use_mouse_emulate_3_button = not context.preferences.inputs.use_mouse_emulate_3_button
        return {"FINISHED"}

class PREFERENCES_OT_toggle_emulate_numpad(bpy.types.Operator):
    bl_idname = "preferences.toggle_numpad"
    bl_label = "Toggle 'Numpad'"

    def execute(self, context):
        bpy.context.preferences.inputs.use_emulate_numpad = not bpy.context.preferences.inputs.use_emulate_numpad
        return {"FINISHED"}



keys = {"MENU": [{"label": "Toggle Emulate 3 Button Mouse",
                #   "region_type": "WINDOW",
                #   "map_type": "KEYBOARD",
                  "keymap": "Emulate MMB Toggle",
                  "idname": "preferences.toggle_emulate_3_button_mouse",
                  "type": "QUOTE",
                  "ctrl": False,
                  "alt": False,
                  "shift": False,
                  "oskey": False,
                  "value": "PRESS"
                  },
                {"label": "Toggle Numpad",
                #   "region_type": "WINDOW",
                #   "map_type": "KEYBOARD",
                  "keymap": "Emulate Numpad Toggle",
                  "idname": "preferences.toggle_numpad",
                  "type": "SEMI_COLON",
                  "ctrl": False,
                  "alt": False,
                  "shift": False,
                  "oskey": False,
                  "value": "PRESS"
                  }]}


def get_keys():
    keylists = []
    keylists.append(keys["MENU"])
    return keylists
        
def register_keymaps(keylists):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    keymaps = []

    for keylist in keylists:
        for item in keylist:
            keymap = item.get("keymap")
            space_type = item.get("space_type", "EMPTY")
            # region_type = item.get("region_type", "WINDOW")

            if keymap:
                # km = kc.keymaps.new(name=keymap, space_type=space_type, region_type=region_type)
                km = kc.keymaps.new(name=keymap, space_type=space_type)

                if km:
                    idname = item.get("idname")
                    type = item.get("type")
                    value = item.get("value")

                    shift = item.get("shift", False)
                    ctrl = item.get("ctrl", False)
                    alt = item.get("alt", False)
                    oskey = item.get("oskey", False)

                    kmi = km.keymap_items.new(idname, type, value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

                    if kmi:
                        properties = item.get("properties")

                        if properties:
                            for name, value in properties:
                                setattr(kmi.properties, name, value)

                        keymaps.append((km, kmi))
    return keymaps

def unregister_keymaps(keymaps):
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)


classes = (PREFERENCES_OT_toggle_emulate_3_button_mouse, PREFERENCES_OT_toggle_emulate_numpad)


def register():
    for cls in classes:
        register_class(cls)

    global keymaps
    keys = get_keys()
    keymaps = register_keymaps(keys)




def unregister():
    global keymaps
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)

    for cls in classes:
        unregister_class(cls)


# if __name__ == "__main__":
#     register()