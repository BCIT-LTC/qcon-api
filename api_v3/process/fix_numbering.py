import re
import os
import subprocess

from pathlib import Path

import logging
newlogger = logging.getLogger(__name__)
# from api_v3.logging.contextfilter import QuestionlibraryFilenameFilter
from api_v3.logging.logging_adapter import FilenameLoggingAdapter

def fix_numbering(questionlibrary):

    logger = FilenameLoggingAdapter(newlogger, {
        'filename': questionlibrary.temp_file.name,
        'user_ip': questionlibrary.user_ip
        })

    try:
        ref_array = re.split(r"(\n *[0-9]+\\?[)|.])", questionlibrary.txt_output)
        pandoc_array = re.split(r"(\n *[0-9]+\\?[)|.])", questionlibrary.pandoc_output)

        logger.debug(f"ref_array length: {len(ref_array)} pandoc_array length: {len(pandoc_array)}")
        logger.debug("--------------") 
        logger.debug(ref_array)
        logger.debug("--------------")
        logger.debug(pandoc_array)
        logger.debug("--------------") 

        if len(ref_array) != len(pandoc_array):
            logger.debug(f"ref_array length and pandoc_array length not equal")
            raise FixNumberingError("cannot compare reference with original because length not equal, some question(s) are possibly removed by pandoc")

        for idx, x in enumerate(ref_array):
            number_match_ref = re.search(r"^\n.*([0-9]+)$", x)

            if number_match_ref is not None:
                number_match_original = re.search(r"^\n.*([0-9]+)$", pandoc_array[idx])
                if number_match_original is not None:
                    logger.debug(f"ref: {number_match_ref.group(1)} pandoc: {number_match_original.group(1)}")
                    if number_match_ref.group(1) != number_match_original.group(1):
                        logger.warn(f"mismatch found [ref]:[pandoc]-[{number_match_ref.group(1)}:{number_match_original.group(1)}]")
                        subbed = re.sub(r"[0-9]+", number_match_ref.group(1), pandoc_array[idx])
                        pandoc_array[idx] = subbed
                        logger.info(f"mismatch fixed [ref]:[pandoc]-[{number_match_ref.group(1)}:{number_match_original.group(1)}]->[{number_match_ref.group(1)}:{number_match_ref.group(1)}]")

        # logger.debug(pandoc_array)
        combined_string = ''.join(pandoc_array)
        questionlibrary.pandoc_output = combined_string
        questionlibrary.save()

    except Exception as e:
        raise Exception(e)

class FixNumberingError(Exception):
    def __init__(self, reason, message="FixNumberingError"):
        self.reason = reason
        self.message = message

    def __str__(self):
        return f'{self.message} -> {self.reason}'
