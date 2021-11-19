from typing import NewType, Optional, Tuple, Union

ImGuiWindowFlags = NewType("ImGuiWindowFlags", int)
ImGuiFocusedFlags = NewType("ImGuiFocusedFlags", int)
ImGuiStyleVar = NewType("ImGuiStyleVar", int)
ImGuiID = NewType("ImGuiID", int)
ImGuiDir = NewType("ImGuiDir", int)
ImGuiCond = NewType("ImGuiCond", int)
ImU32 = NewType("ImU32", int)
ImGuiCol = NewType("ImGuiCol", int)
ImVec2 = Tuple[float, float]
ImVec4 = Tuple[float, float, float, float]

# Windows
def Begin(
    name: str, open: Optional[bool] = None, flags: ImGuiWindowFlags = 0
) -> bool: ...
def End() -> None: ...

# Child Windows
def BeginChild(
    str_id: str,
    size: ImVec2 = (0, 0),
    border: bool = False,
    flags: ImGuiWindowFlags = 0,
) -> bool: ...
def BeginChild(
    id: ImGuiID,
    size: ImVec2 = (0, 0),
    border: bool = False,
    flags: ImGuiWindowFlags = 0,
) -> bool: ...
def Endchild() -> None: ...

# Windows Utilities
def IsWindowAppearing() -> bool: ...
def IsWindowCollapsed() -> bool: ...
def IsWindowFocused(flags: ImGuiFocusedFlags = 0) -> bool: ...
def IsWindowHovered(flags: ImGuiFocusedFlags = 0) -> bool: ...
def GetWindowPos() -> ImVec2: ...
def GetWindowSize() -> ImVec2: ...
def GetWindowWidth() -> float: ...
def GetWindowHeight() -> float: ...
def SetNextWindowPos(
    pos: ImVec2, cone: ImGuiCond = 0, pivot: ImVec2 = (0, 0)
) -> None: ...
def SetNextWindowSize(size: ImVec2, cond: ImGuiCond = 0) -> None: ...
def SetNextWindowSizeConstraints(size_min: ImVec2, size_max: ImVec2) -> None: ...
def SetNextWindowContentSize(size: ImVec2) -> None: ...
def SetNextWindowCollapsed(collapsed: bool, cond: ImGuiCond = 0) -> None: ...
def SetNextWindowFocus() -> None: ...
def SetNextWindowBgAlpha(alpha: float) -> None: ...
def SetWindowPos(pos: ImVec2, cond: ImGuiCond = 0) -> None: ...
def SetWindowSize(pos: ImVec2, cond: ImGuiCond = 0) -> None: ...
def SetWindowCollapsed(collapsed: bool, cond: ImGuiCond = 0) -> None: ...
def SetWindowFocus() -> None: ...
def SetWindowFontScale(scale: float) -> None: ...
def SetWindowPos(name: str, pos: ImVec2, cond: ImGuiCond = 0) -> None: ...
def SetWindowSize(name: str, size: ImVec2, cond: ImGuiCond = 0) -> None: ...
def SetWindowSize(name: str, size: ImVec2, cond: ImGuiCond = 0) -> None: ...
def SetWindowCollapsed(name: str, collapsed: bool, cond: ImGuiCond = 0) -> None: ...
def SetWindowFocus(name: str) -> None: ...

# Content region
def GetContentRegionMax() -> ImVec2: ...
def GetContentRegionAvail() -> ImVec2: ...
def GetWindowContentRegionMin() -> ImVec2: ...
def GetWindowContentRegionMax() -> ImVec2: ...
def GetWindowContentRegionWidth() -> float: ...

# Windows Scrolling
def GetScrollX() -> float: ...
def GetScrollY() -> float: ...
def GetScrollMaxX() -> float: ...
def GetScrollMaxY() -> float: ...
def SetScrollX(scroll_x: float) -> None: ...
def SetScrollY(scroll_y: float) -> None: ...
def SetScrollHereX(center_x_ratio: float = 0.5) -> None: ...
def SetScrollHereY(center_y_ratio: float = 0.5) -> None: ...
def SetScrollFromPosX(local_x: float, center_x_ratio: float = 0.5) -> None: ...
def SetScrollFromPosY(local_y: float, center_y_ratio: float = 0.5) -> None: ...

