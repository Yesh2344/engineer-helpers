import argparse

def main:
 parser = argparse.ArgumentParser
 parser.add_argument('--foo', help='foo help')
 args = parser.parse_args
 print(f'Foo: {args.foo}')