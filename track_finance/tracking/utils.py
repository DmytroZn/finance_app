from rest_framework.response import Response
from rest_framework import status


class ObjectGetting:
    def __init__(self, obj, **kwargs):
        self._obj = obj
        self.kwargs = kwargs

    def get_model(self):
        try:
            self._res = self._obj.objects.get(**self.kwargs)
        except self._obj.DoesNotExist:
            return False, Response({"msg": "Not_Found"}, status=status.HTTP_404_NOT_FOUND)
        return True, self._res


def adding_user_id(func):
    def wrapper(*args, **kwargs):
        args[1].data['fk_user'] = args[1].user.id
        return func(*args, **kwargs)
    return wrapper
