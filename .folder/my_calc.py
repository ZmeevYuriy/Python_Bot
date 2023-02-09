def calculator(mess):
    if len(mess) > 1:
        try:
            res = str(eval(mess))
        except Exception as e:
            res = "Error input!"
    else:
        res = "0"
    return res