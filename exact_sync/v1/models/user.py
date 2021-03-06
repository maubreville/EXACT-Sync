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


class User(object):
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
        'username': 'str',
        'is_superuser': 'bool',
        'is_staff': 'bool',
        'is_active': 'bool',
        'last_login': 'datetime',
        'team_set': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'is_superuser': 'is_superuser',
        'is_staff': 'is_staff',
        'is_active': 'is_active',
        'last_login': 'last_login',
        'team_set': 'team_set'
    }

    def __init__(self, id=None, username=None, is_superuser=None, is_staff=None, is_active=None, last_login=None, team_set=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._is_superuser = None
        self._is_staff = None
        self._is_active = None
        self._last_login = None
        self._team_set = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.username = username
        if is_superuser is not None:
            self.is_superuser = is_superuser
        if is_staff is not None:
            self.is_staff = is_staff
        if is_active is not None:
            self.is_active = is_active
        if last_login is not None:
            self.last_login = last_login
        if team_set is not None:
            self.team_set = team_set

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def is_superuser(self):
        """Gets the is_superuser of this User.  # noqa: E501

        Designates that this user has all permissions without explicitly assigning them.  # noqa: E501

        :return: The is_superuser of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_superuser

    @is_superuser.setter
    def is_superuser(self, is_superuser):
        """Sets the is_superuser of this User.

        Designates that this user has all permissions without explicitly assigning them.  # noqa: E501

        :param is_superuser: The is_superuser of this User.  # noqa: E501
        :type: bool
        """

        self._is_superuser = is_superuser

    @property
    def is_staff(self):
        """Gets the is_staff of this User.  # noqa: E501

        Designates whether the user can log into this admin site.  # noqa: E501

        :return: The is_staff of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_staff

    @is_staff.setter
    def is_staff(self, is_staff):
        """Sets the is_staff of this User.

        Designates whether the user can log into this admin site.  # noqa: E501

        :param is_staff: The is_staff of this User.  # noqa: E501
        :type: bool
        """

        self._is_staff = is_staff

    @property
    def is_active(self):
        """Gets the is_active of this User.  # noqa: E501

        Designates whether this user should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :return: The is_active of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this User.

        Designates whether this user should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :param is_active: The is_active of this User.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501


        :return: The last_login of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.


        :param last_login: The last_login of this User.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def team_set(self):
        """Gets the team_set of this User.  # noqa: E501


        :return: The team_set of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._team_set

    @team_set.setter
    def team_set(self, team_set):
        """Sets the team_set of this User.


        :param team_set: The team_set of this User.  # noqa: E501
        :type: list[str]
        """

        self._team_set = team_set

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
