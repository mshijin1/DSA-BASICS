def highest_frequency_element(arr):
    frequency_dict={}
    max_frequency=0
    max_frequency_element=None
    
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] +=1
            if frequency_dict[element] > max_frequency:
                max_frequency = frequency_dict[element]
                max_frequency_element = element
            
        else:
            frequency_dict[element] =1
    return frequency_dict, max_frequency_element, max_frequency

arr=[1,1,2,3,4,4,4,5,5,6,7,8,8,8]
result, max_frequency_element, max_frequency=highest_frequency_element(arr)
print("arr", result, "element", max_frequency_element, "frequency", max_frequency)