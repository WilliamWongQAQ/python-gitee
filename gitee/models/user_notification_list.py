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


class UserNotificationList(object):
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
        'total_count': 'int',
        'list': 'list[UserNotification]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'list': 'list'
    }

    def __init__(self, total_count=None, list=None, _configuration=None):  # noqa: E501
        """UserNotificationList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._total_count = None
        self._list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if list is not None:
            self.list = list

    @property
    def total_count(self):
        """Gets the total_count of this UserNotificationList.  # noqa: E501


        :return: The total_count of this UserNotificationList.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this UserNotificationList.


        :param total_count: The total_count of this UserNotificationList.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def list(self):
        """Gets the list of this UserNotificationList.  # noqa: E501

        通知列表  # noqa: E501

        :return: The list of this UserNotificationList.  # noqa: E501
        :rtype: list[UserNotification]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this UserNotificationList.

        通知列表  # noqa: E501

        :param list: The list of this UserNotificationList.  # noqa: E501
        :type: list[UserNotification]
        """

        self._list = list

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
        if issubclass(UserNotificationList, dict):
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
        if not isinstance(other, UserNotificationList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserNotificationList):
            return True

        return self.to_dict() != other.to_dict()
