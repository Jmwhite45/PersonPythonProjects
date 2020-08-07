
def cmToMile(cm):
    return cm/160934.4

def mileToCm(mile):
    return mile*160934.4

ModelSunRadius = 14/2
RealSunRadius = mileToCm(432170)

ModelPlanetRadius = 0# calcuateable value
RealPlanetRadius = mileToCm(2106.1) #mi

RealPlanetDistance = mileToCm(141.6*1000000) # miles (millions) 
ModelPlanetDistance = 0


Scale = RealSunRadius/ModelSunRadius #Model*scale = real thing, real/scale = model

ModelPlanetRadius=RealPlanetRadius/Scale #model radius=real radius/scale
ModelPlanetDistance=RealPlanetDistance/Scale #model radius=real radius/scale

print(f"Mar's Diameter: {(2*ModelPlanetRadius)/2.54} in")
print(f"orbit radius: {(ModelPlanetDistance/100)} m")