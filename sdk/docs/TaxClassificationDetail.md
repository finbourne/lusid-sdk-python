# TaxClassificationDetail

A single instrument's classification with the version history of every input behind it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**classification** | [**TaxClassification**](TaxClassification.md) |  | 
**history** | [**List[TaxClassificationFieldVersion]**](TaxClassificationFieldVersion.md) | Every version of every classification input and override for the instrument, oldest first. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.tax_classification_detail import TaxClassificationDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
classification: TaxClassification
history: List[TaxClassificationFieldVersion] = # Replace with your value
links: Optional[List[Link]] = None
tax_classification_detail_instance = TaxClassificationDetail(href=href, classification=classification, history=history, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

