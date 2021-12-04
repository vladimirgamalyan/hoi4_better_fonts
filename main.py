import click


@click.command()
@click.argument('font_dir', type=click.Path(exists=True, file_okay=False))
def make_fonts(font_dir):
    print(font_dir)


if __name__ == '__main__':
    make_fonts()
