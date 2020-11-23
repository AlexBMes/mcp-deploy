terraform {
  backend "gcs" {
    bucket = "mcp-deployment-action-test"
  }
}

module "mcp" {
  source = "../../../../../mcp"
}