# Parameters stacks (shared)
def PushStyleColor(idx: ImGuiCol, col: ImU32) -> None: ...
def PushStyleColor(idx: ImGuiCol, col: ImVec4) -> None: ...
def PopStyleColor(count: int = 1) -> None: ...
def PushStyleVar(idx: ImGuiStyleVar, val: float) -> None: ...
def PushStyleVar(idx: ImGuiStyleVar, val: ImVec2) -> None: ...
def PopStyleVar(count: int = 1) -> None: ...
def GetStyleColorVec4(idx: ImGuiCol) -> ImVec4: ...
def GetFontSize() -> float: ...
def GetFontTexUvWhitePixel() -> ImVec2: ...
def GetColorU32(idx: ImGuiCol, alpha_mul: float = 1.0) -> ImU32: ...
def GetColorU32(col: ImVec4) -> ImU32: ...
def GetColorU32(col: ImU32) -> ImU32: ...

# Parameters stacks (current window)
def PushItemWidth(item_width) -> float: ...
def PopItemWidth() -> None: ...
def SetNextItemWidth(item_width) -> float: ...
def CalcItemWidth() -> float: ...
def CalcItemWidth() -> float: ...
def PushTextWrapPos(wrap_local_pos_x: float) -> None: ...
def PopTextWrapPos() -> None: ...
def PushAllowKeyboardFocus(allow_keyboard_focus: bool) -> None: ...
def PopAllowKeyboardFocus() -> None: ...
def PushButtonRepeat(repeat: bool) -> None: ...
def PopButtonRepeat() -> None: ...

# Cursor / Layout
def Separator() -> None: ...
def SameLine(offset_from_start_x: float = 0.0, spacing: float = 1.0) -> None: ...
def NewLine() -> None: ...
def Spacing() -> None: ...
def Dummy(size: ImVec2) -> None: ...
def Indent(intent_w: float = 0.0) -> None: ...
def Unindent(intent_w: float = 0.0) -> None: ...
def BeginGroup() -> None: ...
def EndGroup() -> None: ...
def GetCursorPos() -> ImVec2: ...
def GetCursorPosX() -> float: ...
def SetCursorPos(local_pos: ImVec2) -> None: ...
def SetCursorPosX(locol_x: float) -> None: ...
def SetCursorPosY(locol_y: float) -> None: ...
def GetCursorStartPos() -> ImVec2: ...
def GetCursorScreenPos() -> ImVec2: ...
def SetCursorScreenPos(pos: ImVec2) -> None: ...
def AlignTextToFramePadding() -> None: ...
def GetTextLineHeight() -> float: ...
def GetTextLineHeightWithSpacing() -> float: ...
def GetFrameHeight() -> float: ...
def GetFrameHeightWithSpacing() -> float: ...

# ID stack/scopes
def PushID(str_id: str) -> None: ...
def PushID(int_id: int) -> None: ...
def PopID() -> None: ...
def GetID(str_id: str) -> ImGuiID: ...

# Widgets: Text
def Text(text: str) -> None: ...
def TextColored(col: ImVec4, text: str) -> None: ...
def TextDisabled(text: str) -> None: ...
def TextWrapped(text: str) -> None: ...
def LabelText(label: str) -> None: ...
def BulletText(text: str) -> None: ...

# Widgets: Main
def Button(label: str, size: ImVec2 = (0, 0)) -> bool: ...
def SmallButton(label: str) -> bool: ...
def InvisibleButton(str_id: str, size: ImVec2) -> bool: ...
def ArrowButton(str_id: str, dir: ImGuiDir) -> bool: ...
def Checkbox(label: str, v: bool) -> Tuple[bool, bool]: ...
def CheckboxFlags(label: str, flags: int, flags_value: int) -> Tuple[bool, int]: ...
def RadioButton(label: str, active: bool) -> bool: ...
def RadioButton(label: str, v: int, v_button: int) -> Tuple[bool, int]: ...
def ProgressBar(fraction: float, size_arg: ImVec2 = (-1, 0)) -> None: ...
def Bullte() -> None: ...

