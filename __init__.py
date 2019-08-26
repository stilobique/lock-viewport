# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****


bl_info = {
    "name": "Lock View",
    "description": "Exposes rotation locking in the 3D View to a specific viewing angle",
    "author": "Jason van Gumster (Fweeb), forked by stilobique",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D View > Properties Region > View",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}

import bpy
import os

from .Views.lock_icon import load_icon

classes = [
    # Models,
    # Views,
    # Controller,
]


def lock_ui(self, context):
    load_icon(os.path.join(os.path.dirname(__file__)), state=False)


def register():
    bpy.types.VIEW3D_MT_editor_menus.append(lock_ui)


def unregister():
    bpy.types.VIEW3D_MT_editor_menus.remove(lock_ui)
