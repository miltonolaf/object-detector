from tf_object_detector.config import Config
import click


def main():
    pass


def demo_download():
    import sys
    if sys.version_info[0] >= 3:
        from urllib.request import urlretrieve
    else:
        from urllib import urlretrieve
    import tarfile

    model_url = 'http://download.tensorflow.org/models/object_detection/'
    cfg = Config()
    downloaded_models_dir = cfg.DOWNLOADED_MODELS_DIR

    for model, file in cfg.DEMO_MODELS.items():
        click.echo('Downloading all demo models...')
        click.echo('This may take a while.')
        urlretrieve(model_url + file + '.tar.gz', downloaded_models_dir + file)
        tf = tarfile.open(downloaded_models_dir + '/' + file + '.tar.gz')
        tf.extractall()