#
def PushStyleColor(idx: ImGuiCol, col: ImU32) -> None: ...
def PushStyleColor(idx: ImGuiCol, col: ImVec4) -> None: ...
def PopStyleColor(count: int) -> None: ...
def PushStyleVar(idx: ImGuiCol, val: Union[ImVec2, float]) -> None: ...
def PopStyleVar(count: int) -> None: ...
def GetStyleColorVec4(idx: ImGuiCol) -> ImVec4: ...
def GetFontSize() -> int: ...
def GetFontTePushTextWrapPosxUvWhitePixel() -> ImVec2: ...
def GetColorU32(idx: ImGuiCol, alpha_mul: float = 1.0) -> ImU32: ...
def GetColorU32(col: ImVec4) -> ImU32: ...
def GetColorU32(col: ImU32) -> ImU32: ...
def PushItemWidth(item_width: float) -> None: ...
def PopItemWidth() -> None: ...
def SetNextItemWidth(item_width: float) -> None: ...
def CalcItemWidth() -> float: ...

ImGuiWindowFlags_None: int
ImGuiWindowFlags_NoTitleBar: int
ImGuiWindowFlags_NoResize: int
ImGuiWindowFlags_NoMove: int
ImGuiWindowFlags_NoScrollbar: int
ImGuiWindowFlags_NoScrollWithMouse: int
ImGuiWindowFlags_NoCollapse: int
ImGuiWindowFlags_AlwaysAutoResize: int
ImGuiWindowFlags_NoBackground: int
ImGuiWindowFlags_NoSavedSettings: int
ImGuiWindowFlags_NoMouseInputs: int
ImGuiWindowFlags_MenuBar: int
ImGuiWindowFlags_HorizontalScrollbar: int
ImGuiWindowFlags_NoFocusOnAppearing: int
ImGuiWindowFlags_NoBringToFrontOnFocus: int
ImGuiWindowFlags_AlwaysVerticalScrollbar: int
ImGuiWindowFlags_AlwaysHorizontalScrollbar: int
ImGuiWindowFlags_AlwaysUseWindowPadding: int
ImGuiWindowFlags_NoNavInputs: int
ImGuiWindowFlags_NoNavFocus: int
ImGuiWindowFlags_UnsavedDocument: int
ImGuiWindowFlags_NoNav: int
ImGuiWindowFlags_NoDecoration: int
ImGuiWindowFlags_NoInputs: int
ImGuiWindowFlags_NavFlattened: int
ImGuiWindowFlags_ChildWindow: int
ImGuiWindowFlags_Tooltip: int
ImGuiWindowFlags_Popup: int
ImGuiWindowFlags_Modal: int
ImGuiWindowFlags_ChildMenu: int
ImGuiInputTextFlags_None: int
ImGuiInputTextFlags_CharsDecimal: int
ImGuiInputTextFlags_CharsHexadecimal: int
ImGuiInputTextFlags_CharsUppercase: int
ImGuiInputTextFlags_CharsNoBlank: int
ImGuiInputTextFlags_AutoSelectAll: int
ImGuiInputTextFlags_EnterReturnsTrue: int
ImGuiInputTextFlags_CallbackCompletion: int
ImGuiInputTextFlags_CallbackHistory: int
ImGuiInputTextFlags_CallbackAlways: int
ImGuiInputTextFlags_CallbackCharFilter: int
ImGuiInputTextFlags_AllowTabInput: int
ImGuiInputTextFlags_CtrlEnterForNewLine: int
ImGuiInputTextFlags_NoHorizontalScroll: int
ImGuiInputTextFlags_AlwaysInsertMode: int
ImGuiInputTextFlags_ReadOnly: int
ImGuiInputTextFlags_Password: int
ImGuiInputTextFlags_NoUndoRedo: int
ImGuiInputTextFlags_CharsScientific: int
ImGuiInputTextFlags_CallbackResize: int
ImGuiInputTextFlags_Multiline: int
ImGuiInputTextFlags_NoMarkEdited: int
ImGuiTreeNodeFlags_None: int
ImGuiTreeNodeFlags_Selected: int
ImGuiTreeNodeFlags_Framed: int
ImGuiTreeNodeFlags_AllowItemOverlap: int
ImGuiTreeNodeFlags_NoTreePushOnOpen: int
ImGuiTreeNodeFlags_NoAutoOpenOnLog: int
ImGuiTreeNodeFlags_DefaultOpen: int
ImGuiTreeNodeFlags_OpenOnDoubleClick: int
ImGuiTreeNodeFlags_OpenOnArrow: int
ImGuiTreeNodeFlags_Leaf: int
ImGuiTreeNodeFlags_Bullet: int
ImGuiTreeNodeFlags_FramePadding: int
ImGuiTreeNodeFlags_SpanAvailWidth: int
ImGuiTreeNodeFlags_SpanFullWidth: int
ImGuiTreeNodeFlags_NavLeftJumpsBackHere: int
ImGuiTreeNodeFlags_CollapsingHeader: int
ImGuiSelectableFlags_None: int
ImGuiSelectableFlags_DontClosePopups: int
ImGuiSelectableFlags_SpanAllColumns: int
ImGuiSelectableFlags_AllowDoubleClick: int
ImGuiSelectableFlags_Disabled: int
ImGuiSelectableFlags_AllowItemOverlap: int
ImGuiComboFlags_None: int
ImGuiComboFlags_PopupAlignLeft: int
ImGuiComboFlags_HeightSmall: int
ImGuiComboFlags_HeightRegular: int
ImGuiComboFlags_HeightLarge: int
ImGuiComboFlags_HeightLargest: int
ImGuiComboFlags_NoArrowButton: int
ImGuiComboFlags_NoPreview: int
ImGuiComboFlags_HeightMask_: int
ImGuiTabBarFlags_None: int
ImGuiTabBarFlags_Reorderable: int
ImGuiTabBarFlags_AutoSelectNewTabs: int
ImGuiTabBarFlags_TabListPopupButton: int
ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: int
ImGuiTabBarFlags_NoTabListScrollingButtons: int
ImGuiTabBarFlags_NoTooltip: int
ImGuiTabBarFlags_FittingPolicyResizeDown: int
ImGuiTabBarFlags_FittingPolicyScroll: int
ImGuiTabBarFlags_FittingPolicyMask_: int
ImGuiTabBarFlags_FittingPolicyDefault_: int
ImGuiTabItemFlags_None: int
ImGuiTabItemFlags_UnsavedDocument: int
ImGuiTabItemFlags_SetSelected: int
ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: int
ImGuiTabItemFlags_NoPushId: int
ImGuiFocusedFlags_None: int
ImGuiFocusedFlags_ChildWindows: int
ImGuiFocusedFlags_RootWindow: int
ImGuiFocusedFlags_AnyWindow: int
ImGuiFocusedFlags_RootAndChildWindows: int
ImGuiHoveredFlags_None: int
ImGuiHoveredFlags_ChildWindows: int
ImGuiHoveredFlags_RootWindow: int
ImGuiHoveredFlags_AnyWindow: int
ImGuiHoveredFlags_AllowWhenBlockedByPopup: int
ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: int
ImGuiHoveredFlags_AllowWhenOverlapped: int
ImGuiHoveredFlags_AllowWhenDisabled: int
ImGuiHoveredFlags_RectOnly: int
ImGuiHoveredFlags_RootAndChildWindows: int
ImGuiDragDropFlags_None: int
ImGuiDragDropFlags_SourceNoPreviewTooltip: int
ImGuiDragDropFlags_SourceNoDisableHover: int
ImGuiDragDropFlags_SourceNoHoldToOpenOthers: int
ImGuiDragDropFlags_SourceAllowNullID: int
ImGuiDragDropFlags_SourceExtern: int
ImGuiDragDropFlags_SourceAutoExpirePayload: int
ImGuiDragDropFlags_AcceptBeforeDelivery: int
ImGuiDragDropFlags_AcceptNoDrawDefaultRect: int
ImGuiDragDropFlags_AcceptNoPreviewTooltip: int
ImGuiDragDropFlags_AcceptPeekOnly: int
ImGuiDataType_S8: int
ImGuiDataType_U8: int
ImGuiDataType_S16: int
ImGuiDataType_U16: int
ImGuiDataType_S32: int
ImGuiDataType_U32: int
ImGuiDataType_S64: int
ImGuiDataType_U64: int
ImGuiDataType_Float: int
ImGuiDataType_Double: int
ImGuiDataType_COUN: int
ImGuiDir_None: int
ImGuiDir_Left: int
ImGuiDir_Right: int
ImGuiDir_Up: int
ImGuiDir_Down: int
ImGuiDir_COUNT: int
ImGuiKey_Tab: int
ImGuiKey_LeftArrow: int
ImGuiKey_RightArrow: int
ImGuiKey_UpArrow: int
ImGuiKey_DownArrow: int
ImGuiKey_PageUp: int
ImGuiKey_PageDown: int
ImGuiKey_Home: int
ImGuiKey_End: int
ImGuiKey_Insert: int
ImGuiKey_Delete: int
ImGuiKey_Backspace: int
ImGuiKey_Space: int
ImGuiKey_Enter: int
ImGuiKey_Escape: int
ImGuiKey_KeyPadEnter: int
ImGuiKey_A: int
ImGuiKey_C: int
ImGuiKey_V: int
ImGuiKey_X: int
ImGuiKey_Y: int
ImGuiKey_Z: int
ImGuiKey_COUNT: int
ImGuiKeyModFlags_None: int
ImGuiKeyModFlags_Ctrl: int
ImGuiKeyModFlags_Shift: int
ImGuiKeyModFlags_Alt: int
ImGuiKeyModFlags_Super: int
ImGuiNavInput_Activate: int
ImGuiNavInput_Cancel: int
ImGuiNavInput_Input: int
ImGuiNavInput_Menu: int
ImGuiNavInput_DpadLeft: int
ImGuiNavInput_DpadRight: int
ImGuiNavInput_DpadUp: int
ImGuiNavInput_DpadDown: int
ImGuiNavInput_LStickLeft: int
ImGuiNavInput_LStickRight: int
ImGuiNavInput_LStickUp: int
ImGuiNavInput_LStickDown: int
ImGuiNavInput_FocusPrev: int
ImGuiNavInput_FocusNext: int
ImGuiNavInput_TweakSlow: int
ImGuiNavInput_TweakFast: int
ImGuiNavInput_KeyMenu_: int
ImGuiNavInput_KeyLeft_: int
ImGuiNavInput_KeyRight_: int
ImGuiNavInput_KeyUp_: int
ImGuiNavInput_KeyDown_: int
ImGuiNavInput_COUNT: int
ImGuiNavInput_InternalStart_: int
ImGuiConfigFlags_None: int
ImGuiConfigFlags_NavEnableKeyboard: int
ImGuiConfigFlags_NavEnableGamepad: int
ImGuiConfigFlags_NavEnableSetMousePos: int
ImGuiConfigFlags_NavNoCaptureKeyboard: int
ImGuiConfigFlags_NoMouse: int
ImGuiConfigFlags_NoMouseCursorChange: int
ImGuiConfigFlags_IsSRGB: int
ImGuiConfigFlags_IsTouchScreen: int
ImGuiBackendFlags_None: int
ImGuiBackendFlags_HasGamepad: int
ImGuiBackendFlags_HasMouseCursors: int
ImGuiBackendFlags_HasSetMousePos: int
ImGuiBackendFlags_RendererHasVtxOffset: int
ImGuiCol_Text: int
ImGuiCol_TextDisabled: int
ImGuiCol_WindowBg: int
ImGuiCol_ChildBg: int
ImGuiCol_PopupBg: int
ImGuiCol_Border: int
ImGuiCol_BorderShadow: int
ImGuiCol_FrameBg: int
ImGuiCol_FrameBgHovered: int
ImGuiCol_FrameBgActive: int
ImGuiCol_TitleBg: int
ImGuiCol_TitleBgActive: int
ImGuiCol_TitleBgCollapsed: int
ImGuiCol_MenuBarBg: int
ImGuiCol_ScrollbarBg: int
ImGuiCol_ScrollbarGrab: int
ImGuiCol_ScrollbarGrabHovered: int
ImGuiCol_ScrollbarGrabActive: int
ImGuiCol_CheckMark: int
ImGuiCol_SliderGrab: int
ImGuiCol_SliderGrabActive: int
ImGuiCol_Button: int
ImGuiCol_ButtonHovered: int
ImGuiCol_ButtonActive: int
ImGuiCol_Header: int
ImGuiCol_HeaderHovered: int
ImGuiCol_HeaderActive: int
ImGuiCol_Separator: int
ImGuiCol_SeparatorHovered: int
ImGuiCol_SeparatorActive: int
ImGuiCol_ResizeGrip: int
ImGuiCol_ResizeGripHovered: int
ImGuiCol_ResizeGripActive: int
ImGuiCol_Tab: int
ImGuiCol_TabHovered: int
ImGuiCol_TabActive: int
ImGuiCol_TabUnfocused: int
ImGuiCol_TabUnfocusedActive: int
ImGuiCol_PlotLines: int
ImGuiCol_PlotLinesHovered: int
ImGuiCol_PlotHistogram: int
ImGuiCol_PlotHistogramHovered: int
ImGuiCol_TextSelectedBg: int
ImGuiCol_DragDropTarget: int
ImGuiCol_NavHighlight: int
ImGuiCol_NavWindowingHighlight: int
ImGuiCol_NavWindowingDimBg: int
ImGuiCol_ModalWindowDimBg: int
ImGuiCol_COUNT: int
ImGuiStyleVar_Alpha: int
ImGuiStyleVar_WindowPadding: int
ImGuiStyleVar_WindowRounding: int
ImGuiStyleVar_WindowBorderSize: int
ImGuiStyleVar_WindowMinSize: int
ImGuiStyleVar_WindowTitleAlign: int
ImGuiStyleVar_ChildRounding: int
ImGuiStyleVar_ChildBorderSize: int
ImGuiStyleVar_PopupRounding: int
ImGuiStyleVar_PopupBorderSize: int
ImGuiStyleVar_FramePadding: int
ImGuiStyleVar_FrameRounding: int
ImGuiStyleVar_FrameBorderSize: int
ImGuiStyleVar_ItemSpacing: int
ImGuiStyleVar_ItemInnerSpacing: int
ImGuiStyleVar_IndentSpacing: int
ImGuiStyleVar_ScrollbarSize: int
ImGuiStyleVar_ScrollbarRounding: int
ImGuiStyleVar_GrabMinSize: int
ImGuiStyleVar_GrabRounding: int
ImGuiStyleVar_TabRounding: int
ImGuiStyleVar_ButtonTextAlign: int
ImGuiStyleVar_SelectableTextAlign: int
ImGuiStyleVar_COUNT: int
ImGuiColorEditFlags_None: int
ImGuiColorEditFlags_NoAlpha: int
ImGuiColorEditFlags_NoPicker: int
ImGuiColorEditFlags_NoOptions: int
ImGuiColorEditFlags_NoSmallPreview: int
ImGuiColorEditFlags_NoInputs: int
ImGuiColorEditFlags_NoTooltip: int
ImGuiColorEditFlags_NoLabel: int
ImGuiColorEditFlags_NoSidePreview: int
ImGuiColorEditFlags_NoDragDrop: int
ImGuiColorEditFlags_NoBorder: int
ImGuiColorEditFlags_AlphaBar: int
ImGuiColorEditFlags_AlphaPreview: int
ImGuiColorEditFlags_AlphaPreviewHalf: int
ImGuiColorEditFlags_HDR: int
ImGuiColorEditFlags_DisplayRGB: int
ImGuiColorEditFlags_DisplayHSV: int
ImGuiColorEditFlags_DisplayHex: int
ImGuiColorEditFlags_Uint8: int
ImGuiColorEditFlags_Float: int
ImGuiColorEditFlags_PickerHueBar: int
ImGuiColorEditFlags_PickerHueWheel: int
ImGuiColorEditFlags_InputRGB: int
ImGuiColorEditFlags_InputHSV: int
ImGuiColorEditFlags__OptionsDefault: int
ImGuiColorEditFlags__DisplayMask: int
ImGuiColorEditFlags__DataTypeMask: int
ImGuiColorEditFlags__PickerMask: int
ImGuiColorEditFlags__InputMask: int
ImGuiMouseButton_Left: int
ImGuiMouseButton_Right: int
ImGuiMouseButton_Middle: int
ImGuiMouseButton_COUNT: int
ImGuiMouseCursor_None: int
ImGuiMouseCursor_Arrow: int
ImGuiMouseCursor_TextInput: int
ImGuiMouseCursor_ResizeAll: int
ImGuiMouseCursor_ResizeNS: int
ImGuiMouseCursor_ResizeEW: int
ImGuiMouseCursor_ResizeNESW: int
ImGuiMouseCursor_ResizeNWSE: int
ImGuiMouseCursor_Hand: int
ImGuiMouseCursor_NotAllowed: int
ImGuiMouseCursor_COUNT: int
ImGuiCond_Always: int
ImGuiCond_Once: int
ImGuiCond_FirstUseEver: int
ImGuiCond_Appearing: int
