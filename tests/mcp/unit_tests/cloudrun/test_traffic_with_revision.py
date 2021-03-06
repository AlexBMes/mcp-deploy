from sys import path, stderr

try:
    path.insert(1, '../../../test_fixtures/python_validator')
    from python_validator import python_validator
except Exception as e:
    print(e, stderr)

"""
    checks that the data given to the test function is in the correct format
    for the google_cloud_run_service.traffic setting.

    The configuration for traffic comes from the gcp_cloudrun.yml configuration file,
    and should be transformed into a list of maps, which should have the configuration
    for each traffic setting.

    E.g.
    traffic:
      -
        percent: 25
        revision_name: "old"

    needs to be configured in google_cloud_run_service to match:
    traffic{
      percent = 25
      latest_revision = false
      revision_name = "old"
    }
    """

expected_data = {
    "latest_revision": "false",
    "percent": "25",
    "revision_name": "old"
}

if __name__ == '__main__':
    python_validator(expected_data)
