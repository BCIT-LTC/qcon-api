class L1Element:
    def __init__(self):
        self.prefix = ""
        self.content = ""
        self.starmarked = False
        self.listseparator = False
        self.questionseparator = False
        self.answerblockseparator = False
        self.indentlength = 0

    def __str__(self):
        # return "PREFIX: " + str(self.prefix) + " CONTENT:" + str(self.content) + " CORRECT:" + str(self.starmarked) + " SEPARATOR:" + str(self.questionseparator)
        return "PREFIX: " + str(self.prefix) +" SEPARATOR:" + str(self.questionseparator) + " ANSWERBLOCK:" + str(self.answerblockseparator) + " LISTSEP:" + str(self.listseparator)
