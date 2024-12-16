def chess(board,square):
    for k in range(board):
        for i in range(square):
            for j in range(board):
                print(" "*square+"#"*square, end='')
            print()
        for i in range(square):
            for j in range(board):
                print("#"*square+" "*square, end='')
            print()

print("---- chess(4,3) ---- \n")

chess(4,3)

print("---- chess(2,1) ---- \n")
chess(2,1)