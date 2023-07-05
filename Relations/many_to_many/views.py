from .models import Article, Publication
from django.db.models import Count
from django.http import HttpResponse


def create_publication_view(request):
    p1 = Publication(title='The Python Journal')
    p1.save()
    p2 = Publication(title='Science News')
    p2.save()
    create_article_view(request, p1, p2)
    return HttpResponse('Publications created successfully')


def create_article_view(request, p1, p2):
    a1 = Article(headline='Django First Article')
    a1.save()

    """ 
        Associate the Article with a Publication
    """

    a1.publications.add(p1)
    a2 = Article(headline='NASA uses Python')
    a2.save()
    a2.publications.add(p1, p2)

    """
        Create and add a Publication to an Article in one step 
    """

    p3 = a2.publications.create(title='Highlights for Children')
    get_publications_view(request, a1, a2)
    get_articles_view(request, p1, p2, p3)
    return HttpResponse('Articles created Successfully')


def get_publications_view(request, a1, a2):
    """
        Article objects have access to their related Publication objects
    """

    print(a2.publications.all())
    a1_publications = a1.publications.all()
    for p in a1_publications:
        print(p.title)
    return HttpResponse('Publications fetched successfully')


def get_articles_view(request, p1, p2, p3):
    """
        Publication objects have access to their related Article objects
    """

    print(p1.article_set.all())
    print(p2.article_set.all())
    print(Publication.objects.get(id=3).article_set.all())

    """
        Fetching using where condition
    """

    print(Article.objects.filter(publications__id=1))
    print(Article.objects.filter(publications__title__startswith='Science').distinct().count())

    """
        Group articles by publication title and count the number of articles per publication
    """
    grouped_articles = Article.objects.values('publications__title').annotate(article_count=Count('id'))

    for group in grouped_articles:
        publication_title = group['publications__title']
        article_count = group['article_count']
        print(f"Publication: {publication_title}, Article Count: {article_count}")

    return HttpResponse('Articles fetched successfully')



