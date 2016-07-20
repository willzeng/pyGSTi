#!/usr/bin/env python
from .lintAll           import lint_all
from ..automation_tools import read_yaml, write_yaml


def get_score():
    lintResult = lint_all()
    scoreLine  = lintResult[-2]
    # Score is located between leftmost slash and then rightmost space:
    # -> Your code has been rated at 9.57/10 (previous run: 9.57/10, +0.00) 
    #                                    ^
    # -> Your code has been rated at 9.57
    #                               ^
    # -> 9.57
    score      = scoreLine.split('/', 1)[0].rsplit(' ', 1)[1]
    return score
    
