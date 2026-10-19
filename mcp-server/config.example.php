<?php

return [
    // Put this file outside the public document root and copy it to config.local.php.
    // Generate a long random token out-of-band; never commit the real value.
    'bearer_token' => '',
    'allowed_hosts' => ['mcp.possino.ir'],
    'skills_directory' => __DIR__.'/content/skills',
    'session_directory' => __DIR__.'/var/sessions',
];
