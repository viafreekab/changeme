from changeme.scanners.http_get import HTTPGetScanner
from requests.auth import HTTPBasicAuth


class HTTPBasicAuthScanner(HTTPGetScanner):
    pass

    def _make_request(self):
        self.logger.debug("Requesting %s" % self.url)
        self.response = self.request.get(self.url,
                                         auth=HTTPBasicAuth(self.username, self.password),
                                         verify=False,
                                         proxies=self.config.proxy,
                                         timeout=self.config.timeout,
                                         headers=self.headers,
                                         cookies=self.cookies)
