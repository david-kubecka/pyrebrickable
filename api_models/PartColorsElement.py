# coding: utf-8

import pprint
import re  # noqa: F401

import six


class PartColorsElement(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'elements': 'List',
        'numUnderscoresetUnderscoreparts': 'Integer',
        'numUnderscoresets': 'Integer',
        'partUnderscoreimgUnderscoreurl': 'String',
        'yearUnderscorefrom': 'Integer',
        'yearUnderscoreto': 'Integer'
    }

    attribute_map = {
        'elements': 'elements',
        'numUnderscoresetUnderscoreparts': 'num_set_parts',
        'numUnderscoresets': 'num_sets',
        'partUnderscoreimgUnderscoreurl': 'part_img_url',
        'yearUnderscorefrom': 'year_from',
        'yearUnderscoreto': 'year_to'
    }

    def __init__(self, elements=null, numUnderscoresetUnderscoreparts=null, numUnderscoresets=null, partUnderscoreimgUnderscoreurl=null, yearUnderscorefrom=null, yearUnderscoreto=null):  # noqa: E501
        """PartColorsElement - a model defined in OpenAPI"""  # noqa: E501

        self._elements = None
        self._numUnderscoresetUnderscoreparts = None
        self._numUnderscoresets = None
        self._partUnderscoreimgUnderscoreurl = None
        self._yearUnderscorefrom = None
        self._yearUnderscoreto = None
        self.discriminator = None

        if elements is not None:
            self.elements = elements
        if numUnderscoresetUnderscoreparts is not None:
            self.numUnderscoresetUnderscoreparts = numUnderscoresetUnderscoreparts
        if numUnderscoresets is not None:
            self.numUnderscoresets = numUnderscoresets
        if partUnderscoreimgUnderscoreurl is not None:
            self.partUnderscoreimgUnderscoreurl = partUnderscoreimgUnderscoreurl
        if yearUnderscorefrom is not None:
            self.yearUnderscorefrom = yearUnderscorefrom
        if yearUnderscoreto is not None:
            self.yearUnderscoreto = yearUnderscoreto

    @property
    def elements(self):
        """Gets the elements of this PartColorsElement.  # noqa: E501


        :return: The elements of this PartColorsElement.  # noqa: E501
        :rtype: List
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this PartColorsElement.


        :param elements: The elements of this PartColorsElement.  # noqa: E501
        :type: List
        """

        self._elements = elements

    @property
    def numUnderscoresetUnderscoreparts(self):
        """Gets the numUnderscoresetUnderscoreparts of this PartColorsElement.  # noqa: E501


        :return: The numUnderscoresetUnderscoreparts of this PartColorsElement.  # noqa: E501
        :rtype: Integer
        """
        return self._numUnderscoresetUnderscoreparts

    @numUnderscoresetUnderscoreparts.setter
    def numUnderscoresetUnderscoreparts(self, numUnderscoresetUnderscoreparts):
        """Sets the numUnderscoresetUnderscoreparts of this PartColorsElement.


        :param numUnderscoresetUnderscoreparts: The numUnderscoresetUnderscoreparts of this PartColorsElement.  # noqa: E501
        :type: Integer
        """

        self._numUnderscoresetUnderscoreparts = numUnderscoresetUnderscoreparts

    @property
    def numUnderscoresets(self):
        """Gets the numUnderscoresets of this PartColorsElement.  # noqa: E501


        :return: The numUnderscoresets of this PartColorsElement.  # noqa: E501
        :rtype: Integer
        """
        return self._numUnderscoresets

    @numUnderscoresets.setter
    def numUnderscoresets(self, numUnderscoresets):
        """Sets the numUnderscoresets of this PartColorsElement.


        :param numUnderscoresets: The numUnderscoresets of this PartColorsElement.  # noqa: E501
        :type: Integer
        """

        self._numUnderscoresets = numUnderscoresets

    @property
    def partUnderscoreimgUnderscoreurl(self):
        """Gets the partUnderscoreimgUnderscoreurl of this PartColorsElement.  # noqa: E501


        :return: The partUnderscoreimgUnderscoreurl of this PartColorsElement.  # noqa: E501
        :rtype: String
        """
        return self._partUnderscoreimgUnderscoreurl

    @partUnderscoreimgUnderscoreurl.setter
    def partUnderscoreimgUnderscoreurl(self, partUnderscoreimgUnderscoreurl):
        """Sets the partUnderscoreimgUnderscoreurl of this PartColorsElement.


        :param partUnderscoreimgUnderscoreurl: The partUnderscoreimgUnderscoreurl of this PartColorsElement.  # noqa: E501
        :type: String
        """

        self._partUnderscoreimgUnderscoreurl = partUnderscoreimgUnderscoreurl

    @property
    def yearUnderscorefrom(self):
        """Gets the yearUnderscorefrom of this PartColorsElement.  # noqa: E501


        :return: The yearUnderscorefrom of this PartColorsElement.  # noqa: E501
        :rtype: Integer
        """
        return self._yearUnderscorefrom

    @yearUnderscorefrom.setter
    def yearUnderscorefrom(self, yearUnderscorefrom):
        """Sets the yearUnderscorefrom of this PartColorsElement.


        :param yearUnderscorefrom: The yearUnderscorefrom of this PartColorsElement.  # noqa: E501
        :type: Integer
        """

        self._yearUnderscorefrom = yearUnderscorefrom

    @property
    def yearUnderscoreto(self):
        """Gets the yearUnderscoreto of this PartColorsElement.  # noqa: E501


        :return: The yearUnderscoreto of this PartColorsElement.  # noqa: E501
        :rtype: Integer
        """
        return self._yearUnderscoreto

    @yearUnderscoreto.setter
    def yearUnderscoreto(self, yearUnderscoreto):
        """Sets the yearUnderscoreto of this PartColorsElement.


        :param yearUnderscoreto: The yearUnderscoreto of this PartColorsElement.  # noqa: E501
        :type: Integer
        """

        self._yearUnderscoreto = yearUnderscoreto

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PartColorsElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
