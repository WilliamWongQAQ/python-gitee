# coding: utf-8

"""
    码云 Open API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from gitee.configuration import Configuration


class EnterpriseMember(object):
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
        'url': 'str',
        'active': 'str',
        'remark': 'str',
        'role': 'str',
        'outsourced': 'str',
        'enterprise': 'EnterpriseBasic',
        'user': 'str'
    }

    attribute_map = {
        'url': 'url',
        'active': 'active',
        'remark': 'remark',
        'role': 'role',
        'outsourced': 'outsourced',
        'enterprise': 'enterprise',
        'user': 'user'
    }

    def __init__(self, url=None, active=None, remark=None, role=None, outsourced=None, enterprise=None, user=None, _configuration=None):  # noqa: E501
        """EnterpriseMember - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._url = None
        self._active = None
        self._remark = None
        self._role = None
        self._outsourced = None
        self._enterprise = None
        self._user = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if active is not None:
            self.active = active
        if remark is not None:
            self.remark = remark
        if role is not None:
            self.role = role
        if outsourced is not None:
            self.outsourced = outsourced
        if enterprise is not None:
            self.enterprise = enterprise
        if user is not None:
            self.user = user

    @property
    def url(self):
        """Gets the url of this EnterpriseMember.  # noqa: E501


        :return: The url of this EnterpriseMember.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EnterpriseMember.


        :param url: The url of this EnterpriseMember.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def active(self):
        """Gets the active of this EnterpriseMember.  # noqa: E501


        :return: The active of this EnterpriseMember.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this EnterpriseMember.


        :param active: The active of this EnterpriseMember.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def remark(self):
        """Gets the remark of this EnterpriseMember.  # noqa: E501


        :return: The remark of this EnterpriseMember.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this EnterpriseMember.


        :param remark: The remark of this EnterpriseMember.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def role(self):
        """Gets the role of this EnterpriseMember.  # noqa: E501


        :return: The role of this EnterpriseMember.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this EnterpriseMember.


        :param role: The role of this EnterpriseMember.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def outsourced(self):
        """Gets the outsourced of this EnterpriseMember.  # noqa: E501


        :return: The outsourced of this EnterpriseMember.  # noqa: E501
        :rtype: str
        """
        return self._outsourced

    @outsourced.setter
    def outsourced(self, outsourced):
        """Sets the outsourced of this EnterpriseMember.


        :param outsourced: The outsourced of this EnterpriseMember.  # noqa: E501
        :type: str
        """

        self._outsourced = outsourced

    @property
    def enterprise(self):
        """Gets the enterprise of this EnterpriseMember.  # noqa: E501


        :return: The enterprise of this EnterpriseMember.  # noqa: E501
        :rtype: EnterpriseBasic
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this EnterpriseMember.


        :param enterprise: The enterprise of this EnterpriseMember.  # noqa: E501
        :type: EnterpriseBasic
        """

        self._enterprise = enterprise

    @property
    def user(self):
        """Gets the user of this EnterpriseMember.  # noqa: E501


        :return: The user of this EnterpriseMember.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EnterpriseMember.


        :param user: The user of this EnterpriseMember.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(EnterpriseMember, dict):
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
        if not isinstance(other, EnterpriseMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnterpriseMember):
            return True

        return self.to_dict() != other.to_dict()
