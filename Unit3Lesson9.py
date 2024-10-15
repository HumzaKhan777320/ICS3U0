#Not done yet
def wc(TdegC, windKPH):
   """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
   """
   vTemp = 0

   vTemp=13.12+0.6215*TdegC-11.37*(windKPH**0.16)+((0.3965*TdegC)*windKPH**0.16)

   return vTemp

def myfunc(vTemp):
  if(-9<=vTemp<=0):
    return "Low risk"
  if(-27<=vTemp<=-10):
    return "Moderate risk of hypothermia"
  if(-39<=vTemp<=-28):
    return "High risk of frostbite"
  if(-47<=vTemp<=-40):
    return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
  if(-54<=vTemp<=-48):
    return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
  if(vTemp<=-55):
    return "Extreme risk: exposed skin freezes in under 2 minutes"

T = -5.0
W = 10.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h. The risk is: %s" % (wc(T, W), T, W, myfunc(wc(T,W))))
T = -20.0
W = 20.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h. The risk is: %s" % (wc(T, W), T, W, myfunc(wc(T,W))))
T = -45.0
W = 40.0
print("WC=%8.3f T=%8.3f W=%6.3f km/h. The risk is: %s" % (wc(T, W), T, W, myfunc(wc(T,W))))
