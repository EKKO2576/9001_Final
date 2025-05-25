class Creature:


    def __init__(self, nickname):
        self.nickname = nickname
        self.clean = "medium"
        self.energy = "medium"
        self.interaction = "low"
        self.appearance = "medium"
        self.alive = True
        self.danger_rounds = 0 # Continuous critical rounds

    def bathe(self):
        """Bathing improves cleanliness and interaction"""
        self.clean = "high"
        self.interaction = "medium"
        print(f"{self.nickname} is now clean. (Clean -> high, Interaction -> medium)")

    def rest(self):
        """Resting restores energy"""
        self.energy = "high"
        print(f"{self.nickname} has rested. (Energy -> high)")

    def decorate(self):
        """Decorating improves appearance and interaction"""
        self.appearance = "high"
        self.interaction = "high"
        print(f"{self.nickname}'s appearance has been improved. (Appearance -> high, Interaction -> high)")

    def talk(self):
        """Talking gradually improves interaction"""
        if self.interaction == "low":
            self.interaction = "medium"
        elif self.interaction == "medium":
            self.interaction = "high"
        print(f"You talked to {self.nickname}. (Interaction level increased)")

    def decay(self):
        """Daily decay of attributes"""
        self.clean = self._lower(self.clean)
        self.energy = self._lower(self.energy)
        self.interaction = self._lower(self.interaction)
        self.appearance = self._lower(self.appearance)

    def _lower(self, state):
        """Rule for lowering state"""
        if state == "high":
            return "medium"
        elif state == "medium":
            return "low"
        else:
            return "low"

    def check_condition(self):
        """Check if pet should die"""
        if self.energy == "low" and self.interaction == "low":
            self.danger_rounds += 1
            if self.danger_rounds == 2:
                print("Warning: Your pet has low energy and low interaction.")
            elif self.danger_rounds == 3:
                print("Critical: If this continues, your pet may not survive.")
            elif self.danger_rounds >= 4:
                print(f"{self.nickname} could not survive the prolonged neglect.")
                self.alive = False
        else:
            self.danger_rounds = 0  #Reset danger counter

    def show_status(self):
        """Display current state levels"""
        print(f"\nStatus of {self.nickname}:")
        print(f"  Cleanliness   : {self.clean}")
        print(f"  Energy        : {self.energy}")
        print(f"  Interaction   : {self.interaction}")
        print(f"  Appearance    : {self.appearance}")
