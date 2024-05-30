from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key= None
        self.password_file= None
        self.password_dict= {}

    
    def write_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, "wb") as file:
            file.write(self.key)
    
    def load_key(self, path):
        with open(path, "rb") as file:
            self.key = file.read()
        
    def create_file(self, path, initial_values= None):
        self.password_file = path

        if initial_values != None:
            for key, value in initial_values.items():
                self.add_password(key, value)
    
    def load_file(self, path):
        self.password_file = path

        with open(path, "r") as file:
            for line in file:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file != None:
            with open(self.password_file, "a+") as file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                file.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict.get(site, "Password not found.")


def main():

    pm= PasswordManager()

    my_key= "mykey.key"
    password_file_path = "password.txt"


    print("What would you like to do, add a new password or view the previous ones?")


    match= False 

    while not match:
        choice= input("Enter your choice: ")

        if choice == "add":
            site= input("Enter the site/title: ")
            password= input("Enter password: ")
            pm.add_password(site, password)
        elif choice == "view" :
            site= input("Enter the site/title: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            break
        else:
            print("Invalid choice.")
            

if __name__ == "__main__":
    main()