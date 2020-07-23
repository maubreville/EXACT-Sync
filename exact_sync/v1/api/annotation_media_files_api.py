# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import
from exact_sync.v1.api.pagination_base_api import PaginationBaseAPI
import re  # noqa: F401
# python 2 and python 3 compatibility library
import six

from exact_sync.v1.api_client import ApiClient


class AnnotationMediaFilesApi(PaginationBaseAPI):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_annotation_media_file(self, **kwargs):  # noqa: E501
        """create_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation_media_file(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param int media_file_type:
        :param str file:
        :param int annotation:
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_annotation_media_file_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_annotation_media_file_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_annotation_media_file_with_http_info(self, **kwargs):  # noqa: E501
        """create_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation_media_file_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param int media_file_type:
        :param str file:
        :param int annotation:
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'media_file_type', 'file', 'annotation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_annotation_media_file" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        if 'name' in params:
            form_params.append(('name', params['name']))  # noqa: E501
        if 'media_file_type' in params:
            form_params.append(('media_file_type', params['media_file_type']))  # noqa: E501
        if 'annotation' in params:
            form_params.append(('annotation', params['annotation']))  # noqa: E501

        body_params = {}
            
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotation_media_files/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationMediaFiles',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def destroy_annotation_media_file(self, id, **kwargs):  # noqa: E501
        """destroy_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_annotation_media_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.destroy_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.destroy_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def destroy_annotation_media_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """destroy_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_annotation_media_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_annotation_media_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `destroy_annotation_media_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotation_media_files/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_annotation_media_files(self, pagination:bool=True, **kwargs):  # noqa: E501
        """list_annotation_media_files  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_annotation_media_files(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str id: id
        :param str name: name
        :param str name__contains: name__contains
        :param str annotation: annotation
        :param str media_file_type: media_file_type
        :return: AnnotationMediaFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if pagination:
            if kwargs.get('async_req'):
                return self.list_annotation_media_files_with_http_info(**kwargs)  # noqa: E501
            else:
                (data) = self.list_annotation_media_files_with_http_info(**kwargs)  # noqa: E501
                return data
        else:
            return self._get_all(self.list_annotation_media_files_with_http_info, **kwargs)

    def list_annotation_media_files_with_http_info(self, **kwargs):  # noqa: E501
        """list_annotation_media_files  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_annotation_media_files_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str id: id
        :param str name: name
        :param str name__contains: name__contains
        :param str annotation: annotation
        :param str media_file_type: media_file_type
        :return: AnnotationMediaFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'id', 'name', 'name__contains', 'annotation', 'media_file_type']  # noqa: E501
        all_params.append('omit')
        all_params.append('expand')
        all_params.append('fields')
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_annotation_media_files" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name__contains' in params:
            query_params.append(('name__contains', params['name__contains']))  # noqa: E501
        if 'annotation' in params:
            query_params.append(('annotation', params['annotation']))  # noqa: E501
        if 'media_file_type' in params:
            query_params.append(('media_file_type', params['media_file_type']))  # noqa: E501
        if 'omit' in params:
            query_params.append(('omit', params['omit']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotation_media_files/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationMediaFiles',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_annotation_media_file(self, id, **kwargs):  # noqa: E501
        """partial_update_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_annotation_media_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str name:
        :param int media_file_type:
        :param int annotation:
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.partial_update_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def partial_update_annotation_media_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """partial_update_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_annotation_media_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str name:
        :param int media_file_type:
        :param int annotation:
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name', 'media_file_type', 'annotation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_annotation_media_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `partial_update_annotation_media_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = {}
        if 'name' in params:
            body_params['name'] = params['name']
        if 'media_file_type' in params:
            body_params['media_file_type'] = params['media_file_type']
        if 'annotation' in params:
            body_params['annotation'] = params['annotation']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotation_media_files/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationMediaFile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_annotation_media_file(self, id, **kwargs):  # noqa: E501
        """retrieve_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_annotation_media_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str name: name
        :param str name__contains: name__contains
        :param str annotation: annotation
        :param str media_file_type: media_file_type
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def retrieve_annotation_media_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """retrieve_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_annotation_media_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str name: name
        :param str name__contains: name__contains
        :param str annotation: annotation
        :param str media_file_type: media_file_type
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name', 'name__contains', 'annotation', 'media_file_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('omit')
        all_params.append('fields')
        all_params.append('expand')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_annotation_media_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `retrieve_annotation_media_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name__contains' in params:
            query_params.append(('name__contains', params['name__contains']))  # noqa: E501
        if 'annotation' in params:
            query_params.append(('annotation', params['annotation']))  # noqa: E501
        if 'media_file_type' in params:
            query_params.append(('media_file_type', params['media_file_type']))  # noqa: E501
        if 'omit' in params:
            query_params.append(('omit', params['omit']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E50
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

            
        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotation_media_files/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationMediaFile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_annotation_media_file(self, id, **kwargs):  # noqa: E501
        """update_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation_media_file(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param AnnotationMediaFile body:
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_annotation_media_file_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_annotation_media_file_with_http_info(self, id, **kwargs):  # noqa: E501
        """update_annotation_media_file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation_media_file_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param AnnotationMediaFile body:
        :return: AnnotationMediaFile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_annotation_media_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_annotation_media_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in body:
            local_var_files['file'] = body['file']  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/annotations/annotation_media_files/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationMediaFile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
