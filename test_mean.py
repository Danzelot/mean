from mean import mean

def test_ints():
    num_list = [1,2,3,4,5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp
    
# when there is 0 in the list
def test_zero_in_list():
    num_list = [3,4,0,5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp
    
# when the results is a double
def test_double_as_result():
    num_list = [3,4,5]
    obs = mean(num_list)
    exp = 4
    assert exp - 0.0001 < obs < exp + 0.0001 
    
# when the results is a really large number
def test_large_result():
    num_list = [3E7,4E7,5E7]
    obs = mean(num_list)
    exp = 4E7
    assert exp - 0.0001E7 < obs < exp + 0.0001E7
    
# when the elements are doubles\, not integeres
def test_double_as_input():
    num_list = [3.0,4.0,5]
    obs = mean(num_list)
    exp = 4
    assert exp - 0.0001 < obs < exp + 0.0001 
    
    
# test_ints()
# test_zero_in_list()
# test_double_as_result()
# test_large_result()
# test_double_as_input()
