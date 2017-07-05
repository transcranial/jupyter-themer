from __future__ import print_function

import argparse
import glob
import notebook
import os
import sys


current_dir = os.path.dirname(os.path.realpath(__file__))
notebook_dir = os.path.dirname(notebook.__file__)
custom_css_filepath = notebook_dir + '/static/custom/custom.css'


def write_to_css(content, css_path):
    try:
        with open(css_path, 'w+') as f:
            f.write(content)
    except:
        print('Error writing to custom.css')
        sys.exit(1)


def run(args=None):
    if args is None:
        parser = argparse.ArgumentParser(description='Jupyter notebook themer.')
        parser.add_argument('-c', '--color', required=False, dest='color', default=None, help='color style')
        parser.add_argument('-l', '--layout', required=False, dest='layout', default=None, help='layout style')
        parser.add_argument('-t', '--typography', required=False, dest='typography',
                            default=None, help='typography style')
        parser.add_argument('-f', '--font', required=False, dest='font', default=None, help='code font family')
        parser.add_argument('-b', '--background', required=False, dest='background',
                            default=None, help='background theme styling')
        parser.add_argument('-s', '--show', required=False, dest='show',
                            default=None, help='show available choices')
        parser.add_argument('-p', '--css_path', required=False, dest='css_path',
                            default=custom_css_filepath, help='custom css path.(default:%s)' % custom_css_filepath)
        args = parser.parse_args()

    if (args.color is None
            and args.layout is None
            and args.typography is None
            and args.font is None
            and args.background is None
            and args.show is None):
        print('Jupyter notebook reverted to default style.')
        write_to_css('', args.css_path)
        sys.exit()

    if args.show in ['color', 'layout', 'typography', 'font', 'background']:
        if args.show == 'font':
            args.show = 'code_font'
        options = glob.glob('{}/styles/{}/*.css'.format(current_dir, args.show))
        for option in sorted(options):
            print(os.path.basename(option).split('.')[0])
        sys.exit()

    content_all = ''

    if args.typography is not None:
        try:
            with open('{}/styles/typography/{}.import'.format(current_dir, args.typography), 'r') as f_color:
                content_all += f_color.read() + '\n'
        except:
            print('Bad argument passed to --typography')
            sys.exit(1)

    if args.font is not None:
        try:
            with open('{}/styles/code_font/{}.import'.format(current_dir, args.font), 'r') as f_font:
                content_all += f_font.read() + '\n'
        except:
            print('Bad argument passed to --font')
            sys.exit(1)

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

    if args.font is not None:
        try:
            with open('{}/styles/code_font/{}.css'.format(current_dir, args.font), 'r') as f_font:
                content_all += f_font.read() + '\n'
        except:
            print('Bad argument passed to --font')
            sys.exit(1)

    if args.background is not None:
        try:
            with open('{}/styles/background/{}.css'.format(current_dir, args.background), 'r') as f_background:
                content_all += f_background.read() + '\n'
        except:
            print('Bad argument passed to --background')
            sys.exit(1)

    write_to_css(content_all, args.css_path)
    print('Custom jupyter notebook theme created - refresh any open jupyter notebooks to apply theme.')


if __name__ == '__main__':
    run()
