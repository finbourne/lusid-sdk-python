# AggregationOptions

Options for controlling the default aspects and behaviour of the aggregation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_ansi_like_syntax** | **bool** | Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \&quot;select a,sum(a) from results\&quot;;  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a). | [optional] 
**allow_partial_entitlement_success** | **bool** | In the case of valuing a portfolio group where some, but not all entitlements fail, should the aggregation return the valuations  applied only to those portfolios where entitlements checks succeeded. | [optional] 
**apply_iso4217_rounding** | **bool** | Various results that are units of currency might need to be rounded.  This will round according to the ISO4217 standard number of decimal places for a currency. | [optional] 

## Example

```python
from lusid.models.aggregation_options import AggregationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationOptions from a JSON string
aggregation_options_instance = AggregationOptions.from_json(json)
# print the JSON string representation of the object
print AggregationOptions.to_json()

# convert the object into a dict
aggregation_options_dict = aggregation_options_instance.to_dict()
# create an instance of AggregationOptions from a dict
aggregation_options_form_dict = aggregation_options.from_dict(aggregation_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


