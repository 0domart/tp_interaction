class Fustrum(object):
    def __init__(self,r,parent):
        self.radius=r
        self.perception_range=100
        self.parent=parent
        self.perceptionList=[]

    def vision(self,obj):
        if hasattr(obj,'position'):
            if hasattr(obj,"mass"):
                if obj.position.distance_to(self.parent.position) < self.perception_range+obj.mass:
                    return True
        return False
