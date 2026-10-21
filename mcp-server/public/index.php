<?php

declare(strict_types=1);

use Mcp\Server\Transport\Http\Middleware\CorsMiddleware;
use Mcp\Server\Transport\Http\Middleware\DnsRebindingProtectionMiddleware;
use Mcp\Server\Transport\StreamableHttpTransport;
use Nyholm\Psr7\Factory\Psr17Factory;
use Nyholm\Psr7Server\ServerRequestCreator;
use UiUxPro\Mcp\BearerTokenMiddleware;
use UiUxPro\Mcp\ServerFactory;
use UiUxPro\Mcp\SkillCatalog;

require dirname(__DIR__).'/vendor/autoload.php';

$settingsPath = dirname(__DIR__).'/config.local.php';
$settings = is_file($settingsPath) ? require $settingsPath : [];
$settings = is_array($settings) ? $settings : [];
$token = (string) ($settings['bearer_token'] ?? getenv('UIUX_MCP_BEARER_TOKEN') ?: '');
$allowedHosts = $settings['allowed_hosts'] ?? array_filter(array_map('trim', explode(',', (string) (getenv('UIUX_MCP_ALLOWED_HOSTS') ?: ''))));
$skillsDirectory = (string) ($settings['skills_directory'] ?? getenv('UIUX_MCP_SKILLS_DIR') ?: dirname(__DIR__).'/content/skills');
$sessionDirectory = (string) ($settings['session_directory'] ?? getenv('UIUX_MCP_SESSION_DIR') ?: dirname(__DIR__).'/var/sessions');

$method = strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? 'GET'));
$requestPath = parse_url((string) ($_SERVER['REQUEST_URI'] ?? '/'), PHP_URL_PATH) ?: '/';
if ('GET' === $method && '/health' === $requestPath) {
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo '{"status":"ok","service":"ui-ux-pro-mcp"}';
    exit;
}
if (!in_array($requestPath, ['/', '/index.php'], true)) {
    http_response_code(404);
    header('Cache-Control: no-store');
    exit;
}
if ('' === $token || [] === $allowedHosts) {
    http_response_code(503);
    header('Cache-Control: no-store');
    echo 'MCP service is not configured.';
    exit;
}

try {
    $factory = new Psr17Factory();
    $creator = new ServerRequestCreator($factory, $factory, $factory, $factory);
    $request = $creator->fromGlobals();
    $catalog = new SkillCatalog($skillsDirectory);
    $server = ServerFactory::build($catalog, $sessionDirectory);
    $transport = new StreamableHttpTransport(
        request: $request,
        responseFactory: $factory,
        streamFactory: $factory,
        middleware: [
            new CorsMiddleware(),
            new DnsRebindingProtectionMiddleware(allowedHosts: $allowedHosts),
            new BearerTokenMiddleware($factory, $token),
        ],
        maxBodyBytes: 1_048_576,
    );
    $response = $server->run($transport)->withHeader('Cache-Control', 'no-store');

    http_response_code($response->getStatusCode());
    foreach ($response->getHeaders() as $name => $values) {
        foreach ($values as $value) {
            header($name.': '.$value, false);
        }
    }
    echo (string) $response->getBody();
} catch (Throwable $error) {
    error_log('ui-ux-pro-mcp request failed: '.get_class($error));
    http_response_code(500);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo '{"error":"MCP request could not be processed."}';
}
