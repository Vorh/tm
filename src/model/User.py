class User():

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


def userMapper(row):
    user = User()
    user.id = row['id']
    user.login = row['username']
    user.password = row['password']
    return user
