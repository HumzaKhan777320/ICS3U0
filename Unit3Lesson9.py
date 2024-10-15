def wc(TdegC, windKPH):#declaring a function that takes 2 parameters
   """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
   """
   vTemp = 0#creating variable to store the output(the wind chill)

   vTemp=13.12+0.6215*TdegC-11.37*(windKPH**0.16)+((0.3965*TdegC)*windKPH**0.16)#doing calculations based on the function's parameters and storing in vTemp

   return vTemp#returning the vTemp variable stored with calculations

def myfunc(vTemp):#declaring a function that takes 1 parameter for the risk statement 
  if(-10<vTemp<=0):#using an if statment to check for 1st level of risk
    return "Low risk"#returning coresponding statement
  if(-28<vTemp<=-10):#using an if statment to check for 2nd level of risk
    return "Moderate risk of hypothermia"#returning coresponding statement
  if(-40<vTemp<=-28):#using an if statment to check for 3rd level of risk
    return "High risk of frostbite"#returning coresponding statement
  if(-48<vTemp<=-40):#using an if statment to check for 4th level of risk
    return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"#returning coresponding statement
  if(-55<vTemp<=-48):#using an if statment to check for 5th level of risk
    return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"#returning coresponding statement
  if(vTemp<=-55):#using an if statment to check for 6th level of risk
    return "Extreme risk: exposed skin freezes in under 2 minutes"#returning coresponding statement

T = -5.0#setting a value of T
W = 10.0#setting a value of W
print("WC=%8.3f T=%8.3f W=%6.3f km/h. The risk is: %s" % (wc(T, W), T, W, myfunc(wc(T,W))))#printing the wind chill with given wind speed and temp through wc and using the wind chill to find the risk through myfunc
T = -20.0#setting a value of T
W = 20.0#setting a value of W
print("WC=%8.3f T=%8.3f W=%6.3f km/h. The risk is: %s" % (wc(T, W), T, W, myfunc(wc(T,W))))#printing the wind chill with given wind speed and temp through wc and using the wind chill to find the risk through myfunc
T = -45.0#setting a value of T
W = 40.0#setting a value of W
print("WC=%8.3f T=%8.3f W=%6.3f km/h. The risk is: %s" % (wc(T, W), T, W, myfunc(wc(T,W))))#printing the wind chill with given wind speed and temp through wc and using the wind chill to find the risk through myfunc
