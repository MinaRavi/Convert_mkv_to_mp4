import os
import ffmpeg
start_dir = os.getcwd() #giving it the placed directory (looks for the same folder as this code)


def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + '.mp4'
    ffmpeg.input(mkv_file).output(out_name).run()
    print('Finished Converting {}'.format(mkv_file))