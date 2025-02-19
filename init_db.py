import os
import sqlite3


def main():
    try:
        os.makedirs('instance')
    except OSError:
        pass

    conn = sqlite3.connect('instance/user.sqlite')
    cur = conn.cursor()
    cur.executescript(
        """
        DROP TABLE IF EXISTS user;

        CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        );
        """
    )
    conn.commit()
    print('done.')


if __name__ == '__main__':
    main()

