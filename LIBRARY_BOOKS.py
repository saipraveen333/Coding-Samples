class book:
    def __init__(self,book_id,book_name):
        self.book_id=book_id
        self.book_name=book_name


class library:
    def __init__(self,library_id,address,book_list):
        self.library_id=library_id
        self.address=address
        self.book_list=book_list

    def char_input(self, ch):
        count=0
        for i in self.book_list:
            if i.book_name[0]==ch:
                count+=1
        return count
    def remove_books(self,new_book_list):
         for i in self.book_list:
            for j in new_book_list:
                if i.book_name==j:
                    self.book_list.remove(i)
                    print('The book','\'',i.book_name,'\'','is removed')
book_list=[]
for i in range(int(input())):
    book_id=int(input())
    book_name=input()
    book_list.append(book(book_id,book_name))
ch=input()
new_book_list=[]
for i in range(int(input())):
    new_book_list.append(input())
obj=library('lib_id','address',book_list)
print(obj.char_input(ch))
obj.remove_books(new_book_list)

























