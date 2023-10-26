# PackageRequest

A request to create or update a Package.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | Related order ids. | 
**order_instruction_ids** | [**List[ResourceId]**](ResourceId.md) | Related order instruction ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 

## Example

```python
from lusid.models.package_request import PackageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PackageRequest from a JSON string
package_request_instance = PackageRequest.from_json(json)
# print the JSON string representation of the object
print PackageRequest.to_json()

# convert the object into a dict
package_request_dict = package_request_instance.to_dict()
# create an instance of PackageRequest from a dict
package_request_form_dict = package_request.from_dict(package_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


