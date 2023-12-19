import dis

a = 100

def main():
    b = 100
    c = 100
    print(b is c)
    print(a is b)
    print(a is c)

if __name__ == "__main__":
    main()
    dis.dis(main)