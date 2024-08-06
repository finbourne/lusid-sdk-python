# QueryableKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | The address that is the query to be made into the system. e.g. a Valuation/PV or Instrument/MaturityDate | 
**description** | **str** | What does the information that is being queried by the address mean. What is the address for. | [optional] 
**display_name** | **str** | The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address. | 
**type** | **str** | Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the more complex representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \&quot;Result0D\&quot;, the decimal-currency pair. | 
**flattened_type** | **str** | Financially meaningful results can be presented as either simple flat types or more complex expanded types. This field gives the type of the simpler representation.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied) or as a decimal-currency pair. In this example, the type returned in this field would be \&quot;Decimal\&quot;. | 
**holding_quantity_scaling** | **str** | Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and PV. The present value of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the contract size. | 
**supported_usages** | **List[str]** | The types of queries that support this key. | 
**supported_operations** | **List[str]** | When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context). | 
**life_cycle_status** | **str** | Within an API where an item can be accessed through an address or property, there is an associated status that determines whether the item is stable or likely to change. This status is one of [Experimental, Beta, EAP, Prod,  Deprecated]. If the item is deprecated it will be removed on or after the associated DateTime RemovalDate field. That field will not otherwise be set. | 
**removal_date** | **datetime** | If the life cycle status is set to deprecated then this will be populated with the date on or after which removal of the address query will happen | [optional] 
**applicable_options** | [**Dict[str, AddressKeyOptionDefinition]**](AddressKeyOptionDefinition.md) | A mapping from option names to the definition that the corresponding option value must match. | [optional] 
**derivation_formula** | **str** | Derivation formula for when the for when the query key represents a DerivedValuation property. | [optional] 

## Example

```python
from lusid.models.queryable_key import QueryableKey

# TODO update the JSON string below
json = "{}"
# create an instance of QueryableKey from a JSON string
queryable_key_instance = QueryableKey.from_json(json)
# print the JSON string representation of the object
print QueryableKey.to_json()

# convert the object into a dict
queryable_key_dict = queryable_key_instance.to_dict()
# create an instance of QueryableKey from a dict
queryable_key_form_dict = queryable_key.from_dict(queryable_key_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


