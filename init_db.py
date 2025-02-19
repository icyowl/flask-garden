import os
import sqlite3
from werkzeug.security import generate_password_hash


def main():

    user = 'Alice'
    password = 'madteaparty1865'
    pw_hash = generate_password_hash(password)

    conn = sqlite3.connect('instance/user.sqlite')
    cur = conn.cursor()
    cur.executescript(
        f"""
        DROP TABLE IF EXISTS user;

        CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        );

        INSERT INTO user(username, password) VALUES('{user}', '{pw_hash}');
        """
    )
    conn.commit()
    print('done.')


if __name__ == '__main__':
    main()

