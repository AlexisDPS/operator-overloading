class Contact():
    def __init__(self, fn, ln, ph, addr, city, zip):
        # pass in the contact’s information and assign each one to its corresponding attribute.
        self.first_name = fn
        self.last_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        # passes in two contacts and returns a boolean value. 
        # Compare by last names alphabetically, if they are the same, then compare by first names.
        #  This method will automatically be called when you sort your list of contacts.
        if self.last_name != other.last_name:
            return self.last_name < other.last_name
        else:
            return self.first_name < other.first_name

    def __str__(self):
        # returns a string that is used to display the contact to the console.
        return f"{self.first_name} {self.last_name}\n{self.phone}\n{self.address}\n{self.city} {self.zip}"

    def __repr__(self):
        # returns a string that is used to write the contact to the file in the format ‘f_name,l_name,phone,address,city,zip’.
        return f"{self.first_name},{self.last_name},{self.phone},{self.address},{self.city},{self.zip}"
    