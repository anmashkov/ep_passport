from Register import Register


def main():
    reg = Register()
    db = reg.get_db()
    db.init_database()


if __name__ == '__main__':
    main()