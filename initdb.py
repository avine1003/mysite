import random
from mysite.wsgi import *
from blog.models import Author, Article, Tag


author_name_list = ['xiaobai', 'xiaohei', 'xiaoming', 'xiaohua']
article_title_list = ['Python 教程', 'Django 教程', 'JS 教程']

def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # 随机生成9位数qq
        author.qq = ''.join(str(random.choice(range(10))) for _ in range(9))
        author.addr = 'addr_{}'.format(random.randrange(1, 3))
        author.email = '{}@gmail.com'.format(author.addr)
        author.save()

def create_articles_and_tags():
    # 随机生成文章
    for article_title in article_title_list:
        # 从文章标题中得到tag
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)

        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '{}_{}'.format(article_title, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,  # 随机分配作者
                    'content': '{} 正文'.format(title),
                    'score': random.randrange(70, 101),  # 随机打分
                }
            )
            article.tags.add(tag)

def main():
    create_authors()
    create_articles_and_tags()

if __name__ == '__main__':
    main()
    print('Done!')
