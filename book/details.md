Home page 
2. Signing up a new user (e.g. admin, student) 
3. Login as admin and as student 
4. Updating a user details 
5. Adding a book (by admin) 
6. Updating a book details (by admin) 
7. Browsing books ((by admin and students) 
8. Showing a list of books that satisfy certain criteria (e.g., ISBN, publication year, author…) 
9. Performing operations on books: borrowing, returning, extending borrowing period 
10. Log out

    title=models.CharField(max_length=100)
    ISBN=models.IntegerField(default=0)
    publishedAt=models.DateField(auto_now=True)
    borrowingPeriod=models.IntegerField(default=0)
    numberOfPages=models.IntegerField(default=0)
    author=models.CharField(max_length=100)
    image=models.ImageField()
    borowingStatu=models.BooleanField()
    description=models.TextField()