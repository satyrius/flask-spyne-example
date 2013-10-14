from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer
from spyne.model.primitive import Unicode


class HelloWorldService(ServiceBase):
    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(name, times):
        for i in range(times):
            yield u'Hello, %s' % name


application = Application(
    [HelloWorldService], 'flask-spyne-example',
    in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

wsgi_application = WsgiApplication(application)
