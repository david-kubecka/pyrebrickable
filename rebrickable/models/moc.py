# coding: utf-8

"""
    

     This is pyrebrickable, a python CLI wrapper around the Rebrickable API<br> <br> It supports the v3 API through it's openAPI specification.<br> https://rebrickable.com/api/v3/swagger/?format=openapi<br> Models for Part, Set, etc. have been manually added to provide meaningful results from HTTP responses<br> <br> Some endpoints might not work, don't hesitate to file an issue<br>   # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Moc(object):
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
        'designer_name': 'str',
        'designer_url': 'str',
        'moc_img_url': 'str',
        'moc_url': 'str',
        'name': 'str',
        'num_parts': 'int',
        'set_num': 'str',
        'theme_id': 'int',
        'year': 'int'
    }

    attribute_map = {
        'designer_name': 'designer_name',
        'designer_url': 'designer_url',
        'moc_img_url': 'moc_img_url',
        'moc_url': 'moc_url',
        'name': 'name',
        'num_parts': 'num_parts',
        'set_num': 'set_num',
        'theme_id': 'theme_id',
        'year': 'year'
    }

    def __init__(self, designer_name=None, designer_url=None, moc_img_url=None, moc_url=None, name=None, num_parts=None, set_num=None, theme_id=None, year=None):  # noqa: E501
        """Moc - a model defined in Swagger"""  # noqa: E501

        self._designer_name = None
        self._designer_url = None
        self._moc_img_url = None
        self._moc_url = None
        self._name = None
        self._num_parts = None
        self._set_num = None
        self._theme_id = None
        self._year = None
        self.discriminator = None

        if designer_name is not None:
            self.designer_name = designer_name
        if designer_url is not None:
            self.designer_url = designer_url
        if moc_img_url is not None:
            self.moc_img_url = moc_img_url
        if moc_url is not None:
            self.moc_url = moc_url
        if name is not None:
            self.name = name
        if num_parts is not None:
            self.num_parts = num_parts
        if set_num is not None:
            self.set_num = set_num
        if theme_id is not None:
            self.theme_id = theme_id
        if year is not None:
            self.year = year

    @property
    def designer_name(self):
        """Gets the designer_name of this Moc.  # noqa: E501


        :return: The designer_name of this Moc.  # noqa: E501
        :rtype: str
        """
        return self._designer_name

    @designer_name.setter
    def designer_name(self, designer_name):
        """Sets the designer_name of this Moc.


        :param designer_name: The designer_name of this Moc.  # noqa: E501
        :type: str
        """

        self._designer_name = designer_name

    @property
    def designer_url(self):
        """Gets the designer_url of this Moc.  # noqa: E501


        :return: The designer_url of this Moc.  # noqa: E501
        :rtype: str
        """
        return self._designer_url

    @designer_url.setter
    def designer_url(self, designer_url):
        """Sets the designer_url of this Moc.


        :param designer_url: The designer_url of this Moc.  # noqa: E501
        :type: str
        """

        self._designer_url = designer_url

    @property
    def moc_img_url(self):
        """Gets the moc_img_url of this Moc.  # noqa: E501


        :return: The moc_img_url of this Moc.  # noqa: E501
        :rtype: str
        """
        return self._moc_img_url

    @moc_img_url.setter
    def moc_img_url(self, moc_img_url):
        """Sets the moc_img_url of this Moc.


        :param moc_img_url: The moc_img_url of this Moc.  # noqa: E501
        :type: str
        """

        self._moc_img_url = moc_img_url

    @property
    def moc_url(self):
        """Gets the moc_url of this Moc.  # noqa: E501


        :return: The moc_url of this Moc.  # noqa: E501
        :rtype: str
        """
        return self._moc_url

    @moc_url.setter
    def moc_url(self, moc_url):
        """Sets the moc_url of this Moc.


        :param moc_url: The moc_url of this Moc.  # noqa: E501
        :type: str
        """

        self._moc_url = moc_url

    @property
    def name(self):
        """Gets the name of this Moc.  # noqa: E501


        :return: The name of this Moc.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Moc.


        :param name: The name of this Moc.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_parts(self):
        """Gets the num_parts of this Moc.  # noqa: E501


        :return: The num_parts of this Moc.  # noqa: E501
        :rtype: int
        """
        return self._num_parts

    @num_parts.setter
    def num_parts(self, num_parts):
        """Sets the num_parts of this Moc.


        :param num_parts: The num_parts of this Moc.  # noqa: E501
        :type: int
        """

        self._num_parts = num_parts

    @property
    def set_num(self):
        """Gets the set_num of this Moc.  # noqa: E501


        :return: The set_num of this Moc.  # noqa: E501
        :rtype: str
        """
        return self._set_num

    @set_num.setter
    def set_num(self, set_num):
        """Sets the set_num of this Moc.


        :param set_num: The set_num of this Moc.  # noqa: E501
        :type: str
        """

        self._set_num = set_num

    @property
    def theme_id(self):
        """Gets the theme_id of this Moc.  # noqa: E501


        :return: The theme_id of this Moc.  # noqa: E501
        :rtype: int
        """
        return self._theme_id

    @theme_id.setter
    def theme_id(self, theme_id):
        """Sets the theme_id of this Moc.


        :param theme_id: The theme_id of this Moc.  # noqa: E501
        :type: int
        """

        self._theme_id = theme_id

    @property
    def year(self):
        """Gets the year of this Moc.  # noqa: E501


        :return: The year of this Moc.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Moc.


        :param year: The year of this Moc.  # noqa: E501
        :type: int
        """

        self._year = year

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
        if not isinstance(other, Moc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other