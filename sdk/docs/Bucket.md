# Bucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_lot_id** | **str** | The identifier of the tax lot this bucket is for. | [optional] 
**movement_name** | **str** | The name of the movement. | [optional] 
**holding_type** | **str** | The type of the holding. | [optional] 
**economic_bucket** | **str** | The economic bucket. | [optional] 
**economic_bucket_component** | **str** | The economic bucket component. | [optional] 
**economic_bucket_variant** | **str** | The economic bucket component. | [optional] 
**holding_sign** | **str** | The holding sign. | [optional] 
**local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**units** | **float** | The units. | [optional] 
**activity_date** | **datetime** | The activity date of the bucket. | [optional] 

## Example

```python
from lusid.models.bucket import Bucket

# TODO update the JSON string below
json = "{}"
# create an instance of Bucket from a JSON string
bucket_instance = Bucket.from_json(json)
# print the JSON string representation of the object
print Bucket.to_json()

# convert the object into a dict
bucket_dict = bucket_instance.to_dict()
# create an instance of Bucket from a dict
bucket_form_dict = bucket.from_dict(bucket_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


