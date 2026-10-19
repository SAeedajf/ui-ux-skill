<?php

declare(strict_types=1);

use UiUxPro\Mcp\SkillCatalog;

require dirname(__DIR__).'/vendor/autoload.php';

$skillsDirectory = getenv('UIUX_MCP_SKILLS_DIR') ?: dirname(__DIR__, 2).'/.agents/skills';
$catalog = new SkillCatalog($skillsDirectory);
$checks = 0;

$assert = static function (bool $condition, string $message) use (&$checks): void {
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
    ++$checks;
};

$skills = $catalog->list();
$assert(15 === count($skills), 'catalog exposes the expected 15 canonical Skills');
$assert('accessibility-inclusive-design' === $skills[0]['id'], 'catalog ordering is deterministic');
$assert('forms-input' === array_values(array_filter($skills, static fn (array $item): bool => 'forms-input' === $item['id']))[0]['id'], 'catalog includes the forms Skill');
$assert(str_contains($catalog->readSkill('forms-input'), 'name: forms-input'), 'exact Skill content can be read');
$assert([] !== $catalog->search('validation error', 'forms-input', 5), 'search returns relevant form guidance');

$blocked = false;
try {
    $catalog->readSkill('../composer');
} catch (RuntimeException) {
    $blocked = true;
}
$assert($blocked, 'path traversal cannot select another file');

$blocked = false;
try {
    $catalog->readReference('forms-input', '../../composer.json');
} catch (RuntimeException) {
    $blocked = true;
}
$assert($blocked, 'reference reader is restricted to reference Markdown');

printf("PASS: %d MCP catalog checks\n", $checks);
