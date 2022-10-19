import logging

class FilenameLoggingAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def process(self, msg, kwargs):
        user_ip = ""
        filename = ""
        question = ""

        if 'user_ip' in self.extra:
            user_ip = self.extra['user_ip']
        
        if 'filename' in self.extra:
            filename = self.extra['filename']
        
        if 'question' in self.extra:
            question = self.extra['question']

        return f"{user_ip}:[{filename}]:{question} {msg}", kwargs
