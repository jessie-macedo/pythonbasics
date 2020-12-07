class Fantasy:
    name = ""
    howmanydragons = 1
    isbecomingamovie = True
    howmanyprinces = 2
    howmanywarriors = 200
    explicitmagic = 0.80

    def description(self, isbecomingamovie):
        desc_fantasy = "%s has %s dragons, %s princes and %s warriors" % (self.name, self.howmanydragons, self.howmanyprinces, self.howmanywarriors)
        print(desc_fantasy)
        if isbecomingamovie:
            print("This novel os becoming a movie soon!")
    
newFantasy = Fantasy()
newFantasy.name = "Ode to Love and Thunder"
newFantasy.howmanydragons = 3
newFantasy.description(True)