#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

# Info
THEME_NAME = "Fuchsia"
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/fuchsia-cursor"

# XCursor
X_DELAY: int = 35


# Windows Cursor
WIN_DELAY = 2

X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    ##########
    # Static #
    ##########
    "all-scroll.png": {"xhot": 100, "yhot": 100},
    "bottom_left_corner.png": {"xhot": 98, "yhot": 97},
    "bottom_right_corner.png": {"xhot": 98, "yhot": 99},
    "bottom_tee.png": {"xhot": 98, "yhot": 144},
    "center_ptr.png": {"xhot": 100, "yhot": 20},
    "context-menu.png": {"xhot": 28, "yhot": 28},
    "copy.png": {"xhot": 28, "yhot": 28},
    "cross.png": {"xhot": 100, "yhot": 100},
    "crossed_circle.png": {"xhot": 28, "yhot": 28},
    "crosshair.png": {"xhot": 99, "yhot": 100},
    "dnd_no_drop.png": {"xhot": 28, "yhot": 28},
    "dotbox.png": {"xhot": 100, "yhot": 100},
    "hand1.png": {"xhot": 100, "yhot": 100},
    "hand2.png": {"xhot": 28, "yhot": 28},
    "left_ptr.png": {"xhot": 28, "yhot": 28},
    "left_side.png": {"xhot": 99, "yhot": 99},
    "left_tee.png": {"xhot": 53, "yhot": 100},
    "link.png": {"xhot": 28, "yhot": 28},
    "ll_angle.png": {"xhot": 66, "yhot": 132},
    "lr_angle.png": {"xhot": 131, "yhot": 132},
    "move.png": {"xhot": 100, "yhot": 100},
    "pencil.png": {"xhot": 49, "yhot": 150},
    "plus.png": {"xhot": 99, "yhot": 98},
    "question_arrow.png": {"xhot": 28, "yhot": 28},
    "right_ptr.png": {"xhot": 171, "yhot": 28},
    "right_tee.png": {"xhot": 145, "yhot": 99},
    "sb_down_arrow.png": {"xhot": 101, "yhot": 146},
    "sb_h_double_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_left_arrow.png": {"xhot": 53, "yhot": 100},
    "sb_right_arrow.png": {"xhot": 147, "yhot": 100},
    "sb_up_arrow.png": {"xhot": 100, "yhot": 53},
    "sb_v_double_arrow.png": {"xhot": 99, "yhot": 99},
    "top_side.png": {"xhot": 100, "yhot": 96},
    "top_tee.png": {"xhot": 98, "yhot": 55},
    "ul_angle.png": {"xhot": 67, "yhot": 68},
    "ur_angle.png": {"xhot": 147, "yhot": 52},
    "vertical-text.png": {"xhot": 100, "yhot": 100},
    "wayland-cursor.png": {"xhot": 100, "yhot": 100},
    "X_cursor.png": {"xhot": 100, "yhot": 100},
    "xterm.png": {"xhot": 98, "yhot": 97},
    "zoom-in.png": {"xhot": 89, "yhot": 88},
    "zoom-out.png": {"xhot": 88, "yhot": 89},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need an extension and frame numbers.
    "left_ptr_watch": {"xhot": 28, "yhot": 28},
    "wait": {"xhot": 100, "yhot": 100},
}

WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    ##########
    # Static #
    ##########
    "right_ptr.png": {"to": "Alternate", "position": "top_right"},
    "cross.png": {"to": "Cross"},
    "left_ptr.png": {"to": "Default", "position": "top_left"},
    "bottom_right_corner.png": {"to": "Diagonal_1"},
    "bottom_left_corner.png": {"to": "Diagonal_2"},
    "pencil.png": {"to": "Handwriting"},
    "question_arrow.png": {"to": "Help", "position.png": "top_left"},
    "sb_h_double_arrow.png": {"to": "Horizontal"},
    "xterm.png": {"to": "IBeam", "position": "top_left"},
    "hand2.png": {"to": "Link", "position": "top_left"},
    "hand1.png": {"to": "Move"},
    "crossed_circle.png": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow.png": {"to": "Vertical"},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need frame numbers.
    "left_ptr_watch": {"to": "Work", "position": "top_left"},
    "wait": {"to": "Busy"},
}
