from mysqlconnection import connectToMySQL

class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users').query_db(query)
        users = []

        for user in results:
            users.append( cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        return connectToMySQL('users').query_db( query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * from users WHERE id = %(id)s;"
        result = connectToMySQL('users').query_db(query, data)
        if result:
            return cls(result[0])

    @classmethod
    def update_users(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(id)s"
        connectToMySQL('users').query_db(query,data)

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        connectToMySQL('users').query_db(query,data)

