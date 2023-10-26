# JELinesQueryParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The start date of the JELines. | [optional] 
**end_date** | **str** | The end date of the JELInes | [optional] 
**filter** | **str** | Expression to filter the result set. | [optional] 
**property_keys** | **List[str]** | A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39; domain to decorate onto the JELine. | [optional] 

## Example

```python
from lusid.models.je_lines_query_parameters import JELinesQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of JELinesQueryParameters from a JSON string
je_lines_query_parameters_instance = JELinesQueryParameters.from_json(json)
# print the JSON string representation of the object
print JELinesQueryParameters.to_json()

# convert the object into a dict
je_lines_query_parameters_dict = je_lines_query_parameters_instance.to_dict()
# create an instance of JELinesQueryParameters from a dict
je_lines_query_parameters_form_dict = je_lines_query_parameters.from_dict(je_lines_query_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


