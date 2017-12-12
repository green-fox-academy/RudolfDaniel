class Aircraft(object):
    def __init__(self, max_ammo, base_damage):
        self.ammo = 0
        self.max_ammo = max_ammo
        self.base_damage = base_damage

    def fight(self):
        damage = (self.base_damage * self.ammo)
        self.ammo = 0
        return damage

    def refill(self, filled_ammo):
        remaining_ammo = 0
        if filled_ammo > self.max_ammo:
            remaining_ammo += (filled_ammo - self.max_ammo)
            self.ammo = self.max_ammo
        else:
            self.ammo = filled_ammo
        return remaining_ammo

    def getType(self):
        pass

    def getStatus(self):
        pass