import click
from libs.Console import get_terminal_size, to_string_image, render, clear
from libs.Frame import read_image, check_camera, get_frame, relative_resize, check_video, get_video_fps
import time


def validate_jpg(_, __, value):
    if not value.lower().endswith('.jpg') and not value.lower().endswith('.png') and not value.lower().endswith('.jpeg'):
        raise click.BadParameter('The file must have a .jpg extension.')
    return value


def validate_mp4(_, __, value):
    if not value.lower().endswith('.mp4'):
        raise click.BadParameter('The file must have a .jpg extension.')
    return value


@click.command("show-image")
@click.argument('path', type=click.Path(exists=True, readable=True), callback=validate_jpg)
def print_picture(path):
    width, height = get_terminal_size()
    image = read_image(path)
    image = relative_resize(image, width, height)
    image = to_string_image(image)
    clear()
    render(image)


@click.command("show-video")
@click.argument('path', type=click.Path(exists=True, readable=True), callback=validate_mp4)
def show_video(path):
    clear()
    check_video(path)
    fps = get_video_fps(path)
    while True:
        width, height = get_terminal_size()
        image = get_frame()
        image = relative_resize(image, width, height)
        image = to_string_image(image)
        render(image)
        time.sleep(1/fps)


@click.command("show-camera")
def show_camera():
    clear()
    check_camera()
    while True:
        width, height = get_terminal_size()
        image = get_frame()
        image = relative_resize(image, width, height)
        image = to_string_image(image)
        render(image)


@click.group()
def cli():
    pass


cli.add_command(print_picture)
cli.add_command(show_camera)
cli.add_command(show_video)

if __name__ == '__main__':
    cli()
