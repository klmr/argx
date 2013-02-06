#!/usr/bin/env python

import argparse

def default_arg(default):
    """
    Create an action for optional arguments which provides two defaults.

    Use as argument `action` to the argparse.ArgumentParser.add_argument` method.
    This defines a command line argument which, in addition to its normal default,
    has an additional default value which is taken when this optional argument is
    present, but has no value. For instance:

        >>> parser = argparse.ArgumentParser()
        >>> parser.add_argument('--s', default = 'a', nargs = '?', action = default_arg('b'))
        >>> parser.parse_args([])
        Namespace(s='a')
        >>> parser.parse_args(['--s'])
        Namespace(s='b')
        >>> parser.parse_args(['--s', 'c'])
        Namespace(s='c')
    """
    class DefaultArg(argparse.Action):
        def __call__(self, parser, namespace, value, option_string):
            if value is None:
                setattr(namespace, self.dest, default)
            else:
                setattr(namespace, self.dest, value)

    return DefaultArg
