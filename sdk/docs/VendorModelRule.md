# VendorModelRule

A rule that identifies the set of preferences to be used for a given library, model and instrument type.  There can be many such rules, though only the first found for a given combination would be used.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | **str** | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc | 
**model_name** | **str** | The vendor library model name | 
**instrument_type** | **str** | The vendor library instrument type | 
**parameters** | **str** | THIS FIELD IS DEPRECATED - use ModelOptions  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood. | [optional] 
**model_options** | [**ModelOptions**](ModelOptions.md) |  | [optional] 
**instrument_id** | **str** | This field should generally not be required. It indicates a specific case where there is a particular need to make a rule apply to only a single instrument  specified by an identifier on that instrument such as its LUID. One particular example would be to control the behaviour of a look-through portfolio scaling  methodology, such as where there is a mixture of indices and credit-debit portfolios where scaling on the sum of valuation would be deemed incorrectly for one  set but desired in general. | [optional] 
**address_key_filters** | [**List[AddressKeyFilter]**](AddressKeyFilter.md) | Condition for model selection. If a condition is satisfied the default model for valuation is overridden (for that instrument). | [optional] 

## Example

```python
from lusid.models.vendor_model_rule import VendorModelRule

# TODO update the JSON string below
json = "{}"
# create an instance of VendorModelRule from a JSON string
vendor_model_rule_instance = VendorModelRule.from_json(json)
# print the JSON string representation of the object
print VendorModelRule.to_json()

# convert the object into a dict
vendor_model_rule_dict = vendor_model_rule_instance.to_dict()
# create an instance of VendorModelRule from a dict
vendor_model_rule_form_dict = vendor_model_rule.from_dict(vendor_model_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


