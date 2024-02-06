from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    Responsable for interact with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        #Lógica de regra de negócios
        #Retorno HTTP
        return HttpResponse(status_code=200, body={"hello": "fucking world"})