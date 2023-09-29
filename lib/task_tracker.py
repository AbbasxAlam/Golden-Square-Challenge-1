def task_tracker(text):
    '''
    parameters:
        string including #TODO
    returns:
        string saying whether text contains #TODO
    side effects:
        none
    '''
    if text == "":
        raise Exception("I need a string containing #TODO")
    elif "#TODO" not in text:
        return "Does not contain #TODO"
    return "Contains #TODO"
