"""
As a senior backend engineer at Jovian, you are tasked with developing a 
fast in-memory data structure to manage profile information 
(username, name and email) for 100 million users. 

It should allow the following operations to be performed efficiently:
1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username
You can assume that usernames are unique.
"""

class User:
    def __init__(self, username, name, email) -> None:
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return "User(username='{}', email='{}')".format(self.username, self.email)
    
    def __str__(self) -> str:
        return self.__repr__()

    def introduce_yourself(self):
        print("Hi, I'm %s! Contact me at %s" % (self.username, self.email))


class UserDatabase:
    def __init__(self) -> None:
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i = i+1
        self.users.insert(i, user)


    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        temp = self.find(user.username)
        temp.name, temp.email = user.name, user.email


    def list_all(self):
        return self.users


if __name__ == "__main__":
    user1 = User("siddy", "Siddesh BG", "siddesh.bg@gmail.com")
    user2 = User("samsy", "Samskruthi", "sams.kruthi@gmail.com")
    user3 = User("samik", "Samiksha", "samiksha.s@gmail.com")
    user4 = User("seema", "Seema C", "seemac7@gmail.com")

    # user3.introduce_yourself()
    # print(user4)

    user_db = UserDatabase()
    user_db.users = [user1, user2, user3, user4]
    print(user_db.find("samsy"))
    user_db.insert(User("santhu", "Santhosh G", "santhosh.g@gmail.com"))
    print(user_db.list_all())
    user_db.update(User("santhu", "Santhosh G", "santhosh.g2k@gmail.com"))
    print(user_db.list_all())


