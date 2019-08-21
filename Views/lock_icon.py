import bpy
import gpu
import bgl

from os.path import join
from gpu_extras.batch import batch_for_shader


def load_icon(image):
    shader = gpu.shader.from_builtin('2D_IMAGE')
    batch = batch_for_shader(
        shader, 'TRI_FAN',
        {
            "pos": ((100, 100), (128, 100), (128, 128), (100, 128)),
            "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
        },
    )

    if image.gl_load():
        raise Exception()

    def draw():
        bgl.glActiveTexture(bgl.GL_TEXTURE0)
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, image.bindcode)

        shader.bind()
        shader.uniform_int("image", 0)
        batch.draw(shader)

    bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_PIXEL')
