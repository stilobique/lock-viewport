import bpy
import gpu
import bgl
from gpu_extras.batch import batch_for_shader


def load_icon_picture(image_name):
    picture = ''
    for icon in bpy.data.images:
        if icon.name == image_name:
            picture = bpy.data.images[image_name]
        else:
            picture = bpy.data.images.load(r'W:\WIP Git\Blender-Setup\blender-addons\Lock-Viewport\Resources\Test.png')

    return picture


def load_icon():
    shader = gpu.shader.from_builtin('2D_IMAGE')
    batch = batch_for_shader(
        shader, 'TRI_FAN',
        {
            "pos": ((100, 100), (200, 100), (200, 200), (100, 200)),
            "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
        },
    )

    image = load_icon_picture('IconLock')
    if image.gl_load():
        raise Exception()

    def draw():
        bgl.glActiveTexture(bgl.GL_TEXTURE0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, image.bindcode)

        shader.bind()
        shader.uniform_int("image", 0)
        batch.draw(shader)

    bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_PIXEL')
