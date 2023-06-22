terraform {
  required_providers {
    confluence = {
      source  = "atlassian/confluence"
    }
  }
}

provider "confluence" {
  url        = "https://vaishnav-vsri.atlassian.net/wiki/home"
  username   = "vaishnavsri2@gmail.com"
  password   = "Rahul@123"
}

resource "confluence_page" "my_page" {
  space_key     = "~62b4ef640c77011bdfde15dd"
  title         = "terraform"
  body          = file("README.md")  # Provide the path to your README file
  version_number = 2  # Specify the desired version number for the updated page
}
