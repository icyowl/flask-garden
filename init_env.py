import secrets

def main():
    with open('.env', 'w') as f:
        s = f'SECRET_KEY="{secrets.token_hex(16)}"'
        f.write(s)
        print(f'Maybe succeeded. {s}')

if __name__ == '__main__':
    main()