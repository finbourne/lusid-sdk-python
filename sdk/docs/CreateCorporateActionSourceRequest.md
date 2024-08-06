# CreateCorporateActionSourceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the corporate action source | 
**code** | **str** | The code of the corporate action source | 
**display_name** | **str** | The name of the corporate action source | 
**description** | **str** | The description of the corporate action source | [optional] 
**instrument_scopes** | **List[str]** | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. | [optional] 

## Example

```python
from lusid.models.create_corporate_action_source_request import CreateCorporateActionSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCorporateActionSourceRequest from a JSON string
create_corporate_action_source_request_instance = CreateCorporateActionSourceRequest.from_json(json)
# print the JSON string representation of the object
print CreateCorporateActionSourceRequest.to_json()

# convert the object into a dict
create_corporate_action_source_request_dict = create_corporate_action_source_request_instance.to_dict()
# create an instance of CreateCorporateActionSourceRequest from a dict
create_corporate_action_source_request_form_dict = create_corporate_action_source_request.from_dict(create_corporate_action_source_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


