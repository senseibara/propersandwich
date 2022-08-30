# -*- coding: utf-8 -*-

from .context import boilerplate_python

import pytest


def test_thoughts():
    assert (boilerplate_python.hmm()) is None
