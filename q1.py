#THIS CODE IS OWNED BY NURAFNI HASHIMA BINTI SUHIB (20DDT21F1010) FROM DDT4B FOR DFP40203 PYTHON PROGRAMMING.

# Create password.txt file
# newfiles = open ('password.txt','w')
# newfiles.write('admin897')
# newfiles.write('\nqwerty50')
# newfiles.write('\nvisuOp')
# newfiles.close()

class PasswordManager:

    def __init__(self):
        self.old_passwords = self.load_passwords()

    def load_passwords(self):
            with open("password.txt", "r") as file:
                passwords = file.read().splitlines()
            return passwords
        
    def save_passwords(self):
        with open("password.txt", "w") as file:
            file.write("\n".join(self.old_passwords))

    #Method get_password
    def get_password(self):
        return self.old_passwords[-1]

    #Method set_password
    def set_password(self, new_password):
        if new_password != self.old_passwords[-1] and new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            self.save_passwords()

    #Method is_correct
    def is_correct(self, password):
        return password == self.old_passwords[-1]


def main():
        password_manager = PasswordManager()
        current_password = password_manager.get_password()

        password = input("Please enter your password: ")
        if not password_manager.is_correct(password):
            print("Your password is wrong.")
            new_password = input("Please enter your new password to reset: ")
            password_manager.set_password(new_password)
            print("Your password has been reset and updated.Thank You!")
        else:
            print('You have succesfully logged in.')



if __name__ == "__main__":
        main()
