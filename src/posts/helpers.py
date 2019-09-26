from accounts.models import UserModel
from posts.models import CommendsModel, FilesModel
from posts.serializers import CommendSerializer, FilesSerializer


def get_all_children_json(query):
    data = []

    if query:
        for x in query:
            comm = CommendSerializer(
                x, many=False
            ).data

            try:
                children = get_all_children_json(x.get_children())

                comm['children'] = children
            except AttributeError:
                comm['children'] = []

            data.append(comm)

    return data


def get_full_post_data(d) -> dict:
    data = d
    data['user'] = UserModel.objects.get(pk=data['user']).username

    files = FilesModel.objects.filter(post__id=data['id'])
    files = FilesSerializer(
        files, many=True
    ).data

    data['files'] = files

    commends = CommendsModel.objects.filter(post__id=data['id'], parent__isnull=True)
    data['commends'] = get_all_children_json(commends)

    return data
