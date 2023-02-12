variable='a'
# a b c
printable=''
layer_count=5

# if variable=='a':
printable=''
for i in range(0,8):
#         0 1 2 3 4
    print(printable)
    printable= printable+'x'
#         'x' + 'x' = 'xx'
# if variable =='b':
    
# # # # # # # # # # # # # # # # # # # # # #     

for searched_layer in range(1,15):
    layer_count=14
#     searched_layer=4
    result=" " * (layer_count-searched_layer) + 'x'*searched_layer
    #                 14-4
    print(result)

#
    
    
# layer_count=5
# searched_layer=4
# result=" " * (layer_count-searched_layer) + 'x '*searched_layer
# print(result)

layer_count=5    
for searched_layer in range(0,layer_count):   
#     searched_layer=4
    result=" " * (layer_count-searched_layer) + 'x '*searched_layer
    print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    