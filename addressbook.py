import pickle, cwd

class Contact:
    """Represents a persons contact.
    
    Attributes: name, phone_no, email.
    """
    def __init__(self, name, number, email=None):
        """Initialize instance fields."""
        self.__name = name
        self.__phone_no = number
        self.__email = email
    
    def __str__(self):
        return """\
Name: {0}
Phone Number: {1}
Email: {2}
""".format(self.__name, self.__phone_no, self.__email)
        
    def get_name(self):
        return self.__name
        
    def get_email(self):
        return self.__email
        
    def get_phonenumber(self):
        return self.__phone_no
        
    def set_name(self, name):
        self.__name = name
        
    def set_email(self, email):
        self.__email = email
        
    def set_phone(self, phone_no):
        self.__phone_no = phone_no
        
    
class AddressBook(dict):
    """Representing address book.
    
    Attributes: add, delete, exit, modify, search, save.
    """   
    def __init__(self):
        """Initialize instance."""
        dict.__init__(self)
        self.__ab_open()
        
    def __ab_open(self, filename="Address-book.data"):
        """Retrieve address book from file(if any).
        
        Updates/merges instance with retrieved address book.
        
        filename: string
        """
        try:
            with open(filename, "rb") as f:
                # try loading(if any) address-book from file
                try:
                    ab = pickle.load(f)
                except EOFError:
                    pass
                else:
                    self.update(ab)    
        except FileNotFoundErrorwith open(filename, "wb") as f:
            
                      
    def add(self):
        """Add contact to Address Book."""
        name = input("Enter Fullname: \n")
        number = input("Enter Phone no.: \n")
        email = input("Enter Email: \n")
        # create contact
        contact = Contact(name, number, email)
        key = contact.get_name()
        if key in self:
            print("contact already exists")
            print()
            return
        self[key] = contact
        self.save()
        print()
        
    def browse(self):    
        """Browse contacts in address book."""
        if len(self) == 0:
            print("Empty Address-book")
            return
                       
        for name in self:
            cont = self[name]
            print(cont)
        
    def delete(self, name):
        """Delete contact with given name from address book.
        
        name: string.
        """               
        try:
            del self[name]
        except KeyError:
            print("contact does not exist.")
        else:            
            print("contact deleted")
            self.save()
                    
    def exit(self):
        print("Exiting Address Book")
        
    def modify(self, name, d):
        """Modify contact in address book.
        Edit contact with given name using field-value pair from kwargs.
        
        d: dictionary of field-value pair items.
        """
        if name in self:
            contact = self[name]
            for field, value in d.items():
                if field.lower() == "name":
                    contact.set_name(value)
                if field.lower() == "email":
                    contact.set_email(value)
                else:
                    contact.set_phone(value)
                
            self.save()
        else:
            print("contact does not exist")
                     
    def search(self, name):
        """Search address book for contact with given name.
        
        Returns contact if found or "Not Found" if otherwise.
        
        name: string.
        """   
        found = self.get(name, "Not found") 
        print(found)
        return found          
        
    def save(self):
        """Save address book.
        
        Dumps the address book in "Address-book.data" file.
        """
        with open("Address-book.data", "wb") as f: 
            pickle.dump(self, f)
            print("contact saved") 
  

def main():
    address_book = AddressBook()
    op_map = {
        "a": address_book.add, 
        "b": address_book.browse,
        "d": address_book.delete, 
        "m": address_book.modify,
        "s": address_book.save,
        "f": address_book.search,
        "z": address_book.exit
    }
              
    def run():  
        print()
        print("Add new contact(a)")
        print("Browse Address Book(b)")
        print("Delete contact(d contact-name)")
        print("Modify contact(m contact-name dictionary of fields)")
        print("Save contact(s)")
        print("Search contact(f contact-name)")
        print("To exit(z)")
        print()
        inp = input("Enter option --> ")
        print()
        
        op = inp[0].lower()
        # exiting / terminating run()
        if op == "z":
            op_map[op]()
            return 
        # fetch extra arg from input
        # for search and delete methods
        if op == "f" or op == "d":
            arg = inp[2:]
            op_map[op](arg)
            run()
        if op == "m":
            args = inp[2:].split(" ")
            op_map[op](args[0], eval(args[1]))
            run()
        else:
            op_map[op]()
            run()
            
    
    print()        
    title = "\tSimple Address Book"
    print(title)
    print("\t", "- "*(len(title)//2), sep="")
    run()
    

    
__version__ = "0.0.1"

  
if __name__ == "__main__":
    main()   
