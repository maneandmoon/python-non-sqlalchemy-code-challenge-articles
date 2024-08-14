class Article:
    all =[]

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property 
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if(isinstance(new_author, Author)):
            self._author = new_author

    @property 
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if(isinstance(new_magazine, Magazine)):
            self._magazine = new_magazine        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if(isinstance(new_title, str) and 5 <= len(new_title) <= 50):
            # self._title = new_title
            if(hasattr(self, 'title')):
                print("title cannot change")
            else:
                self._title = new_title


    def __repr__(self):
        return f'<Article author={self.author} magazine={self.magazine} title={self.title} />'    
    
class Author:
    def __init__(self, name):
        self.name = name
        
    # look through all articles and find articles author has written 
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # look through all articles and extract magazine where author contributed unique=set and return as list
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
#     - `Author add_article(magazine, title)`
#   - Receives a `Magazine` instance, and a title as arguments
#   - Creates and returns a new `Article` instance and associates it with that
#     author, the magazine provided 
#return new article instance
# FAILED Author in many_to_many.py creates and returns a new article given a magazine and title - TypeError: __init__() missing 1 required positional argument: 'author'

    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)
    
    #unique list of strings with categories of magazines author contributed
    #list and set article.magazine.category
    # None if author has no articles
    # self.articles() = None
    # FAILED Author in many_to_many.py topic areas are unique - assert [] is None
    
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if(isinstance(new_name, str) and len(new_name) > 0):
            # self._name = new_name 
            if(hasattr(self, 'name')):
                print("name cannot change")
            else:
                self._name = new_name
        else:
            raise Exception("author name is of type str and cannot change")
        #comment out- **author_test.py**
        #- lines 31-32, and 35-36
        #uncomment out  - **author_test.py**
        #- lines 39-40, and 53-54

    def __repr__(self):
        return f'<Author name={self.name} />'


class Magazine:
    all =[]

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    #look through all articles and find matching one
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    #look through matching articles to find authors and return unique list
    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    #look through matching articles to find titles 
    # return none if magazine has no articles
        # if not self.articles():
        #     return None
    
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    #look for authors with more than 2 articles    
    #self.articles() list of all articles mag published
    #get authors --so get list of authors and this is = to at least 1 article
    #create a new list to add author + 1
    #The count() method returns the number of elements with the specified value.
    #list.count
    # [article.author for article in self.articles() if article.title > 2]    
       
    def contributing_authors(self):
        articles = self.articles()
        if not articles:
            return None
        
        get_authors = set(article.author for article in articles)
        contributing_authors = []
        
        for author in get_authors:
            count = sum(1 for article in articles if article.author == author)
            if count > 2:
                contributing_authors.append(author)
        return contributing_authors if contributing_authors else None     
     
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if(isinstance(new_name, str) and 2 <= len(new_name) <= 16):
            self._name = new_name
        # else:
        #     raise Exception('name must be str and bewtween 2 and 16 characters')
        #comment out  - **magazine_test.py**
    # - lines 31-32, 47-48, 51-52, 84-85, and 100-102
        #uncomment  - **magazine_test.py**
    # - lines 35-36, 55-56, 59-60, 90-91, and 105-106

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if(isinstance(new_category, str) and len(new_category) > 0):
            self._category = new_category
        # else:
        #     raise Exception('category must be str and longer than 0 characters')

    # #### Bonus: Aggregate and Association Method

# - `Magazine classmethod top_publisher()`
#   - Returns the `Magazine` instance with the most articles
#   - Returns `None` if there are no articles.
#   - Uncomment lines 206-224 in the magazine_test file
#   - _hint: will need a way to remember all magazine objects_

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        
        most_articles = 0
        magazine_list = None

        for magazine in cls.all:
            article_count = len(magazine.articles())
            if article_count > most_articles:
                most_articles = article_count
                magazine_list = magazine
        return magazine_list       


    def __repr__(self):
        return f'<Magazine name={self.name} category={self.category} />'    

