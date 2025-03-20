output "function_app_url" {
  value = azurerm_linux_function_app.func.default_hostname
}

output "function_app_name" {
  value = azurerm_linux_function_app.func.name
}

# Use `azurerm_function_app_host_keys` for keys
output "function_app_master_key" {
  value = azurerm_function_app_host_keys.func.default_function_key
  sensitive = true
}

output "function_app_system_key" {
  value = azurerm_function_app_host_keys.func.system_key
  sensitive = true
}
