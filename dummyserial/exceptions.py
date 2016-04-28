#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dummy Serial Exceptions."""

__author__ = 'Greg Albrecht <gba@orionlabs.io>'
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'


class DSIOError(IOError):
    pass


class DSTypeError(TypeError):
    pass
