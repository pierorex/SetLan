#! /usr/bin/env python
# -*- coding: utf-8 -*-

import ply.lex as lex,parser
import lexer, parser, sys

def main(arg):
    print (str(parser.mainParser(sys.argv[1])))
