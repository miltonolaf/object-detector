import click
import json

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """TensorFlow Obeject Detection
    """


@click.command('demo', short_help='Run demos')
@click.option('-D', '--download', is_flag=True,
              help='Download all pre-trained models.')
def demo(download):
    """Play with pre-trained models and check your functionality for yourself
    """
    if download:
        from tf_object_detector.demo import demo_download
        click.echo('test')
        demo_download()


cli.add_command(demo)


@click.command('init', short_help='Init app')
def init():
    """Initialize your project by creating the configuration file with this command
    """
    from tf_object_detector.config import Config
    cfg = Config()
    cfg.init_config()

cli.add_command(init)
