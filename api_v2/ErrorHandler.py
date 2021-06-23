# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

def HandleQuestionError(question, errortype, error_message, action):
    try:    
       
        from api_v2.models import QuestionError
        new_error = QuestionError(question=question, errortype=errortype, message=error_message, action=action)
        new_error.save()

    except:
        pass

    return None

def HandleDocumentError(document, errortype, error_message, action):
    try:    

        from api_v2.models import DocumentError
        new_error = DocumentError(document=document, errortype=errortype, message=error_message, action=action)
        new_error.save()

    except:
        pass

    return None