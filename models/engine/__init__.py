#!/usr/bib/python3
"""
This is a package that contains the engine module for data storage.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
