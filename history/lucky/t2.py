import simplekml
kml = simplekml.Kml()
pol = kml.newpolygon(name="Atrium Garden",
             outerboundaryis=[(18.43348,-33.98985),(18.43387,-33.99004),(18.43410,-33.98972),
                              (18.43371,-33.98952),(18.43348,-33.98985)],
             innerboundaryis=[(18.43360,-33.98982),(18.43386,-33.98995),(18.43401,-33.98974),
                              (18.43376,-33.98962),(18.43360,-33.98982)])



res = simplekml.Color.rgb(12, 180, 83)
# pol.style.polystyle.color = simplekml.Color.red
pol.style.polystyle.color = 'red'
pol.style.polystyle.outline = 0
kml.save("PolyStyle.kml")
print(res)

