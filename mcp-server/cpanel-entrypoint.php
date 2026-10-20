<?php

declare(strict_types=1);

// cPanel requires addon-domain document roots to remain under public_html.
// This small public front controller keeps the application and its config private.
$privateRoot = getenv('UIUX_MCP_PRIVATE_ROOT') ?: dirname(__DIR__, 2).'/uiux-mcp-private/ui-ux-pro-mcp';
$entrypoint = rtrim($privateRoot, '/').'/public/index.php';

if (!is_file($entrypoint)) {
    error_log('ui-ux-pro-mcp private entrypoint is unavailable.');
    http_response_code(503);
    header('Cache-Control: no-store');
    echo 'MCP service is not available.';
    exit;
}

require $entrypoint;
