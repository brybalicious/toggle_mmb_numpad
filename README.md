# Blender Addon: Toggle Emulate MMB & Numpad

<!-- # toggle_emulate_mmb_numpad -->
This addon makes it simple and easy to set up Blender for e.g. a lightweight portable setup. Perfect with a laptop 2-in-1 and stylus pen, where Numpad and a Mouse with or without Middle Mouse Button are lacking entirely.


- ";" toggles the number keys to become Numpad Keys for viewport orientation and view snapping
- "' or "" toggles Middle Mouse Button emulation, so the stylus can be used with Alt (or one of its buttons mapped to Alt) for orbiting and 3D viewport navigation

- Highly recommend downloading a stylus programming application like ['HP Pen Control'](https://www.microsoft.com/store/productId/9PJ3VGVQ4NMP) to give easy, though minimal control over programming of stylus buttons. Mapping one to right-click and another to 'Alt' frees up the left hand for hotkeys, while the stylus can be used for drawing and navigation

- Especially useful for stylus operation with QuickTools ([QuickShape](https://gumroad.com/jamajurabaev#tOWta), [QuickDeform](https://gumroad.com/alksndr), [QuickCurve](https://gumroad.com/jamajurabaev#EmBrX)) on a lightweight setup

- Saves figuring out how to add the hidden toggle operators to the keymap, or going into preferences to toggle them

- Far easier than setting up AutoHotkey for stylus buttons. The keymap seems fairly unused in Blender at present

- Soon to add visual indicator of toggle status so you can *free your mind* for imagination

-------------------------------------------------------------------------

##Notes on keymaps:
<!-- https://docs.blender.org/api/current/bpy.types.KeyMap.html?highlight=key%20name#bpy.types.KeyMap.name -->
<!-- https://docs.blender.org/api/current/bpy.types.KeyMaps.html#bpy.types.KeyMaps.new -->
<!-- https://docs.blender.org/api/current/bpy.types.KeyMapItem.html?highlight=key%20name#bpy.types.KeyMapItem.name -->
<!-- https://devtalk.blender.org/t/official-keymap-example-does-not-work/9032/6 -->

For Keymaps to show in its corresponding location in the [Edit >> Preferences >> Keymap] ui, keymap name must be one of the following 224 strings (no number), surrounded by quotes:


0    Window
1    Screen
2    Screen Editing
3    User Interface
4    View2D
5    Region Context Menu
6    View2D Buttons List
7    Frames
8    Property Editor
9    Outliner
10    Markers
11    Time Scrub
12    Animation
13    Dopesheet
14    Dopesheet Generic
15    3D View Generic
16    Grease Pencil
17    Grease Pencil Stroke Edit Mode
18    Grease Pencil Stroke Paint Mode
19    Grease Pencil Stroke Paint (Draw brush)
20    Grease Pencil Stroke Paint (Erase)
21    Grease Pencil Stroke Paint (Fill)
22    Grease Pencil Stroke Paint (Tint)
23    Grease Pencil Stroke Sculpt Mode
24    Grease Pencil Stroke Vertex Mode
25    Grease Pencil Stroke Vertex (Draw)
26    Grease Pencil Stroke Vertex (Blur)
27    Grease Pencil Stroke Vertex (Average)
28    Grease Pencil Stroke Vertex (Smear)
29    Grease Pencil Stroke Vertex (Replace)
30    Grease Pencil Stroke Sculpt (Smooth)
31    Grease Pencil Stroke Sculpt (Thickness)
32    Grease Pencil Stroke Sculpt (Strength)
33    Grease Pencil Stroke Sculpt (Grab)
34    Grease Pencil Stroke Sculpt (Push)
35    Grease Pencil Stroke Sculpt (Twist)
36    Grease Pencil Stroke Sculpt (Pinch)
37    Grease Pencil Stroke Sculpt (Randomize)
38    Grease Pencil Stroke Sculpt (Clone)
39    Grease Pencil Stroke Weight Mode
40    Grease Pencil Stroke Weight (Draw)
41    Paint Face Mask (Weight, Vertex, Texture)
42    Paint Vertex Selection (Weight, Vertex)
43    Weight Paint
44    Vertex Paint
45    Pose
46    Object Mode
47    Paint Curve
48    Curve
49    Image Paint
50    Sculpt
51    Mesh
52    Armature
53    Metaball
54    Lattice
55    Particle
56    Font
57    Object Non-modal
58    3D View
59    Image Editor Tool: Uv, Tweak
60    Image Editor Tool: Uv, Select Box
61    Image Editor Tool: Uv, Select Circle
62    Image Editor Tool: Uv, Select Lasso
63    Image Editor Tool: Uv, Cursor
64    Image Editor Tool: Uv, Rip Region
65    3D View Tool: Pose, Breakdowner
66    3D View Tool: Pose, Push
67    3D View Tool: Pose, Relax
68    3D View Tool: Edit Armature, Roll
69    3D View Tool: Edit Armature, Bone Size
70    3D View Tool: Edit Armature, Bone Envelope
71    3D View Tool: Edit Armature, Extrude
72    3D View Tool: Edit Armature, Extrude to Cursor
73    3D View Tool: Edit Mesh, Extrude Region
74    3D View Tool: Edit Mesh, Extrude Manifold
75    3D View Tool: Edit Mesh, Extrude Along Normals
76    3D View Tool: Edit Mesh, Extrude Individual
77    3D View Tool: Edit Mesh, Extrude to Cursor
78    3D View Tool: Edit Mesh, Inset Faces
79    3D View Tool: Edit Mesh, Bevel
80    3D View Tool: Edit Mesh, Loop Cut
81    3D View Tool: Edit Mesh, Offset Edge Loop Cut
82    3D View Tool: Edit Mesh, Knife
83    3D View Tool: Edit Mesh, Bisect
84    3D View Tool: Edit Mesh, Poly Build
85    3D View Tool: Edit Mesh, Spin
86    3D View Tool: Edit Mesh, Spin Duplicates
87    3D View Tool: Edit Mesh, Smooth
88    3D View Tool: Edit Mesh, Randomize
89    3D View Tool: Edit Mesh, Edge Slide
90    3D View Tool: Edit Mesh, Vertex Slide
91    3D View Tool: Edit Mesh, Shrink/Fatten
92    3D View Tool: Edit Mesh, Push/Pull
93    3D View Tool: Edit Mesh, To Sphere
94    3D View Tool: Edit Mesh, Rip Region
95    3D View Tool: Edit Mesh, Rip Edge
96    3D View Tool: Edit Curve, Draw
97    3D View Tool: Edit Curve, Extrude
98    3D View Tool: Edit Curve, Extrude to Cursor
99    3D View Tool: Edit Curve, Radius
100    3D View Tool: Edit Curve, Tilt
101    3D View Tool: Edit Curve, Randomize
102    3D View Tool: Sculpt, Box Mask
103    3D View Tool: Sculpt, Lasso Mask
104    3D View Tool: Sculpt, Box Hide
105    3D View Tool: Sculpt, Mesh Filter
106    3D View Tool: Sculpt, Cloth Filter
107    3D View Tool: Sculpt, Color Filter
108    3D View Tool: Sculpt, Mask By Color
109    3D View Tool: Paint Weight, Gradient
110    3D View Tool: Paint Weight, Sample Weight
111    3D View Tool: Paint Weight, Sample Vertex Group
112    3D View Tool: Paint Gpencil, Cutter
113    3D View Tool: Paint Gpencil, Eyedropper
114    3D View Tool: Paint Gpencil, Line
115    3D View Tool: Paint Gpencil, Polyline
116    3D View Tool: Paint Gpencil, Arc
117    3D View Tool: Paint Gpencil, Curve
118    3D View Tool: Paint Gpencil, Box
119    3D View Tool: Paint Gpencil, Circle
120    3D View Tool: Edit Gpencil, Tweak
121    3D View Tool: Edit Gpencil, Select Box
122    3D View Tool: Edit Gpencil, Select Circle
123    3D View Tool: Edit Gpencil, Select Lasso
124    3D View Tool: Edit Gpencil, Extrude
125    3D View Tool: Edit Gpencil, Radius
126    3D View Tool: Edit Gpencil, Bend
127    3D View Tool: Edit Gpencil, Shear
128    3D View Tool: Edit Gpencil, To Sphere
129    3D View Tool: Edit Gpencil, Transform Fill
130    3D View Tool: Edit Mesh, Make Line
131    3D View Tool: Hops
132    3D View Tool: Hardflow
133    3D View Tool: BoxCutter
134    3D View Tool: Cad Transform
135    Gizmos
136    Generic Gizmo
137    Generic Gizmo Maybe Drag
138    Generic Gizmo Tweak Modal Map
139    View3D Gesture Circle
140    Gesture Box
141    Gesture Zoom Border
142    Gesture Straight Line
143    Header
144    Standard Modal Map
145    Animation Channels
146    Knife Tool Modal Map
147    Custom Normals Modal Map
148    Bevel Modal Map
149    UV Editor
150    Paint Stroke Modal
151    Mask Editing
152    Eyedropper Modal Map
153    Eyedropper ColorRamp PointSampling Map
154    Transform Modal Map
155    View3D Fly Modal
156    View3D Walk Modal
157    View3D Rotate Modal
158    View3D Move Modal
159    View3D Zoom Modal
160    View3D Dolly Modal
161    View3D Placement Modal Map
162    Graph Editor Generic
163    Graph Editor
164    Image Generic
165    Image
166    Node Generic
167    Node Editor
168    Info
169    File Browser
170    File Browser Main
171    File Browser Buttons
172    NLA Generic
173    NLA Channels
174    NLA Editor
175    Text Generic
176    Text
177    SequencerCommon
178    Sequencer
179    SequencerPreview
180    Console
181    Clip
182    Clip Editor
183    Clip Graph Editor
184    Clip Dopesheet Editor
185    Clip Time Scrub
186    Generic Gizmo Drag
187    Generic Gizmo Click Drag
188    Generic Gizmo Select
189    Toolbar Popup
190    Generic Tool: Annotate
191    Generic Tool: Annotate Line
192    Generic Tool: Annotate Polygon
193    Generic Tool: Annotate Eraser
194    Image Editor Tool: Sample
195    Image Editor Tool: Uv, Sculpt Stroke
196    Image Editor Tool: Uv, Move
197    Image Editor Tool: Uv, Rotate
198    Image Editor Tool: Uv, Scale
199    Node Tool: Tweak
200    Node Tool: Select Box
201    Node Tool: Select Lasso
202    Node Tool: Select Circle
203    Node Tool: Links Cut
204    3D View Tool: Cursor
205    3D View Tool: Tweak
206    3D View Tool: Select Box
207    3D View Tool: Select Circle
208    3D View Tool: Select Lasso
209    3D View Tool: Transform
210    3D View Tool: Move
211    3D View Tool: Rotate
212    3D View Tool: Scale
213    3D View Tool: Shear
214    3D View Tool: Measure
215    3D View Tool: Object, Add Primitive
216    3D View Tool: Sculpt Gpencil, Tweak
217    3D View Tool: Sculpt Gpencil, Select Box
218    3D View Tool: Sculpt Gpencil, Select Circle
219    3D View Tool: Sculpt Gpencil, Select Lasso
220    Sequencer Tool: Select
221    Sequencer Tool: Select Box
222    Sequencer Tool: Blade
223    Sequencer Tool: Sample

- The above References are spat out by blender scripting console when running:
    ```import bpy
    for i, km in enumerate(bpy.context.window_manager.keyconfigs.default.keymaps):
        print(f"{i}\t{km.name}")```

- Note, these refer to what context one must be in, for key presses to actually activate. If, for example "User Interface", the hotkey will only activate anything when the cursor is hovering over a user interface. If, for example "Window", the hotkey will activate anywhere within the Blender application window


###Region Types
region_type must be one of the following references:


[‘WINDOW’, ‘HEADER’, ‘CHANNELS’, ‘TEMPORARY’, ‘UI’, ‘TOOLS’, ‘TOOL_PROPS’, ‘PREVIEW’, ‘HUD’, ‘NAVIGATION_BAR’, ‘EXECUTE’, ‘FOOTER’, ‘TOOL_HEADER’], default ‘WINDOW’, (readonly)



###Space Types
space_type must be one of the following, where the left-side CAPS is the Reference:


    EMPTY Empty.

    VIEW_3D 3D Viewport, Manipulate objects in a 3D environment.

    IMAGE_EDITOR UV/Image Editor, View and edit images and UV Maps.

    NODE_EDITOR Node Editor, Editor for node-based shading and compositing tools.

    SEQUENCE_EDITOR Video Sequencer, Video editing tools.

    CLIP_EDITOR Movie Clip Editor, Motion tracking tools.

    DOPESHEET_EDITOR Dope Sheet, Adjust timing of keyframes.

    GRAPH_EDITOR Graph Editor, Edit drivers and keyframe interpolation.

    NLA_EDITOR Nonlinear Animation, Combine and layer Actions.

    TEXT_EDITOR Text Editor, Edit scripts and in-file documentation.

    CONSOLE Python Console, Interactive programmatic console for advanced editing and script development.

    INFO Info, Log of operations, warnings and error messages.

    TOPBAR Top Bar, Global bar at the top of the screen for global per-window settings.

    STATUSBAR Status Bar, Global bar at the bottom of the screen for general status information.

    OUTLINER Outliner, Overview of scene graph and all available data-blocks.

    PROPERTIES Properties, Edit properties of active object and related data-blocks.

    FILE_BROWSER File Browser, Browse for files and assets.

    PREFERENCES Preferences, Edit persistent configuration settings.


###Keys
Available keys and their references can be seen here https://docs.blender.org/api/current/bpy.types.KeyMapItem.html?highlight=key%20name#bpy.types.KeyMapItem.name, where the left-side CAPS is the Reference, for the colloquial key name on the right-side:


    NONE Undocumented.

    LEFTMOUSE Left Mouse, LMB.

    MIDDLEMOUSE Middle Mouse, MMB.

    RIGHTMOUSE Right Mouse, RMB.

    BUTTON4MOUSE Button4 Mouse, MB4.

    BUTTON5MOUSE Button5 Mouse, MB5.

    BUTTON6MOUSE Button6 Mouse, MB6.

    BUTTON7MOUSE Button7 Mouse, MB7.

    PEN Pen.

    ERASER Eraser.

    MOUSEMOVE Mouse Move, MsMov.

    INBETWEEN_MOUSEMOVE In-between Move, MsSubMov.

    TRACKPADPAN Mouse/Trackpad Pan, MsPan.

    TRACKPADZOOM Mouse/Trackpad Zoom, MsZoom.

    MOUSEROTATE Mouse/Trackpad Rotate, MsRot.

    MOUSESMARTZOOM Mouse/Trackpad Smart Zoom, MsSmartZoom.

    WHEELUPMOUSE Wheel Up, WhUp.

    WHEELDOWNMOUSE Wheel Down, WhDown.

    WHEELINMOUSE Wheel In, WhIn.

    WHEELOUTMOUSE Wheel Out, WhOut.

    EVT_TWEAK_L Tweak Left, TwkL.

    EVT_TWEAK_M Tweak Middle, TwkM.

    EVT_TWEAK_R Tweak Right, TwkR.

    A A.

    B B.

    C C.

    D D.

    E E.

    F F.

    G G.

    H H.

    I I.

    J J.

    K K.

    L L.

    M M.

    N N.

    O O.

    P P.

    Q Q.

    R R.

    S S.

    T T.

    U U.

    V V.

    W W.

    X X.

    Y Y.

    Z Z.

    ZERO 0.

    ONE 1.

    TWO 2.

    THREE 3.

    FOUR 4.

    FIVE 5.

    SIX 6.

    SEVEN 7.

    EIGHT 8.

    NINE 9.

    LEFT_CTRL Left Ctrl, CtrlL.

    LEFT_ALT Left Alt, AltL.

    LEFT_SHIFT Left Shift, ShiftL.

    RIGHT_ALT Right Alt, AltR.

    RIGHT_CTRL Right Ctrl, CtrlR.

    RIGHT_SHIFT Right Shift, ShiftR.

    OSKEY OS Key, Cmd.

    APP Application, App.

    GRLESS Grless.

    ESC Esc.

    TAB Tab.

    RET Return, Enter.

    SPACE Spacebar, Space.

    LINE_FEED Line Feed.

    BACK_SPACE Backspace, BkSpace.

    DEL Delete, Del.

    SEMI_COLON ;.

    PERIOD ..

    COMMA ,.

    QUOTE “.

    ACCENT_GRAVE `.

    MINUS -.

    PLUS +.

    SLASH /.

    BACK_SLASH \.

    EQUAL =.

    LEFT_BRACKET [.

    RIGHT_BRACKET ].

    LEFT_ARROW Left Arrow, ←.

    DOWN_ARROW Down Arrow, ↓.

    RIGHT_ARROW Right Arrow, →.

    UP_ARROW Up Arrow, ↑.

    NUMPAD_2 Numpad 2, Pad2.

    NUMPAD_4 Numpad 4, Pad4.

    NUMPAD_6 Numpad 6, Pad6.

    NUMPAD_8 Numpad 8, Pad8.

    NUMPAD_1 Numpad 1, Pad1.

    NUMPAD_3 Numpad 3, Pad3.

    NUMPAD_5 Numpad 5, Pad5.

    NUMPAD_7 Numpad 7, Pad7.

    NUMPAD_9 Numpad 9, Pad9.

    NUMPAD_PERIOD Numpad ., Pad..

    NUMPAD_SLASH Numpad /, Pad/.

    NUMPAD_ASTERIX Numpad *, Pad*.

    NUMPAD_0 Numpad 0, Pad0.

    NUMPAD_MINUS Numpad -, Pad-.

    NUMPAD_ENTER Numpad Enter, PadEnter.

    NUMPAD_PLUS Numpad +, Pad+.

    F1 F1.

    F2 F2.

    F3 F3.

    F4 F4.

    F5 F5.

    F6 F6.

    F7 F7.

    F8 F8.

    F9 F9.

    F10 F10.

    F11 F11.

    F12 F12.

    F13 F13.

    F14 F14.

    F15 F15.

    F16 F16.

    F17 F17.

    F18 F18.

    F19 F19.

    F20 F20.

    F21 F21.

    F22 F22.

    F23 F23.

    F24 F24.

    PAUSE Pause.

    INSERT Insert, Ins.

    HOME Home.

    PAGE_UP Page Up, PgUp.

    PAGE_DOWN Page Down, PgDown.

    END End.

    MEDIA_PLAY Media Play/Pause, >/||.

    MEDIA_STOP Media Stop, Stop.

    MEDIA_FIRST Media First, |<<.

    MEDIA_LAST Media Last, >>|.

    TEXTINPUT Text Input, TxtIn.

    WINDOW_DEACTIVATE Window Deactivate.

    TIMER Timer, Tmr.

    TIMER0 Timer 0, Tmr0.

    TIMER1 Timer 1, Tmr1.

    TIMER2 Timer 2, Tmr2.

    TIMER_JOBS Timer Jobs, TmrJob.

    TIMER_AUTOSAVE Timer Autosave, TmrSave.

    TIMER_REPORT Timer Report, TmrReport.

    TIMERREGION Timer Region, TmrReg.

    NDOF_MOTION NDOF Motion, NdofMov.

    NDOF_BUTTON_MENU NDOF Menu, NdofMenu.

    NDOF_BUTTON_FIT NDOF Fit, NdofFit.

    NDOF_BUTTON_TOP NDOF Top, Ndof↑.

    NDOF_BUTTON_BOTTOM NDOF Bottom, Ndof↓.

    NDOF_BUTTON_LEFT NDOF Left, Ndof←.

    NDOF_BUTTON_RIGHT NDOF Right, Ndof→.

    NDOF_BUTTON_FRONT NDOF Front, NdofFront.

    NDOF_BUTTON_BACK NDOF Back, NdofBack.

    NDOF_BUTTON_ISO1 NDOF Isometric 1, NdofIso1.

    NDOF_BUTTON_ISO2 NDOF Isometric 2, NdofIso2.

    NDOF_BUTTON_ROLL_CW NDOF Roll CW, NdofRCW.

    NDOF_BUTTON_ROLL_CCW NDOF Roll CCW, NdofRCCW.

    NDOF_BUTTON_SPIN_CW NDOF Spin CW, NdofSCW.

    NDOF_BUTTON_SPIN_CCW NDOF Spin CCW, NdofSCCW.

    NDOF_BUTTON_TILT_CW NDOF Tilt CW, NdofTCW.

    NDOF_BUTTON_TILT_CCW NDOF Tilt CCW, NdofTCCW.

    NDOF_BUTTON_ROTATE NDOF Rotate, NdofRot.

    NDOF_BUTTON_PANZOOM NDOF Pan/Zoom, NdofPanZoom.

    NDOF_BUTTON_DOMINANT NDOF Dominant, NdofDom.

    NDOF_BUTTON_PLUS NDOF Plus, Ndof+.

    NDOF_BUTTON_MINUS NDOF Minus, Ndof-.

    NDOF_BUTTON_ESC NDOF Esc, NdofEsc.

    NDOF_BUTTON_ALT NDOF Alt, NdofAlt.

    NDOF_BUTTON_SHIFT NDOF Shift, NdofShift.

    NDOF_BUTTON_CTRL NDOF Ctrl, NdofCtrl.

    NDOF_BUTTON_1 NDOF Button 1, NdofB1.

    NDOF_BUTTON_2 NDOF Button 2, NdofB2.

    NDOF_BUTTON_3 NDOF Button 3, NdofB3.

    NDOF_BUTTON_4 NDOF Button 4, NdofB4.

    NDOF_BUTTON_5 NDOF Button 5, NdofB5.

    NDOF_BUTTON_6 NDOF Button 6, NdofB6.

    NDOF_BUTTON_7 NDOF Button 7, NdofB7.

    NDOF_BUTTON_8 NDOF Button 8, NdofB8.

    NDOF_BUTTON_9 NDOF Button 9, NdofB9.

    NDOF_BUTTON_10 NDOF Button 10, NdofB10.

    NDOF_BUTTON_A NDOF Button A, NdofBA.

    NDOF_BUTTON_B NDOF Button B, NdofBB.

    NDOF_BUTTON_C NDOF Button C, NdofBC.

    ACTIONZONE_AREA ActionZone Area, AZone Area.

    ACTIONZONE_REGION ActionZone Region, AZone Region.

    ACTIONZONE_FULLSCREEN ActionZone Fullscreen, AZone FullScr.

Note the suggestions here:
https://docs.blender.org/manual/en/latest/advanced/keymap_editing.html#available-keys

https://docs.blender.org/manual/en/latest/interface/keymap/industry_compatible.html


"See the Keymap Code section of the __init__.py script for a working example"


###Please share