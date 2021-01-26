class L1Element:
    def __init__(self):
        self.prefix = ""
        self.content = ""
        self.starmarked = False
        self.listitem = False
        self.questionseparator = False # this one is set by the splitter
        self.answerblockseparator = False # this one is set by the splitter
        self.questionheader = False
        self.sectionheader = False
        self.endanswers = False
        # self.indentlength = 0 # Not being used

    def __str__(self):
        # return "PREFIX: " + str(self.prefix) + " CONTENT:" + str(self.content) + " CORRECT:" + str(self.starmarked) + " SEPARATOR:" + str(self.questionseparator)
        return "PREFIX: " + str(self.prefix) +" SEPARATOR:" + str(self.questionseparator) + " ANSWERBLOCK:" + str(self.answerblockseparator) + " LISTITEM:" + str(self.listitem)
