from urllib import request, parse, error
from collections import namedtuple
from datetime import datetime
from xml.etree import ElementTree
import json


class RequestAPI(object):
    """Handles links, parameters and connections to source API"""

    def __init__(self, api, **kwargs):
        self.api = api
        self.pars = kwargs
        self.url = self.build_link()
        self.resp = self.get_resp()

    def build_link(self):
        """Returns full url to connect and get data"""

        api_scheme, api_netloc, api_path, api_query, api_fragment = parse.urlsplit(self.api)

        Link = namedtuple('Link', 'scheme, netloc, path, query, fragment')
        url_pars = Link(scheme=api_scheme,
                        netloc=api_netloc,
                        path=api_path,
                        query=api_query,
                        fragment=api_fragment)

        url = url_pars._replace(**self.pars)

        return parse.urlunsplit(url)

    def get_resp(self):
        """Connects and pulls xml data"""

        try:
            data = request.urlopen(self.url)
        except error.URLError:
            proxy_support = request.ProxyHandler({'http': 'rb-proxy-de.bosch.com:8080',
                                                  'https': 'rb-proxy-special.bosch.com:8080'})
            opener = request.build_opener(proxy_support)
            request.install_opener(opener)
            data = request.urlopen(self.url)

        # TODO: Delete the above proxy code and uncomment the below line
        # data = request.urlopen(self.url)
        enc = data.headers.get_content_charset()

        return data.read().decode(enc)


class ParseAPI(RequestAPI):
    """Parsing any API response"""

    def __init__(self, api, **kwargs):
        super().__init__(api, **kwargs)

        if self.resp[0] == '<':
            self.root = self.parse_xml()
        else:
            self.root = self.parse_json()

    def parse_xml(self):
        """Parses xml objects"""

        return ElementTree.fromstring(self.resp)

    def parse_json(self):
        """Parses json objects"""

        return json.loads(self.resp)


def processor():
    """Apps main controller"""

    # source_api = 'https://jsonplaceholder.typicode.com/comments'
    source_api = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'
    par = 'date_req'
    value = datetime.today().strftime('%d/%m/%Y')

    pars = {
        'query': f'{par}={value}'
    }

    my_req = ParseAPI(source_api, **pars)
    # my_req = ParseAPI(source_api)

    # For XML data type processing

    print(my_req.root.tag, my_req.root.attrib)

    for child in my_req.root:
        currency = child.find('CharCode').text
        value = child.find('Value').text
        print(f'{currency}: {value}')
        print('-' * 20)

    # For JSON data processing
    # for data in my_req.root:
    #     print(data['postId'])


if __name__ == '__main__':
    processor()
