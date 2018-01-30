# coding: utf-8

"""
    

     This is pyrebrickable, a python CLI wrapper around the Rebrickable API<br> <br> It supports the v3 API through it's openAPI specification.<br> https://rebrickable.com/api/v3/swagger/?format=openapi<br> Models for Part, Set, etc. have been manually added to provide meaningful results from HTTP responses<br> <br> Some endpoints might not work, don't hesitate to file an issue<br>   # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rebrickable.models.set import Set  # noqa: F401,E501


class ArrayOfSets(object):
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
        'count': 'int',
        'results': 'list[Set]'
    }

    attribute_map = {
        'count': 'count',
        'results': 'results'
    }

    def __init__(self, count=None, results=None):  # noqa: E501
        """ArrayOfSets - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._results = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if results is not None:
            self.results = results

    @property
    def count(self):
        """Gets the count of this ArrayOfSets.  # noqa: E501


        :return: The count of this ArrayOfSets.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ArrayOfSets.


        :param count: The count of this ArrayOfSets.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def results(self):
        """Gets the results of this ArrayOfSets.  # noqa: E501


        :return: The results of this ArrayOfSets.  # noqa: E501
        :rtype: list[Set]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ArrayOfSets.


        :param results: The results of this ArrayOfSets.  # noqa: E501
        :type: list[Set]
        """

        self._results = results

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
        if not isinstance(other, ArrayOfSets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
