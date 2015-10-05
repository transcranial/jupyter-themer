from __future__ import print_function

import jupyter
import os
import sys
import argparse

current_dir = os.path.dirname(os.path.realpath(__file__))
jupyter_dir = os.path.dirname(jupyter.__file__)
custom_css_filepath = jupyter_dir + '/notebook/static/custom/custom.css'


def write_to_css(content):
    try:
        with open(custom_css_filepath, 'w') as f:
            f.write(content)
    except:
        print('Error writing to custom.css')
        sys.exit(1)


def run(args=None):
    if args is None:
        parser = argparse.ArgumentParser(description='Jupyter notebook themer.')
        parser.add_argument('-c', '--color', required=False, dest='color', default=None, help='color style')
        parser.add_argument('-l', '--layout', required=False, dest='layout', default=None, help='layout style')
        parser.add_argument('-t', '--typography', required=False, dest='typography', default=None, help='typography style')
        args = parser.parse_args()

    if args.color is None and args.layout is None and args.typography is None:
        print('Jupyter notebook reverted to default style.')
        write_to_css('')
        sys.exit()

    content_all = ''
    if args.color is not None:
        try:
            with open('{}/styles/color/{}.css'.format(current_dir, args.color), 'r') as f_color:
                content_all += f_color.read() + '\n'
        except:
            print('Bad argument passed to --color')
            sys.exit(1)

    if args.layout is not None:
        try:
            with open('{}/styles/layout/{}.css'.format(current_dir, args.layout), 'r') as f_layout:
                content_all += f_layout.read() + '\n'
        except:
            print('Bad argument passed to --layout')
            sys.exit(1)

    if args.typography is not None:
        try:
            with open('{}/styles/typography/{}.css'.format(current_dir, args.typography), 'r') as f_typography:
                content_all += f_typography.read() + '\n'
        except:
            print('Bad argument passed to --typography')
            sys.exit(1)

    write_to_css(content_all)
    print('Custom jupyter notebook theme created - refresh any open jupyter notebooks to apply theme.')


if __name__ == '__main__':
    run()
