<?php

declare(strict_types=1);

namespace UiUxPro\Mcp;

use Psr\Http\Message\ResponseFactoryInterface;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\MiddlewareInterface;
use Psr\Http\Server\RequestHandlerInterface;

final class BearerTokenMiddleware implements MiddlewareInterface
{
    public function __construct(
        private readonly ResponseFactoryInterface $responses,
        private readonly string $expectedToken,
    ) {
    }

    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        $authorization = trim($request->getHeaderLine('Authorization'));
        if (1 !== preg_match('/^Bearer\s+([A-Za-z0-9._~+\/-]+=*)$/iD', $authorization, $matches)
            || !hash_equals($this->expectedToken, $matches[1])) {
            return $this->responses->createResponse(401)
                ->withHeader('WWW-Authenticate', 'Bearer')
                ->withHeader('Cache-Control', 'no-store');
        }

        return $handler->handle($request);
    }
}
