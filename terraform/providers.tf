terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "tf-backend-rg"
    storage_account_name = "tfbackendstorage"
    container_name       = "tfstate"
    key                  = "azure-functions.tfstate"
  }
}

provider "azurerm" {
  features {}
}
