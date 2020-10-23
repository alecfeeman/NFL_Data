#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
code to scrape the most recent weeks data, this can be run in a batch job weekly.

-----------------------------------------------------------------------------
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Alec Feeman"
__copyright__ = "Copyright 2020, Alec Feeman"
__credits__ = ["Alec Feeman"]
__license__ = "GPLv3"
__version__ = "v0.1.0-alpha"
__date__ = "10/22/2020"
__maintainer__ = "Alec Feeman"
__email__ = "afeeman@icloud.com"
__status__ = "Development"

import logging
import data_scraping.scrape_nfl as scrape_nfl
import data_scraping.etl as etl

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}


def configure_logging( file_level, console_level, filepath):
    logger = logging.getLogger(__name__)
    logger.setLevel(file_level)
    formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
    # create a file handler
    fh = logging.FileHandler(filepath)
    fh.setFormatter(formatter)
    # fh.setLevel(file_level)
    logger.addHandler(fh)
    # create a stream handler for the console
    # ch = logging.StreamHandler()
    # ch.setLevel(console_level)
    # ch.setFormatter(formatter)
    # logger.addHandler(ch)
    return logger


def main():

    # get draft data

    # get combine data

    # update coaches

    # update players


    pass


if __name__ == "__main__":
    main()
