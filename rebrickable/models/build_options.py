# coding: utf-8

"""
    

     This is pyrebrickable, a python CLI wrapper around the Rebrickable API<br> <br> It supports the v3 API through it's openAPI specification.<br> https://rebrickable.com/api/v3/swagger/?format=openapi<br> Models for Part, Set, etc. have been manually added to provide meaningful results from HTTP responses<br> <br> Some endpoints might not work, don't hesitate to file an issue<br>   # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BuildOptions(object):
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
        'color': 'int',
        'ignore_altp': 'bool',
        'ignore_minifigs': 'bool',
        'ignore_mold': 'bool',
        'ignore_non_lego': 'bool',
        'ignore_print': 'bool',
        'inc_accessory': 'bool',
        'inc_bmodels': 'bool',
        'inc_custom': 'bool',
        'inc_official': 'bool',
        'inc_owned': 'bool',
        'inc_premium': 'bool',
        'max_parts': 'int',
        'max_year': 'int',
        'min_parts': 'int',
        'min_year': 'int',
        'sort_by': 'int'
    }

    attribute_map = {
        'color': 'color',
        'ignore_altp': 'ignore_altp',
        'ignore_minifigs': 'ignore_minifigs',
        'ignore_mold': 'ignore_mold',
        'ignore_non_lego': 'ignore_non_lego',
        'ignore_print': 'ignore_print',
        'inc_accessory': 'inc_accessory',
        'inc_bmodels': 'inc_bmodels',
        'inc_custom': 'inc_custom',
        'inc_official': 'inc_official',
        'inc_owned': 'inc_owned',
        'inc_premium': 'inc_premium',
        'max_parts': 'max_parts',
        'max_year': 'max_year',
        'min_parts': 'min_parts',
        'min_year': 'min_year',
        'sort_by': 'sort_by'
    }

    def __init__(self, color=None, ignore_altp=None, ignore_minifigs=None, ignore_mold=None, ignore_non_lego=None, ignore_print=None, inc_accessory=None, inc_bmodels=None, inc_custom=None, inc_official=None, inc_owned=None, inc_premium=None, max_parts=None, max_year=None, min_parts=None, min_year=None, sort_by=None):  # noqa: E501
        """BuildOptions - a model defined in Swagger"""  # noqa: E501

        self._color = None
        self._ignore_altp = None
        self._ignore_minifigs = None
        self._ignore_mold = None
        self._ignore_non_lego = None
        self._ignore_print = None
        self._inc_accessory = None
        self._inc_bmodels = None
        self._inc_custom = None
        self._inc_official = None
        self._inc_owned = None
        self._inc_premium = None
        self._max_parts = None
        self._max_year = None
        self._min_parts = None
        self._min_year = None
        self._sort_by = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if ignore_altp is not None:
            self.ignore_altp = ignore_altp
        if ignore_minifigs is not None:
            self.ignore_minifigs = ignore_minifigs
        if ignore_mold is not None:
            self.ignore_mold = ignore_mold
        if ignore_non_lego is not None:
            self.ignore_non_lego = ignore_non_lego
        if ignore_print is not None:
            self.ignore_print = ignore_print
        if inc_accessory is not None:
            self.inc_accessory = inc_accessory
        if inc_bmodels is not None:
            self.inc_bmodels = inc_bmodels
        if inc_custom is not None:
            self.inc_custom = inc_custom
        if inc_official is not None:
            self.inc_official = inc_official
        if inc_owned is not None:
            self.inc_owned = inc_owned
        if inc_premium is not None:
            self.inc_premium = inc_premium
        if max_parts is not None:
            self.max_parts = max_parts
        if max_year is not None:
            self.max_year = max_year
        if min_parts is not None:
            self.min_parts = min_parts
        if min_year is not None:
            self.min_year = min_year
        if sort_by is not None:
            self.sort_by = sort_by

    @property
    def color(self):
        """Gets the color of this BuildOptions.  # noqa: E501


        :return: The color of this BuildOptions.  # noqa: E501
        :rtype: int
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this BuildOptions.


        :param color: The color of this BuildOptions.  # noqa: E501
        :type: int
        """

        self._color = color

    @property
    def ignore_altp(self):
        """Gets the ignore_altp of this BuildOptions.  # noqa: E501


        :return: The ignore_altp of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_altp

    @ignore_altp.setter
    def ignore_altp(self, ignore_altp):
        """Sets the ignore_altp of this BuildOptions.


        :param ignore_altp: The ignore_altp of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._ignore_altp = ignore_altp

    @property
    def ignore_minifigs(self):
        """Gets the ignore_minifigs of this BuildOptions.  # noqa: E501


        :return: The ignore_minifigs of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_minifigs

    @ignore_minifigs.setter
    def ignore_minifigs(self, ignore_minifigs):
        """Sets the ignore_minifigs of this BuildOptions.


        :param ignore_minifigs: The ignore_minifigs of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._ignore_minifigs = ignore_minifigs

    @property
    def ignore_mold(self):
        """Gets the ignore_mold of this BuildOptions.  # noqa: E501


        :return: The ignore_mold of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_mold

    @ignore_mold.setter
    def ignore_mold(self, ignore_mold):
        """Sets the ignore_mold of this BuildOptions.


        :param ignore_mold: The ignore_mold of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._ignore_mold = ignore_mold

    @property
    def ignore_non_lego(self):
        """Gets the ignore_non_lego of this BuildOptions.  # noqa: E501


        :return: The ignore_non_lego of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_non_lego

    @ignore_non_lego.setter
    def ignore_non_lego(self, ignore_non_lego):
        """Sets the ignore_non_lego of this BuildOptions.


        :param ignore_non_lego: The ignore_non_lego of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._ignore_non_lego = ignore_non_lego

    @property
    def ignore_print(self):
        """Gets the ignore_print of this BuildOptions.  # noqa: E501


        :return: The ignore_print of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_print

    @ignore_print.setter
    def ignore_print(self, ignore_print):
        """Sets the ignore_print of this BuildOptions.


        :param ignore_print: The ignore_print of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._ignore_print = ignore_print

    @property
    def inc_accessory(self):
        """Gets the inc_accessory of this BuildOptions.  # noqa: E501


        :return: The inc_accessory of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._inc_accessory

    @inc_accessory.setter
    def inc_accessory(self, inc_accessory):
        """Sets the inc_accessory of this BuildOptions.


        :param inc_accessory: The inc_accessory of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._inc_accessory = inc_accessory

    @property
    def inc_bmodels(self):
        """Gets the inc_bmodels of this BuildOptions.  # noqa: E501


        :return: The inc_bmodels of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._inc_bmodels

    @inc_bmodels.setter
    def inc_bmodels(self, inc_bmodels):
        """Sets the inc_bmodels of this BuildOptions.


        :param inc_bmodels: The inc_bmodels of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._inc_bmodels = inc_bmodels

    @property
    def inc_custom(self):
        """Gets the inc_custom of this BuildOptions.  # noqa: E501


        :return: The inc_custom of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._inc_custom

    @inc_custom.setter
    def inc_custom(self, inc_custom):
        """Sets the inc_custom of this BuildOptions.


        :param inc_custom: The inc_custom of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._inc_custom = inc_custom

    @property
    def inc_official(self):
        """Gets the inc_official of this BuildOptions.  # noqa: E501


        :return: The inc_official of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._inc_official

    @inc_official.setter
    def inc_official(self, inc_official):
        """Sets the inc_official of this BuildOptions.


        :param inc_official: The inc_official of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._inc_official = inc_official

    @property
    def inc_owned(self):
        """Gets the inc_owned of this BuildOptions.  # noqa: E501


        :return: The inc_owned of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._inc_owned

    @inc_owned.setter
    def inc_owned(self, inc_owned):
        """Sets the inc_owned of this BuildOptions.


        :param inc_owned: The inc_owned of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._inc_owned = inc_owned

    @property
    def inc_premium(self):
        """Gets the inc_premium of this BuildOptions.  # noqa: E501


        :return: The inc_premium of this BuildOptions.  # noqa: E501
        :rtype: bool
        """
        return self._inc_premium

    @inc_premium.setter
    def inc_premium(self, inc_premium):
        """Sets the inc_premium of this BuildOptions.


        :param inc_premium: The inc_premium of this BuildOptions.  # noqa: E501
        :type: bool
        """

        self._inc_premium = inc_premium

    @property
    def max_parts(self):
        """Gets the max_parts of this BuildOptions.  # noqa: E501


        :return: The max_parts of this BuildOptions.  # noqa: E501
        :rtype: int
        """
        return self._max_parts

    @max_parts.setter
    def max_parts(self, max_parts):
        """Sets the max_parts of this BuildOptions.


        :param max_parts: The max_parts of this BuildOptions.  # noqa: E501
        :type: int
        """

        self._max_parts = max_parts

    @property
    def max_year(self):
        """Gets the max_year of this BuildOptions.  # noqa: E501


        :return: The max_year of this BuildOptions.  # noqa: E501
        :rtype: int
        """
        return self._max_year

    @max_year.setter
    def max_year(self, max_year):
        """Sets the max_year of this BuildOptions.


        :param max_year: The max_year of this BuildOptions.  # noqa: E501
        :type: int
        """

        self._max_year = max_year

    @property
    def min_parts(self):
        """Gets the min_parts of this BuildOptions.  # noqa: E501


        :return: The min_parts of this BuildOptions.  # noqa: E501
        :rtype: int
        """
        return self._min_parts

    @min_parts.setter
    def min_parts(self, min_parts):
        """Sets the min_parts of this BuildOptions.


        :param min_parts: The min_parts of this BuildOptions.  # noqa: E501
        :type: int
        """

        self._min_parts = min_parts

    @property
    def min_year(self):
        """Gets the min_year of this BuildOptions.  # noqa: E501


        :return: The min_year of this BuildOptions.  # noqa: E501
        :rtype: int
        """
        return self._min_year

    @min_year.setter
    def min_year(self, min_year):
        """Sets the min_year of this BuildOptions.


        :param min_year: The min_year of this BuildOptions.  # noqa: E501
        :type: int
        """

        self._min_year = min_year

    @property
    def sort_by(self):
        """Gets the sort_by of this BuildOptions.  # noqa: E501


        :return: The sort_by of this BuildOptions.  # noqa: E501
        :rtype: int
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this BuildOptions.


        :param sort_by: The sort_by of this BuildOptions.  # noqa: E501
        :type: int
        """

        self._sort_by = sort_by

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
        if not isinstance(other, BuildOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other