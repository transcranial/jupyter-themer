from setuptools import setup, find_packages

long_description = 'Apply custom CSS styling to your jupyter notebooks.\n\nMix and match themes by:\n\n- color\n- layout\n- typography\n'

setup(
    name='jupyter-themer',
    version='0.1.2',
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
    keywords = ['jupyter', 'ipython', 'notebook', 'themes', 'css'],
)
