# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PartCategory(object):
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
        'part_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'part_count': 'part_count'
    }

    def __init__(self, id=None, name=None, part_count=None):  # noqa: E501
        """PartCategory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._part_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if part_count is not None:
            self.part_count = part_count

    @property
    def id(self):
        """Gets the id of this PartCategory.  # noqa: E501


        :return: The id of this PartCategory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartCategory.


        :param id: The id of this PartCategory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PartCategory.  # noqa: E501


        :return: The name of this PartCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartCategory.


        :param name: The name of this PartCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def part_count(self):
        """Gets the part_count of this PartCategory.  # noqa: E501


        :return: The part_count of this PartCategory.  # noqa: E501
        :rtype: int
        """
        return self._part_count

    @part_count.setter
    def part_count(self, part_count):
        """Sets the part_count of this PartCategory.


        :param part_count: The part_count of this PartCategory.  # noqa: E501
        :type: int
        """

        self._part_count = part_count

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PartCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
