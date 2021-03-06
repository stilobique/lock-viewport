import bpy
import gpu
import bgl

from os.path import join
from gpu_extras.batch import batch_for_shader


def load_icon(path):
    """
    Function to draw the Lock Icon
    :param path:
    :return:
    """
    picture = ''
    for icon in bpy.data.images:
        if icon.name == 'lock-icon.tga':
            picture = bpy.data.images[icon.name]
            break
        else:
            picture = bpy.data.images.load(join(path, 'lock-icon.tga'))
            break
    scn = bpy.context.scene.Viewport
    state = scn.lock_activate

    if state:
        uv_icon = ((0, 0), (1, 0), (1, 0.5), (0, 0.5))
    else:
        uv_icon = ((0, 0.5), (1, 0.5), (1, 1), (0, 1))
    shader = gpu.shader.from_builtin('2D_IMAGE')
    batch = batch_for_shader(
        shader, 'TRI_FAN',
        {
            "pos": ((100, 100), (200, 100), (200, 200), (100, 200)),
            "texCoord": uv_icon,
        },
    )

    if picture.gl_load():
        raise Exception()

    def draw():
        bgl.glActiveTexture(bgl.GL_TEXTURE0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, picture.bindcode)

        shader.bind()
        shader.uniform_int("image", 0)
        batch.draw(shader)

    def event():
        print('Not really important')

    bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_PIXEL')
