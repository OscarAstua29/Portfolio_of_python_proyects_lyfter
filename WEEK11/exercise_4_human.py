class Head: 
    head = "head"

class Torso:
    def __init__(self,head,right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        

class Arm:
    def __init__(self,hand):
        self.hand = hand

class Hand:
    hand = "hand"

class Leg:
    def __init__(self,foot):
        self.foot = foot

class Foot:
    Foot = "Foot"

class Human:
    def __init__(self, torse):
     self.torso = torso

head = Head()
right_hand = Hand()
left_hand = Hand() 
right_foot = Foot()
left_foot = Foot()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_leg = Leg(right_foot)
left_leg = Leg(left_foot)
torso = Torso(head,right_arm, left_arm, right_leg, left_leg)
human = Human(torso)

print(human.torso)