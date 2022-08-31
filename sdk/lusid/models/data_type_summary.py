# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4746
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class DataTypeSummary(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'type_value_range': 'str',
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'value_type': 'str',
        'acceptable_values': 'list[str]',
        'unit_schema': 'str',
        'acceptable_units': 'list[IUnitDefinitionDto]'
    }

    attribute_map = {
        'type_value_range': 'typeValueRange',
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'value_type': 'valueType',
        'acceptable_values': 'acceptableValues',
        'unit_schema': 'unitSchema',
        'acceptable_units': 'acceptableUnits'
    }

    required_map = {
        'type_value_range': 'required',
        'id': 'required',
        'display_name': 'required',
        'description': 'required',
        'value_type': 'required',
        'acceptable_values': 'optional',
        'unit_schema': 'optional',
        'acceptable_units': 'optional'
    }

    def __init__(self, type_value_range=None, id=None, display_name=None, description=None, value_type=None, acceptable_values=None, unit_schema=None, acceptable_units=None, local_vars_configuration=None):  # noqa: E501
        """DataTypeSummary - a model defined in OpenAPI"
        
        :param type_value_range:  Indicates the range of data acceptable by a data type. The available values are: Open, Closed (required)
        :type type_value_range: str
        :param id:  (required)
        :type id: lusid.ResourceId
        :param display_name:  The display name of the data type. (required)
        :type display_name: str
        :param description:  The description of the data type. (required)
        :type description: str
        :param value_type:  The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel (required)
        :type value_type: str
        :param acceptable_values:  The acceptable set of values for this data type. Only applies to 'open' value type range.
        :type acceptable_values: list[str]
        :param unit_schema:  The schema of the data type's units. The available values are: NoUnits, Basic, Iso4217Currency
        :type unit_schema: str
        :param acceptable_units:  The definitions of the acceptable units.
        :type acceptable_units: list[lusid.IUnitDefinitionDto]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type_value_range = None
        self._id = None
        self._display_name = None
        self._description = None
        self._value_type = None
        self._acceptable_values = None
        self._unit_schema = None
        self._acceptable_units = None
        self.discriminator = None

        self.type_value_range = type_value_range
        self.id = id
        self.display_name = display_name
        self.description = description
        self.value_type = value_type
        self.acceptable_values = acceptable_values
        if unit_schema is not None:
            self.unit_schema = unit_schema
        self.acceptable_units = acceptable_units

    @property
    def type_value_range(self):
        """Gets the type_value_range of this DataTypeSummary.  # noqa: E501

        Indicates the range of data acceptable by a data type. The available values are: Open, Closed  # noqa: E501

        :return: The type_value_range of this DataTypeSummary.  # noqa: E501
        :rtype: str
        """
        return self._type_value_range

    @type_value_range.setter
    def type_value_range(self, type_value_range):
        """Sets the type_value_range of this DataTypeSummary.

        Indicates the range of data acceptable by a data type. The available values are: Open, Closed  # noqa: E501

        :param type_value_range: The type_value_range of this DataTypeSummary.  # noqa: E501
        :type type_value_range: str
        """
        if self.local_vars_configuration.client_side_validation and type_value_range is None:  # noqa: E501
            raise ValueError("Invalid value for `type_value_range`, must not be `None`")  # noqa: E501
        allowed_values = ["Open", "Closed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type_value_range not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type_value_range` ({0}), must be one of {1}"  # noqa: E501
                .format(type_value_range, allowed_values)
            )

        self._type_value_range = type_value_range

    @property
    def id(self):
        """Gets the id of this DataTypeSummary.  # noqa: E501


        :return: The id of this DataTypeSummary.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataTypeSummary.


        :param id: The id of this DataTypeSummary.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this DataTypeSummary.  # noqa: E501

        The display name of the data type.  # noqa: E501

        :return: The display_name of this DataTypeSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DataTypeSummary.

        The display name of the data type.  # noqa: E501

        :param display_name: The display_name of this DataTypeSummary.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this DataTypeSummary.  # noqa: E501

        The description of the data type.  # noqa: E501

        :return: The description of this DataTypeSummary.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataTypeSummary.

        The description of the data type.  # noqa: E501

        :param description: The description of this DataTypeSummary.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def value_type(self):
        """Gets the value_type of this DataTypeSummary.  # noqa: E501

        The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :return: The value_type of this DataTypeSummary.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this DataTypeSummary.

        The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :param value_type: The value_type of this DataTypeSummary.  # noqa: E501
        :type value_type: str
        """
        if self.local_vars_configuration.client_side_validation and value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501
        allowed_values = ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def acceptable_values(self):
        """Gets the acceptable_values of this DataTypeSummary.  # noqa: E501

        The acceptable set of values for this data type. Only applies to 'open' value type range.  # noqa: E501

        :return: The acceptable_values of this DataTypeSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._acceptable_values

    @acceptable_values.setter
    def acceptable_values(self, acceptable_values):
        """Sets the acceptable_values of this DataTypeSummary.

        The acceptable set of values for this data type. Only applies to 'open' value type range.  # noqa: E501

        :param acceptable_values: The acceptable_values of this DataTypeSummary.  # noqa: E501
        :type acceptable_values: list[str]
        """

        self._acceptable_values = acceptable_values

    @property
    def unit_schema(self):
        """Gets the unit_schema of this DataTypeSummary.  # noqa: E501

        The schema of the data type's units. The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :return: The unit_schema of this DataTypeSummary.  # noqa: E501
        :rtype: str
        """
        return self._unit_schema

    @unit_schema.setter
    def unit_schema(self, unit_schema):
        """Sets the unit_schema of this DataTypeSummary.

        The schema of the data type's units. The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :param unit_schema: The unit_schema of this DataTypeSummary.  # noqa: E501
        :type unit_schema: str
        """
        allowed_values = ["NoUnits", "Basic", "Iso4217Currency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unit_schema not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unit_schema` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_schema, allowed_values)
            )

        self._unit_schema = unit_schema

    @property
    def acceptable_units(self):
        """Gets the acceptable_units of this DataTypeSummary.  # noqa: E501

        The definitions of the acceptable units.  # noqa: E501

        :return: The acceptable_units of this DataTypeSummary.  # noqa: E501
        :rtype: list[lusid.IUnitDefinitionDto]
        """
        return self._acceptable_units

    @acceptable_units.setter
    def acceptable_units(self, acceptable_units):
        """Sets the acceptable_units of this DataTypeSummary.

        The definitions of the acceptable units.  # noqa: E501

        :param acceptable_units: The acceptable_units of this DataTypeSummary.  # noqa: E501
        :type acceptable_units: list[lusid.IUnitDefinitionDto]
        """

        self._acceptable_units = acceptable_units

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataTypeSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataTypeSummary):
            return True

        return self.to_dict() != other.to_dict()