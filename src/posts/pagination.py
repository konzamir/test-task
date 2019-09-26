from rest_framework.pagination import LimitOffsetPagination, _positive_int
from django.conf import settings


class CustomPaginator(LimitOffsetPagination):
    default_limit = settings.POSTS_PER_PAGE
    offset_query_param = "page"

    def get_offset(self, request):
        try:
            offset = _positive_int(
                request.query_params[self.offset_query_param],
            )
            if offset == 0:
                offset = 1
            if offset > 1:
                offset = (offset - 1) * self.default_limit + 1
            return offset - 1
        except (KeyError, ValueError):
            return 0
