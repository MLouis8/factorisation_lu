def display_matrix(M):
    print("$\\begin{pmatrix}")
    size = len(M.shape)
    if size == 1:
        for elem in M:
                print(f"{elem} \\\\", end='\n')
    elif size == 2:
        for l in M:
            beginning = True
            for elem in l:
                print(f"{elem}", end=' ') if beginning else print(f"& {elem}", end=' ')
                beginning = False
            print("\\\\", end='\n')
    else:
        raise ValueError("taille incompatible")
    print("\\end{pmatrix}$")