import os
import django
django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

def main():
    from blog.models import Blog
    # f = open('oldblog.txt')
    # for line in f:
    #     title, content = line.split('****')
    #     Blog.objects.create(title=title, content=content)
    # f.close()
    Blog_list = []
    with open('oldblog.txt') as f:
        Blog_list = [Blog(title=line.split('****')[0]), content=line.split('****')[1] for line in f]
        Blog.objects.bulk_create(Blog_list)
if __name__ == '__main__':
    main()
    print('Done!')

