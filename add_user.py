import click
import sqlite3
from werkzeug.security import generate_password_hash


@click.command()
@click.option('--username', prompt='Your name')
@click.option('--password', prompt='Your password')
def main(username, password):
    
    pw_hash = generate_password_hash(password)

    conn = sqlite3.connect('instance/user.sqlite')
    cur = conn.cursor()
    cur.executescript(
        f'INSERT INTO user(username, password) VALUES("{username}", "{pw_hash}");'
        )
    conn.commit()
    click.echo(f"I've added {username} into db")



if __name__ == '__main__':
    main()