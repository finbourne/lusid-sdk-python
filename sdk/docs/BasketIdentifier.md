# BasketIdentifier

Descriptive information that describes a particular basket of instruments. Most commonly required with a CDS Index or similarly defined instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** | Index set, e.g. iTraxx or CDX. | 
**name** | **str** | The index name within the set, e.g. \&quot;MAIN\&quot; or \&quot;Crossover\&quot;. | 
**region** | **str** | Applicable geographic country or region. Typically something like \&quot;Europe\&quot;, \&quot;Asia ex-Japan\&quot;, \&quot;Japan\&quot; or \&quot;Australia\&quot;. | 
**series_id** | **int** | The series identifier. | 
## Example

```python
from lusid.models.basket_identifier import BasketIdentifier
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr

index: StrictStr = "example_index"
name: StrictStr = "example_name"
region: StrictStr = "example_region"
series_id: StrictInt = # Replace with your value
series_id: StrictInt = 42
basket_identifier_instance = BasketIdentifier(index=index, name=name, region=region, series_id=series_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

