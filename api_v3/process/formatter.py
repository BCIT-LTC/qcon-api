import os
import xml.etree.ElementTree as ET
import subprocess
import logging
logger = logging.getLogger(__name__)

def run_formatter(questionlibrary):
    os.chdir('/formatter/jarfile')
    result = subprocess.run('java -cp formatter.jar:* formatter',
                            shell=True,
                            input=questionlibrary.pandoc_output.encode(),
                            capture_output=True)
    os.chdir('/code')
    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        # raise FormatterError("Not valid")
        logger.error("File Not valid")
        return

    try:
        if root[0].tag == "body":
            questionlibrary.formatter_output = root[0].text
            questionlibrary.save()
            pass
        else:
            logger.error("Body not found")
            # raise FormatterError("Body not found")
            return
    except:
        logger.error("Body not found")
        # raise FormatterError("Body not found")
        return
    try:
        if root[1].tag == "end_answers":
            questionlibrary.end_answers_raw = root[1].text
            questionlibrary.save()
        else:
            # logger.warning("Answer Section not found")
            pass
    except:
        # logger.warning("Answer section not found")
        pass