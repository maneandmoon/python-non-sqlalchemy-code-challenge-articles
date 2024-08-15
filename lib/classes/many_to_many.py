class Article:
    all = []

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
        if(not hasattr(self, 'title') and isinstance(new_title, str) and 5 <= len(new_title) <= 50):
            self._title = new_title
        else:
            raise Exception("title is an immutable string and must be between 5 and 50 characters inclusive")   
 
 
    def __repr__(self):
        return f'<Article author={self.author} magazine={self.magazine} title={self.title} />'    


class Author:
    def __init__(self, name):
        self.name = name
        
    # look through all articles and find articles author has written Article.all
    # return list [] of all articles author has written article.author == self

    def articles(self):
        return [article for article in Article.all if article.author == self]

    # look through all articles and extract magazine where author contributed 
    # return unique list ---use set and turn back to list article.magazine
    # already have list of articles author written from  def articles == self.articles()
    #can write like this: for article in self.articles(), return (list(set(article.magazine)))
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    # Author add_article(magazine, title)
    # Receives a `Magazine` instance, and a title as arguments
    # magazine=magazine and title=title
    # Creates and returns a new `Article` instance and associates it with that author, the magazine provided == author=self
    #return new article instance == Article


    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)
    
    # FAILED Author in many_to_many.py topic areas are unique - assert [] is None
    # list and set article.magazine.category
    # Returns `None` if the author has no articles
    # self.articles() = None
    # for article in self.articles() == (which we already know is a list of all articles the author has written) 
    # return the categories of the magazines author has contribute == article.magazine.category
    
    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if(not hasattr(self, 'name') and isinstance(new_name, str) and len(new_name) > 0):
            self._name = new_name
        else:
            raise Exception("author name is of type str and cannot change and author name must be longer than 0 characters")
   

    def __repr__(self):
        return f'<Author name={self.name} />'


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # look through all articles and find matching one
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # look through matching articles to find authors and return unique list
    # use self.articles()

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    # look through matching articles to find titles 
    # Returns `None` if the magazine has no articles
    # if not self.articles():return None
    
    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    # look for authors with more than 2 articles 
    # something along this line== [article.author for article in self.articles() if greater than 2 articles]    
    # self.articles() list of all articles mag published = articles
    # get list of authors and this is = to at least 1 article ==create get_authors 
    # create a new list to add author + 1 == contributing_authors []
    # The count() method returns the number of elements with the specified value.
    # list.count
    # sum 
          
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
        else:
            raise Exception("magazine name is of type str and can change and magazine name is between 2 and 16 character, inclusive")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if(isinstance(new_category, str) and len(new_category) > 0):
            self._category = new_category
        else:
            raise Exception("magazine category is of type str and can change and magazine category has length greater than 0")


    # #### Bonus: Aggregate and Association Method
    # - `Magazine classmethod top_publisher()`
    #   - Returns the `Magazine` instance with the most articles
        # create most_articles and have it = 0
    #   - Returns `None` if there are no articles.
        #if no articles in magazine write if not cls.all, return None
    #   - Uncomment lines 206-224 in the magazine_test file
    #   - _hint: will need a way to remember all magazine objects_
        # create magazine_list = []===not [] use None
        # FAILED Magazine in many_to_many.py returns the magazine with the most articles - AssertionError: assert [] == None
        #return magazine_list which will have the count of most articles
        # get count of articles by len of magazine.articles()    

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

