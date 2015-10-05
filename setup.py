from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='jupyter-themer',
    version='0.1.0',
    license='MIT',
    description='Custom CSS themer for jupyter notebooks',
    long_description=long_description,
    author='Leon Chen',
    author_email='lchen3@gmail.com',
    url='https://github.com/transcranial/jupyter-themer',
    packages = find_packages(exclude=['*test*']),
    package_data = {
        'jupythemer': ['styles/**/*.css']
    },
    entry_points = {
        'console_scripts' : [
            'jupyter-themer = jupythemer.jupythemer:run'
        ]
    },
    install_requires=['jupyter', 'notebook'],
    download_url = 'https://github.com/transcranial/jupyter-themer/tarball/0.1.0',
    keywords = ['jupyter', 'ipython', 'notebook', 'themes', 'css'],
)
