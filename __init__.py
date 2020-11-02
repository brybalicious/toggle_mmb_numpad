bl_info = {
    "name": "Toggle 'Emulate 3 Button Mouse' & 'Emulate Numpad'",
    "author": "brybalicious courtesy Robert Guetzkow",
    "version": (1, 0),
    "blender": (2, 90, 1),
    "location": "Edit > Operator Search",
    "description": "Operator for toggling the 'Emulate 3 Button Mouse' & 'Emulate Numpad' options",
    "warning": "",
    "wiki_url": "https://github.com/brybalicious/toggle_mmb_numpad/wiki",
    "category": "Preferences"}

import bpy
import rna_keymap_ui
from bpy.utils import register_class, unregister_class

# Surfacing the Operators
# They can now be looked up via their bl_label attribute with the search function on default hotkey F3

class PREFERENCES_OT_toggle_emulate_3_button_mouse(bpy.types.Operator):
    bl_idname = "preferences.toggle_emulate_3_button_mouse"
    bl_label = "Toggle 'Emulate 3 Button Mouse'"

    def execute(self, context):
        context.preferences.inputs.use_mouse_emulate_3_button = not context.preferences.inputs.use_mouse_emulate_3_button
        return {"FINISHED"}

class PREFERENCES_OT_toggle_emulate_numpad(bpy.types.Operator):
    bl_idname = "preferences.toggle_numpad"
    bl_label = "Toggle 'Emulate Numpad'"

    def execute(self, context):
        bpy.context.preferences.inputs.use_emulate_numpad = not bpy.context.preferences.inputs.use_emulate_numpad
        return {"FINISHED"}


# Keymap Code

# First, set up a dictionary of key mappings.

# "TEMPLATE": [{"label": "Human readable name of keymap in Blender Keymap UI",
#               "region_type": "WINDOW", //Default is WINDOW (optional)
#               "space_type", "EMPTY", //Default is EMPTY
#               "map_type": "KEYBOARD", //Device to be used (optional)
#               "keymap": "Window", //Name to be chosen from declared list of keymap names
#               "idname": ..., //Specific reference to operator from blender API
#               "type": "", //Key type identifier - choose a specific keyboard button or mouse button, etc...
#               "ctrl": False, //Combination keys for compound hotkeys (optional)
#               ...
#               "value": "PRESS"}, //Whether key will be held, pressed, etc...
#              {...}]

keys = {"MENU": [{"label": "Toggle Emulate 3 Button Mouse",
                  "region_type": "WINDOW",
                  "space_type", "EMPTY",
                  "map_type": "KEYBOARD",
                  "keymap": "Window",
                  "idname": "preferences.toggle_emulate_3_button_mouse",
                  "type": "QUOTE",
                  "ctrl": False,
                  "alt": False,
                  "shift": False,
                  "oskey": False,
                  "value": "PRESS"
                  },
                {"label": "Toggle Emulate Numpad",
                  "region_type": "WINDOW",
                  "space_type", "EMPTY",
                  "map_type": "KEYBOARD",
                  "keymap": "Window",
                  "idname": "preferences.toggle_numpad",
                  "type": "SEMI_COLON",
                  "ctrl": False,
                  "alt": False,
                  "shift": False,
                  "oskey": False,
                  "value": "PRESS"
                  }]}

# Define a function to get a list of key mappings, 'keylists'
def get_keys():
    keylists = []
    keylists.append(keys["MENU"])
    return keylists

# Define a function to register the key mappings templated in the dict as keymaps, using the constructor kc.keymaps.new()        
def register_keymaps(keylists):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    keymaps = []

    for keylist in keylists:
        for item in keylist:
            keymap = item.get("keymap")
            space_type = item.get("space_type", "EMPTY")
            region_type = item.get("region_type", "WINDOW")

            if keymap:
                km = kc.keymaps.new(name=keymap, space_type=space_type, region_type=region_type)
                # km = kc.keymaps.new(name=keymap, space_type=space_type)

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

# Define a function to unregister the keymaps
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