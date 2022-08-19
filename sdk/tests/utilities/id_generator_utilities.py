import logging
import os

import lusid
from lusid import ApiException
from utilities import TestDataUtilities


def delete_entities(id_generator):

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    logger = logging.getLogger()

    api_client = TestDataUtilities.api_client()

    property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
    portfolios_api = lusid.PortfoliosApi(api_client)
    cut_labels = lusid.CutLabelDefinitionsApi(api_client)
    orders_api = lusid.OrdersApi(api_client)
    recipes_api = lusid.ConfigurationRecipeApi(api_client)
    corporate_action_sources_api = lusid.CorporateActionSourcesApi(api_client)

    for item in id_generator.pop_scope_and_codes():
        entity = item[0]
        scope = item[1]
        code = item[2]

        log_str = ' '.join(item)

        try:
            if entity == "property_definition":
                domain = item[3]
                property_definitions_api.delete_property_definition(domain, scope, code)
                logger.info(f"deleting property definition: {log_str}")
            elif entity == "portfolio":
                portfolios_api.delete_portfolio(scope, code)
                logger.info(f"deleting portfolio: {log_str}")
            elif entity == "cut_label":
                cut_labels.delete_cut_label_definition(code)
                logger.info(f"deleting cut label: {log_str}")
            elif entity == "order":
                orders_api.delete_order(scope, code)
                logger.info(f"deleting order: {log_str}")
            elif entity == "recipe":
                recipes_api.delete_configuration_recipe(scope, code)
                logger.info(f"deleting recipe: {log_str}")
            elif entity == "ca_source":
                corporate_action_sources_api.delete_corporate_action_source(scope, code)
                logger.info(f"deleting corporate action source: {log_str}")
            else:
                logging.warning(f"unknown entity: {log_str}")
        except ApiException as ex:
            logging.error(ex)
