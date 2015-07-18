road_layer = iface.activeLayer()
iter = road_layer.getFeatures() #guessing this creates a dictionary, see: http://stackoverflow.com/questions/14507591/python-dictionary-comprehension
#so filter the "iter" dictionary by one or both of the big_roads or seperated_highways
#in a list it would look something like this
#iter = someListReturningFunction
#def isBigRoad(x):
#   
#or better yet iter = (x for x in someListReturningFunction if x in big_roads)
#making your iter a generator expression using parentheses saves on ram
#generators are super powerful
#I think combining the idea of list/dictionary comprehensions and generators will aid you in speed
#that way instead of an iterative if else aproach you're making this a script that is more of the 
#functional programming type and they tend to be faster
#also, I've got it on anectodal evidence that printing is slow, you might try taking out the print statements until 
#at the end
#so again, to recap, the functional approach basically has you applying filters to arrays or other data 
#as many times as needed until you get your working set just right and then iterate - your working set is then much smaller
big_roads = ['3', '5', '6', '8', '9', '10']
seperated_highways = ['1', '2', '4']
for feature in iter:
    fid = feature.id()
    carto_id = feature.fieldNameIndex('NewCarto')
    print fid
    if feature.attribute('CARTOCODE') in seperated_highways:
        edits = {carto_id : '1'}
        road_layer.dataProvider().changeAttributeValues({fid: edits})
        print edits
    elif feature.attribute('CARTOCODE') == '7':
        edits = {carto_id : '2'}
        road_layer.dataProvider().changeAttributeValues({fid: edits})
        print edits
    elif feature.attribute('CARTOCODE') in big_roads:
        edits = {carto_id : '3'}
        road_layer.dataProvider().changeAttributeValues({fid: edits})
        print edits
    elif feature.attribute('CARTOCODE') == '11':
        edits = {carto_id : '4'}
        road_layer.dataProvider().changeAttributeValues({fid: edits})
        print edits
    else:
        edits = {carto_id : '5'}
        road_layer.dataProvider().changeAttributeValues({fid: edits})
        print edits
    
