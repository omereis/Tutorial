class Resturant (object):
    bankrupt = False
    def open_branch (self):
        if not self.bankrupt:
            print ("branch opened")

print ("Hello, Python!")
x = Resturant()

