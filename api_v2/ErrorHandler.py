def HandleQuestionError(self, question, errortype, error_message, action):
    try:    
       
        from api_v2.models import QuestionError
        new_error = QuestionError(question=question, errortype=errortype, message=error_message, action=action)
        new_error.save()

    except:
        pass

    return None

def HandleDocumentError(self, document, errortype, error_message, action):
    try:    

        from api_v2.models import DocumentError
        new_error = DocumentError(document=document, errortype=errortype, message=error_message, action=action)
        new_error.save()

    except:
        pass

    return None