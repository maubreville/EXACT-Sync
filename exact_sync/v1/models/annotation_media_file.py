# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AnnotationMediaFile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'media_file_type': 'int',
        'file': 'str',
        'annotation': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'media_file_type': 'media_file_type',
        'file': 'file',
        'annotation': 'annotation'
    }

    def __init__(self, id=None, name=None, media_file_type=None, file=None, annotation=None):  # noqa: E501
        """AnnotationMediaFile - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._media_file_type = None
        self._file = None
        self._annotation = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if media_file_type is not None:
            self.media_file_type = media_file_type
        if file is not None:
            self.file = file
        self.annotation = annotation

    @property
    def id(self):
        """Gets the id of this AnnotationMediaFile.  # noqa: E501


        :return: The id of this AnnotationMediaFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnnotationMediaFile.


        :param id: The id of this AnnotationMediaFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AnnotationMediaFile.  # noqa: E501


        :return: The name of this AnnotationMediaFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnnotationMediaFile.


        :param name: The name of this AnnotationMediaFile.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def media_file_type(self):
        """Gets the media_file_type of this AnnotationMediaFile.  # noqa: E501


        :return: The media_file_type of this AnnotationMediaFile.  # noqa: E501
        :rtype: int
        """
        return self._media_file_type

    @media_file_type.setter
    def media_file_type(self, media_file_type):
        """Sets the media_file_type of this AnnotationMediaFile.


        :param media_file_type: The media_file_type of this AnnotationMediaFile.  # noqa: E501
        :type: int
        """

        self._media_file_type = media_file_type

    @property
    def file(self):
        """Gets the file of this AnnotationMediaFile.  # noqa: E501


        :return: The file of this AnnotationMediaFile.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this AnnotationMediaFile.


        :param file: The file of this AnnotationMediaFile.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def annotation(self):
        """Gets the annotation of this AnnotationMediaFile.  # noqa: E501


        :return: The annotation of this AnnotationMediaFile.  # noqa: E501
        :rtype: int
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this AnnotationMediaFile.


        :param annotation: The annotation of this AnnotationMediaFile.  # noqa: E501
        :type: int
        """
        #if annotation is None:
        #    raise ValueError("Invalid value for `annotation`, must not be `None`")  # noqa: E501

        self._annotation = annotation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AnnotationMediaFile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnnotationMediaFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
