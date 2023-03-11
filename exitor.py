def env_exit(works):
    if len(works)!=0:
        print("=====Operations still in progress=====")
        ch = input("Force quit? (y/N): ")
        if ch=="y" or ch=="Y":
            print("Good bye!!!")
            exit()
        else:
            pass

    else:
        print("Good bye!!!")
        exit()
    
