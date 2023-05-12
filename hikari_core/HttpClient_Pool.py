import httpx
from httpx import Request, Response
from loguru import logger

#if config.proxy_on:
#    proxy = {"https://": config.proxy}
#else:
#    proxy = {}
proxy = {"https://": "http://localhost:7890"}
                   
yuyuko_headers = {
    #'Authorization': config.api_token,
    'accept':'application/json',
    'Content-Type':'application/json',
}


async def before_request(request:Request):
    logger.info(f"{request.method} {request.url}")
    
async def after_response(response:Response):
    logger.info(f"本次响应的状态码:{response.status_code} {response.http_version} {response.request}")
    
client_yuyuko = httpx.AsyncClient(
    headers=yuyuko_headers,
    event_hooks={
        "request":[before_request,],
        "response":[after_response,]
        },
    http2 = True
    )

client_wg = httpx.AsyncClient(
    proxies=proxy
)

client_default = httpx.AsyncClient(
)