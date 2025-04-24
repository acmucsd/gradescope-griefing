class Triton:
    def __init__(self):
        """
        initialize a triton
        args:
            none
        return:
            self
        """
        self.energy = 500
        self.knowledge = 0
        self.confidence = 0
        self.so = None # short for "significant other"
    
    def check(self):
        """
        return some info (do not modify)
        """
        return (self.energy, self.knowledge, self.confidence, self.so)
    
    def lock_in(self, hrs):
        """
        study for an upcoming exam: (gain 15 knowledge and lose 5 energy) per hour
        args:
            hrs: number of hours studied
        return:
            self
        """
        self.knowledge = ???
        self.energy = ???
        return self
        
    def crash_out(self):
        """
        undergo a mental breakdown: gain 30 energy but lose 30 knowledge and 30 confidence
        args:
            nothing
        return:
            self
        """
        self.energy = ???
        self.knowledge = ???
        self.confidence = ???
        return self
    
    def yolo(self):
        """
        take an exam
        args:
            nothing
        return:
            average of (current energy and knowledge), rounded down to nearest int
        """
        # hint: you can use // when dividing to automatically round down
        return ???
    
    def touch_grass(self, hrs):
        """
        exercise: (gain 20 confidence but lose 10 energy) per hour
        args:
            hrs: hours exercised
        return:
            self
        """
        self.energy = ???
        self.confidence = ???
        return self
        
    def doomscroll(self, hrs):
        """
        go on social media: (gain 5 energy but lose 10 confidence) per hour
        args:
            hrs: hours doomscrolled
        return:
            self
        """
        self.energy = ???
        self.confidence = ???
        return self
    
    def rizz(self, student):
        """
        attempt to start a relationship, succeeding if (you are both single) AND (your combined confidence is at least 100)
        args:
            student to make your significant other
        return:
            true if rizz successful
        """
        # a student is single if their significant other is not None - don't cheat :(
        # poly relationships are valid btw but i don't want to make this code too complicated
        return False
    
    def breakup(self):
        """
        dissolve a relationship, automatically crashing out in the process
        if you or your significant other are single, do nothing
        args:
            none
        return:
            true if breakup successful false otherwise
        """
        # be sure the breakup is mutual so neither of you have a significant other at end
        return False
        

            
