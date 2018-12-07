import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='tf_object_detector',
    version='1.0',
    url='https://github.com/miltonolaf/tf-object-detection',
    license='MIT',
    maintainer='Milton Olaf Paredes',
    maintainer_email='olafmilton@gmail.com',
    description='',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jsonschema==2.6.0',
        'matplotlib==3.0.1',
        'numpy==1.15.3',
        'opencv-python==3.4.3.18',
        'pandocfilters==1.4.2',
        'scikit-image==0.14.1',
        'scipy==1.1.0',
        'see==1.4.1',
        'six==1.11.0',
        'tensorflow==1.11.0',
        'click'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
    entry_points={
        'console_scripts': [
            'tensorobject = tf_object_detector.cli:cli',
        ],
    }
)
