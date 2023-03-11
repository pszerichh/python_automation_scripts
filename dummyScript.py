def fun(works):
    if(len(works)==0):
        print("No jobs pending")
        return
    else:
        for wk in works:
            print(wk.name)
