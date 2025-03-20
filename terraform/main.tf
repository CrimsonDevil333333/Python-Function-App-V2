# Create a Resource Group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# Create a Storage Account
resource "azurerm_storage_account" "storage" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard" # Standard performance
  account_replication_type = "LRS" # Locally redundant storage
}

# Create an App Service Plan (Consumption-based)
resource "azurerm_service_plan" "plan" {
  name                = "azure-functions-plan" # Name of the App Service Plan
  location           = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type            = "Linux" # Linux-based App Service Plan
  sku_name           = "Y1" # Y1 is the smallest and cheapest SKU (can be changed to P1V2/P2V2... for more power)
}

# Create the Azure Function App
resource "azurerm_linux_function_app" "func" {
  name                       = var.function_app_name
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  service_plan_id            = azurerm_service_plan.plan.id
  storage_account_name       = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key

  site_config {
    application_stack {
      python_version = "3.11" # Python 3.11 runtime
    }
  }
}

# Create Host Keys for the Function App
resource "azurerm_function_app_host_keys" "func" {
  name            = azurerm_linux_function_app.func.name
  resource_group_name = azurerm_resource_group.rg.name
}
