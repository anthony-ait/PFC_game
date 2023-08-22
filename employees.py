import random


#main class of character
class Character():
    def __init__(self, name):
        self.name = name
        self.active = True

class Manager(Character):
    def __init__(self, name):
        super().__init__(name)
        self.talents = {}

    def learn_talent(self, talent):
        if talent.name in self.talents:
            print('Talent already learnt')
        if talent.parent_talent in self.talents or talent.parent_talent == None:
            #create dict from talent but without name
            temp_dict = talent.__dict__.copy()
            del temp_dict['name']
            #add to talent 
            self.talents [talent.name] = temp_dict
        else:
            print('Need to learn', talent.name)


        

class Worker(Character):
    def __init__(self, name, shift):
        super().__init__(name)
        self.shift = shift
        self.skills = {}
        #define base value for task metrics
        self.assign_base_skills()
        self.old = 0
        self.happiness = random.randint(25, 50)
        self.day_in_row = random.randint(0,20)
        self.resistance = random.randint(30, 45) 

    #learn new skills
    def learn_skill(self, skill):
        self.skills [skill.name] = skill.value

    #add base skills to every character
    def assign_base_skills(self):
        #define base skill
        sorting = Skill("sorting", random.randint(0,2))
        loading = Skill("loading", random.randint(0,2))

        #assign base skill
        self.learn_skill(sorting)
        self.learn_skill(loading)


    #at end of each day we update data about worker
    def update(self):
        #if worker active, then add 1 day of work
        if self.active:
            self.day_in_row +=1
        #update happiness value
        if self.day_in_row > self.resistance :
            #add chance for player to don't loose happiness
            if random.random() > 0.5:
                self.happiness -= 2 ** (self.day_in_row - self.resistance)
        #if happiness less than zero, then worker leave company
        if self.happiness <= 0:
            self.active = False
        

class Skill():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Talent():
    def __init__(self, name, parent_talent = None):
        self.name = name
        self.parent_talent = parent_talent
        self.level = 0

class Improving_Talent(Talent):
    def __init__(self, name, value, parent_talent):
        super().__init__(name, value, parent_talent)
        self.max_lvl = 3


talent1 = Talent('talent1')

talent11 = Talent('talent11', 'talent1')

talent2 = Talent('talent2')

Jimmy = Manager('Jimmy')
print(Jimmy.__dict__)

#Jimmy.learn_talent(talent11)

Jimmy.learn_talent(talent1)
Jimmy.learn_talent(talent11)

#Jimmy.learn_talent(talent11)
print(Jimmy.__dict__)

print(Jimmy.talents)


















