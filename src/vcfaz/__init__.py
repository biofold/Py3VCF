#!/usr/bin/env python
"""
A VCFv4.0 and 4.1 parser for Python.

Online version of PyVCF documentation is available at http://pyvcf.rtfd.org/
"""


from .parser import Reader, Writer
from .parser import VCFReader, VCFWriter
from .filters import Base as Filter
from .parser import RESERVED_INFO, RESERVED_FORMAT
from .sample_filter import SampleFilter

VERSION = '0.6.8'
