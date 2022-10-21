class MCEndAnswerExistWarning(Exception):
    def __init__(self, reason, message="MCEndAnswerExistWarning"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'

class MSEndAnswerExistWarning(Exception):
    def __init__(self, reason, message="MSEndAnswerExistWarning"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'

class WREndAnswerExistWarning(Exception):
    def __init__(self, reason, message="WREndAnswerExistWarning"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'
