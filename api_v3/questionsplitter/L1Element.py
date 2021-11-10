# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

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
        self.wr_answertoken = False
        self.endanswers = False
        # self.indentlength = 0 # Not being used

    def __str__(self):
        # return "PREFIX: " + str(self.prefix) + " CONTENT:" + str(self.content) + " CORRECT:" + str(self.starmarked) + " SEPARATOR:" + str(self.questionseparator)
        return "PREFIX: " + str(self.prefix) +" SEPARATOR:" + str(self.questionseparator) + " ANSWERBLOCK:" + str(self.answerblockseparator) + " LISTITEM:" + str(self.listitem)
