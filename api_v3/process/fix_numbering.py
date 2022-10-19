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
        ref_array = re.split('(\n *[0-9]+)', questionlibrary.txt_output)
        original_array = re.split('(\n *[0-9]+)', questionlibrary.pandoc_output)

        logger.debug(f"ref length: {len(ref_array)} orig length: {len(original_array)}")
        # logger.debug("--------------") 
        # logger.debug(ref_array)
        # logger.debug("--------------")
        # logger.debug(original_array)
        # logger.debug("--------------") 

        if len(ref_array) != len(original_array):
            logger.debug(f"ref length and original length not equal")
            raise FixNumberingError("cannot compare reference with original because length not equal, some question(s) are possibly removed by pandoc")

        for idx, x in enumerate(ref_array):
            number_match_ref = re.search(r"^\n.*([0-9]+)$", x)

            if number_match_ref is not None:
                number_match_original = re.search(r"^\n.*([0-9]+)$", original_array[idx])
                if number_match_original is not None:
                    logger.debug(f"ref: {number_match_ref.group(1)} orig: {number_match_original.group(1)}")
                    if number_match_ref.group(1) != number_match_original.group(1):
                        logger.warn("mismatch found")
                        subbed = re.sub(r"[0-9]+", number_match_ref.group(1), original_array[idx])
                        original_array[idx] = subbed

        combined_string = ''.join(original_array)
        questionlibrary.pandoc_output = combined_string
        questionlibrary.save()

    except Exception as e:
        raise Exception(e)

class FixNumberingError(Exception):
    def __init__(self, reason, message="FixNumberingError"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.reason}'
