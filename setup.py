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
        '',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
