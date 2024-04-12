from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "descriptions")
    query = SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")


    # keywords = [word for word in query.split() if len(word) > 2]
    #
    #
    # q_object = Q()
    #
    # for token in keywords:
    #     q_object |= Q(descriptions__icontains=token)
    #     q_object |= Q(name__icontains=token)
    #
    # return Products.objects.filter(q_object)