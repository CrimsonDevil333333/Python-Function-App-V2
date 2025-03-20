terraform {
  backend "azurerm" {
    resource_group_name   = "tf-backend-rg"       # Resource Group where the storage account is
    storage_account_name  = "tfbackendpocstorage01"    # Storage Account Name
    container_name        = "tfstate"             # Container where Terraform state is stored
    key                   = "azure-functions.tfstate" # State file name
  }
}