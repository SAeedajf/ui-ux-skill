<?php

declare(strict_types=1);

namespace UiUxPro\Mcp;

use Mcp\Server;
use Mcp\Server\Session\FileSessionLock;
use Mcp\Server\Session\FileSessionStore;

final class ServerFactory
{
    public static function build(SkillCatalog $catalog, string $sessionDirectory): Server
    {
        $builder = Server::builder()
            ->setServerInfo(
                'ui-ux-pro-mcp',
                '0.1.0',
                'Read-only MCP access to the UI/UX Pro Agent Skills and their authored reference notes.',
            )
            ->setSession(
                sessionStore: new FileSessionStore($sessionDirectory, ttl: 3600),
            )
            ->setSessionLock(new FileSessionLock($sessionDirectory, timeout: 20));

        $builder->addTool(
            static fn (): string => self::json($catalog->list()),
            name: 'list_uiux_skills',
            title: 'List UI/UX Skills',
            description: 'List available UI/UX Pro Skills and their activation descriptions. Use this to choose a focused Skill before requesting its full content.',
            inputSchema: ['type' => 'object', 'properties' => new \stdClass(), 'additionalProperties' => false],
        );

        $builder->addTool(
            static fn (string $query, ?string $skill_id = null, int $limit = 5): string => self::json($catalog->search($query, $skill_id, $limit)),
            name: 'search_uiux_guidance',
            title: 'Search UI/UX guidance',
            description: 'Search the skill files and linked authored reference notes. Returns short excerpts with Skill IDs and relative source paths; fetch a full Skill or reference only when needed.',
            inputSchema: [
                'type' => 'object',
                'properties' => [
                    'query' => ['type' => 'string', 'minLength' => 1, 'maxLength' => 180],
                    'skill_id' => ['type' => 'string', 'pattern' => '^[a-z0-9]+(?:-[a-z0-9]+)*$'],
                    'limit' => ['type' => 'integer', 'minimum' => 1, 'maximum' => 10, 'default' => 5],
                ],
                'required' => ['query'],
                'additionalProperties' => false,
            ],
        );

        $builder->addTool(
            static fn (string $skill_id): string => $catalog->readSkill($skill_id),
            name: 'read_uiux_skill',
            title: 'Read a UI/UX Skill',
            description: 'Read the full SKILL.md for one exact Skill ID returned by list_uiux_skills.',
            inputSchema: [
                'type' => 'object',
                'properties' => ['skill_id' => ['type' => 'string', 'pattern' => '^[a-z0-9]+(?:-[a-z0-9]+)*$']],
                'required' => ['skill_id'],
                'additionalProperties' => false,
            ],
        );

        $builder->addTool(
            static fn (string $skill_id, string $path): string => $catalog->readReference($skill_id, $path),
            name: 'read_uiux_reference',
            title: 'Read a UI/UX reference note',
            description: 'Read one Markdown reference beneath a Skill references/ directory. The path must be a relative file path such as references/forms.md.',
            inputSchema: [
                'type' => 'object',
                'properties' => [
                    'skill_id' => ['type' => 'string', 'pattern' => '^[a-z0-9]+(?:-[a-z0-9]+)*$'],
                    'path' => ['type' => 'string', 'minLength' => 15, 'maxLength' => 180],
                ],
                'required' => ['skill_id', 'path'],
                'additionalProperties' => false,
            ],
        );

        foreach ($catalog->list() as $skill) {
            $id = $skill['id'];
            $builder->addResource(
                static fn (string $uri): string => $catalog->readSkill($id),
                uri: 'uiux://skills/'.$id,
                name: $id,
                title: $skill['name'],
                description: $skill['description'],
                mimeType: 'text/markdown',
            );
        }

        return $builder->build();
    }

    private static function json(mixed $value): string
    {
        return json_encode($value, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT | JSON_THROW_ON_ERROR);
    }
}
