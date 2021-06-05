class News:
    '''
    News class to define news object
    '''
    def __init__(self,source,author,title,description,poster):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.poster='https://mw3.wsj.net/mw5/content/logos/mw_logo_social.png' +poster
