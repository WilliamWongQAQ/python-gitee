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


class UserNotification(object):
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
        'content': 'str',
        'type': 'str',
        'unread': 'str',
        'mute': 'str',
        'updated_at': 'str',
        'url': 'str',
        'html_url': 'str',
        'actor': 'UserBasic',
        'repository': 'ProjectBasic',
        'subject': 'UserNotificationSubject',
        'namespaces': 'list[UserNotificationNamespace]'
    }

    attribute_map = {
        'id': 'id',
        'content': 'content',
        'type': 'type',
        'unread': 'unread',
        'mute': 'mute',
        'updated_at': 'updated_at',
        'url': 'url',
        'html_url': 'html_url',
        'actor': 'actor',
        'repository': 'repository',
        'subject': 'subject',
        'namespaces': 'namespaces'
    }

    def __init__(self, id=None, content=None, type=None, unread=None, mute=None, updated_at=None, url=None, html_url=None, actor=None, repository=None, subject=None, namespaces=None, _configuration=None):  # noqa: E501
        """UserNotification - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._content = None
        self._type = None
        self._unread = None
        self._mute = None
        self._updated_at = None
        self._url = None
        self._html_url = None
        self._actor = None
        self._repository = None
        self._subject = None
        self._namespaces = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content is not None:
            self.content = content
        if type is not None:
            self.type = type
        if unread is not None:
            self.unread = unread
        if mute is not None:
            self.mute = mute
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url
        if html_url is not None:
            self.html_url = html_url
        if actor is not None:
            self.actor = actor
        if repository is not None:
            self.repository = repository
        if subject is not None:
            self.subject = subject
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def id(self):
        """Gets the id of this UserNotification.  # noqa: E501


        :return: The id of this UserNotification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserNotification.


        :param id: The id of this UserNotification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def content(self):
        """Gets the content of this UserNotification.  # noqa: E501


        :return: The content of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UserNotification.


        :param content: The content of this UserNotification.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def type(self):
        """Gets the type of this UserNotification.  # noqa: E501


        :return: The type of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserNotification.


        :param type: The type of this UserNotification.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def unread(self):
        """Gets the unread of this UserNotification.  # noqa: E501


        :return: The unread of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._unread

    @unread.setter
    def unread(self, unread):
        """Sets the unread of this UserNotification.


        :param unread: The unread of this UserNotification.  # noqa: E501
        :type: str
        """

        self._unread = unread

    @property
    def mute(self):
        """Gets the mute of this UserNotification.  # noqa: E501


        :return: The mute of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._mute

    @mute.setter
    def mute(self, mute):
        """Sets the mute of this UserNotification.


        :param mute: The mute of this UserNotification.  # noqa: E501
        :type: str
        """

        self._mute = mute

    @property
    def updated_at(self):
        """Gets the updated_at of this UserNotification.  # noqa: E501


        :return: The updated_at of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserNotification.


        :param updated_at: The updated_at of this UserNotification.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this UserNotification.  # noqa: E501


        :return: The url of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UserNotification.


        :param url: The url of this UserNotification.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def html_url(self):
        """Gets the html_url of this UserNotification.  # noqa: E501


        :return: The html_url of this UserNotification.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this UserNotification.


        :param html_url: The html_url of this UserNotification.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def actor(self):
        """Gets the actor of this UserNotification.  # noqa: E501

        通知发送者  # noqa: E501

        :return: The actor of this UserNotification.  # noqa: E501
        :rtype: UserBasic
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this UserNotification.

        通知发送者  # noqa: E501

        :param actor: The actor of this UserNotification.  # noqa: E501
        :type: UserBasic
        """

        self._actor = actor

    @property
    def repository(self):
        """Gets the repository of this UserNotification.  # noqa: E501


        :return: The repository of this UserNotification.  # noqa: E501
        :rtype: ProjectBasic
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this UserNotification.


        :param repository: The repository of this UserNotification.  # noqa: E501
        :type: ProjectBasic
        """

        self._repository = repository

    @property
    def subject(self):
        """Gets the subject of this UserNotification.  # noqa: E501

        通知直接关联对象  # noqa: E501

        :return: The subject of this UserNotification.  # noqa: E501
        :rtype: UserNotificationSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this UserNotification.

        通知直接关联对象  # noqa: E501

        :param subject: The subject of this UserNotification.  # noqa: E501
        :type: UserNotificationSubject
        """

        self._subject = subject

    @property
    def namespaces(self):
        """Gets the namespaces of this UserNotification.  # noqa: E501

        通知次级关联对象  # noqa: E501

        :return: The namespaces of this UserNotification.  # noqa: E501
        :rtype: list[UserNotificationNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this UserNotification.

        通知次级关联对象  # noqa: E501

        :param namespaces: The namespaces of this UserNotification.  # noqa: E501
        :type: list[UserNotificationNamespace]
        """

        self._namespaces = namespaces

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
        if issubclass(UserNotification, dict):
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
        if not isinstance(other, UserNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserNotification):
            return True

        return self.to_dict() != other.to_dict()
