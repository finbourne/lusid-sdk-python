# WithholdingTaxDataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the relational dataset definition. | 
**code** | **str** | The code of the relational dataset definition. Together with the scope this uniquely identifies the definition. | 
**dataset_type** | **str** | Which of the two rate tables this dataset is: Anomaly or Main. Set when the dataset is created through the withholding tax dataset definitions endpoint and never changed afterwards. Available values: Anomaly, Main. | [optional] 
**dimensions** | [**List[SeriesIdentifierField]**](SeriesIdentifierField.md) | The dimensions created on this dataset as series identifiers, as stored. The mandatory core is not returned here; read the full field schema from the relational dataset definition at Href. | 
**href** | **str** | The specific Uri of the relational dataset definition. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.withholding_tax_dataset import WithholdingTaxDataset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
dataset_type: Optional[StrictStr] = "example_dataset_type"
dimensions: List[SeriesIdentifierField] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
withholding_tax_dataset_instance = WithholdingTaxDataset(scope=scope, code=code, dataset_type=dataset_type, dimensions=dimensions, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

