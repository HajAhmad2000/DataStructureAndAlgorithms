from project_BST import BST

print("\n------------\nPrinting the Null Tree\n------------\n")
bst = BST()
print(bst)

print("\n------------\nPrinting After Inserting Item to the Tree\n------------\n")
bst.NR_Insert(1)
print(bst)

print("\n------------\nPrinting After more Inserting Item to the Tree\n------------\n")
bst.NR_Insert(2)
bst.NR_Insert(3)
bst.NR_Insert(2.5)
print(bst)

print("\n------------\nPrinting After more Inserting Item to the Tree\n------------\n")
bst.NR_Insert(4)
print(bst)

print("\n------------\nPrinting Minimum(NR_Procedure)\n------------\n")
print("Minimum Is:", bst.NR_Minimum())

print("\n------------\nDelete Minimum for root\n------------\n")
print("Delete Min has Done:", bst.BST_DeleteMin(bst.root))
print(bst)

print("\n------------\nDelete Minimum for 3.00\n------------\n")
print("Delete Min has Done:", bst.BST_DeleteMin(bst.root.right))
print(bst)


print("\n")




# (---)(---)(---)(---)(---)(---)(---)15.25(---)(---)(---)(---)(---)(---)(---)
# (---)(---)(---)12.25(---)(---)(---)(---)(---)(---)(---)13.25(---)(---)(---)
# (---)14.25(---)(---)(---)15.32(---)(---)(---)15.35(---)(---)(---)15.25(---)
# 12.20(---)14.25(---)15.32(---)15.32(---)15.32(---)15.32(---)15.32(---)15.25

# (---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)15.25(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)
# (---)(---)(---)(---)(---)(---)(---)13.25(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)(---)12.25(---)(---)(---)(---)(---)(---)(---)
# (---)(---)(---)14.25(---)(---)(---)(---)(---)(---)(---)14.25(---)(---)(---)(---)(---)(---)(---)14.25(---)(---)(---)(---)(---)(---)(---)15.35(---)(---)(---)
# (---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)12.20(---)(---)(---)14.25(---)(---)(---)15.32(---)
# 12.20(---)14.25(---)15.32(---)15.32(---)15.32(---)15.32(---)15.32(---)15.25(---)12.20(---)14.25(---)15.32(---)15.32(---)15.32(---)15.32(---)15.32(---)15.25