# PackageSetRequest

A request to create or update multiple Packages.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PackageRequest]**](PackageRequest.md) | A collection of PackageRequests. | [optional] 

## Example

```python
from lusid.models.package_set_request import PackageSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PackageSetRequest from a JSON string
package_set_request_instance = PackageSetRequest.from_json(json)
# print the JSON string representation of the object
print PackageSetRequest.to_json()

# convert the object into a dict
package_set_request_dict = package_set_request_instance.to_dict()
# create an instance of PackageSetRequest from a dict
package_set_request_form_dict = package_set_request.from_dict(package_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


