import simplekml
kml = simplekml.Kml()
ground = kml.newgroundoverlay(name='GroundOverlay')
ground.icon.href = 'http://simplekml.googlecode.com/hg/samples/resources/smile.png'
ground.gxlatlonquad.coords = [(18.410524,-33.903972),(18.411429,-33.904171),
                              (18.411757,-33.902944),(18.410850,-33.902767)]
# or
#ground.latlonbox.north = -33.902828
#ground.latlonbox.south = -33.904104
#ground.latlonbox.east =  18.410684
#ground.latlonbox.west =  18.411633
#ground.latlonbox.rotation = -14
kml.save("GroundOverlay.kml")