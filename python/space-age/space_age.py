class SpaceAge(object):
    seconds = 0
    eareth_day_seconds = 31557600
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_mercury(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/0.2408467, 2)
    
    def on_venus(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/0.61519726, 2)
    
    def on_earth(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds), 2)
    
    def on_mars(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/1.8808158, 2)
    
    def on_jupiter(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/11.862615, 2)
    
    def on_saturn(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/29.447498, 2)
    
    def on_uranus(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/84.016846, 2)
    
    def on_neptune(self):
        return round(float(self.seconds)/float(self.eareth_day_seconds)/164.79132, 2)
