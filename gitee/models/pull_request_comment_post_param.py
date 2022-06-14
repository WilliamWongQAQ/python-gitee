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


class PullRequestCommentPostParam(object):
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
        'access_token': 'str',
        'body': 'str',
        'commit_id': 'str',
        'path': 'str',
        'position': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'body': 'body',
        'commit_id': 'commit_id',
        'path': 'path',
        'position': 'position'
    }

    def __init__(self, access_token=None, body=None, commit_id=None, path=None, position=None, _configuration=None):  # noqa: E501
        """PullRequestCommentPostParam - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._body = None
        self._commit_id = None
        self._path = None
        self._position = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if body is not None:
            self.body = body
        if commit_id is not None:
            self.commit_id = commit_id
        if path is not None:
            self.path = path
        if position is not None:
            self.position = position

    @property
    def access_token(self):
        """Gets the access_token of this PullRequestCommentPostParam.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this PullRequestCommentPostParam.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this PullRequestCommentPostParam.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this PullRequestCommentPostParam.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def body(self):
        """Gets the body of this PullRequestCommentPostParam.  # noqa: E501

        必填。评论内容  # noqa: E501

        :return: The body of this PullRequestCommentPostParam.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PullRequestCommentPostParam.

        必填。评论内容  # noqa: E501

        :param body: The body of this PullRequestCommentPostParam.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def commit_id(self):
        """Gets the commit_id of this PullRequestCommentPostParam.  # noqa: E501

        可选。PR代码评论的commit id  # noqa: E501

        :return: The commit_id of this PullRequestCommentPostParam.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this PullRequestCommentPostParam.

        可选。PR代码评论的commit id  # noqa: E501

        :param commit_id: The commit_id of this PullRequestCommentPostParam.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def path(self):
        """Gets the path of this PullRequestCommentPostParam.  # noqa: E501

        可选。PR代码评论的文件名  # noqa: E501

        :return: The path of this PullRequestCommentPostParam.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PullRequestCommentPostParam.

        可选。PR代码评论的文件名  # noqa: E501

        :param path: The path of this PullRequestCommentPostParam.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def position(self):
        """Gets the position of this PullRequestCommentPostParam.  # noqa: E501

        可选。PR代码评论diff中的行数  # noqa: E501

        :return: The position of this PullRequestCommentPostParam.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PullRequestCommentPostParam.

        可选。PR代码评论diff中的行数  # noqa: E501

        :param position: The position of this PullRequestCommentPostParam.  # noqa: E501
        :type: int
        """

        self._position = position

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
        if issubclass(PullRequestCommentPostParam, dict):
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
        if not isinstance(other, PullRequestCommentPostParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullRequestCommentPostParam):
            return True

        return self.to_dict() != other.to_dict()
