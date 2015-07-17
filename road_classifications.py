road_layer = iface.activeLayer()
iter = road_layer.getFeatures()
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
    