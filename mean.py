def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail:
        msg = 'The algebraic mean of an empty list is undefinied.'
        raise ZeroDivisionError(detail.__str__() + '\n', msg)
    except TypeError:
        raise ValueError('num_list has to be numerical')
