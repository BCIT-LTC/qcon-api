# TODO
def HandlerQuestionError(self, question, errortype, error_message, action):
    try:    
        # from api_v2.models import ErrorType
        # error_type = ErrorType.objects.get(errortype=errortype)
        # from api_v2.models import QuestionError
        # new_error = QuestionError(question=question, errortype=error_type, message=error_message, action=action)
        # new_error.save()
        
        from api_v2.models import QuestionError
        new_error = QuestionError(question=question, errortype=errortype, message=error_message, action=action)
        new_error.save()

    except:
        pass

    return None