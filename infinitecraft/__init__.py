"""
An API Wrapper for Neal's Infinite Craft game in Python.
Copyright (C) 2024-present SqdNoises, Neal Agarwal
License: MIT License
To view the full license, visit https://github.com/sqdnoises/infinite-craft#license

Need help with something?
Join our Discord server -> https://discord.gg/EPr4T2F8bq

Play Infinite Craft by Neal Agarwal on your browser -> https://neal.fun/infinite-craft/
"""

__title__ = "infinite-craft"
__full_title__ = "Infinite Craft"
__description__ = "An API Wrapper for Neal's Infinite Craft game in Python."
__cli_description__ = "Infinite Craft Utilities"
__author__ = "SqdNoises"
__license__ = "MIT License"
__copyright__ = "Copyright (C) 2024-present SqdNoises, Neal Agarwal"
__github__ = "https://github.com/sqdnoises/infinite-craft"
__discord__ = "https://discord.gg/EPr4T2F8bq"
__version__ = "1.1.5"
__display_version__ = __title__ + " " + __version__

from .element       import *
from .infinitecraft import *
from .logger        import *
from .errors        import *