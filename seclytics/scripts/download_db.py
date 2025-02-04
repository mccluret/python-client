from .. import Seclytics
from optparse import OptionParser
from texttable import Texttable
from pprint import pprint

def run():
    # pass in the access_token via commandline
    parser = OptionParser()
    parser.add_option("--access_token",
                      action="store", type="string", dest="access_token",
                      help="API acccess_token")
    parser.add_option("--api_url",
                      action="store", type="string", dest="api_url",
                      default='https://api.seclytics.com/',
                      help="API Hostname")

    parser.add_option("--name",
                      action="store", type="string", dest="name",
                      help="Bulk API Name")

    parser.add_option("--data-dir",
                      action="store", type="string", dest="data_dir",
                      help="Directory to store DBs")

    (options, args) = parser.parse_args()

    if options.access_token is None:
        parser.error('access_token not given')
    if options.name is None:
        parser.error('name is required')

    # initialize the client with your token
    access_token = options.access_token
    api_url = options.api_url
    client = Seclytics(access_token=access_token)
    names = options.name.split(',')
    for name in names:
        client.bulk_api_download(name, data_dir=options.data_dir)

if __name__ == '__main__':
    run()
