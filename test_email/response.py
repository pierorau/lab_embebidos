# coding=utf-8

from rest_framework.response import Response


def response_success(data=None, *args, **kwargs):
    return Response(
        data={'success': True, 'data': data},
        headers={'Access-Control-Allow-Origin': '*'},
        *args, **kwargs
    )


def response_error(error=None, *args, **kwargs):
    return Response(
        data={'success': False, 'message': error},
        content_type="application/json",
        headers={'Access-Control-Allow-Origin': '*'},
        *args, **kwargs
    )
