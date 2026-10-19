<?php

declare(strict_types=1);

namespace UiUxPro\Mcp;

use RuntimeException;
use SplFileInfo;
use RecursiveDirectoryIterator;
use RecursiveIteratorIterator;

final class SkillCatalog
{
    public function __construct(private readonly string $skillsRoot)
    {
        $root = realpath($skillsRoot);
        if (false === $root || !is_dir($root)) {
            throw new RuntimeException('Skill content directory is unavailable.');
        }
    }

    /** @return list<array{id: string, name: string, description: string}> */
    public function list(): array
    {
        $root = $this->root();
        $skills = [];
        foreach (new RecursiveDirectoryIterator($root, RecursiveDirectoryIterator::SKIP_DOTS) as $entry) {
            if (!$entry->isDir() || $entry->isLink()) {
                continue;
            }
            $id = $entry->getFilename();
            if (!$this->validId($id)) {
                continue;
            }
            $path = $this->containedFile($id, 'SKILL.md');
            if (null === $path) {
                continue;
            }
            $source = file_get_contents($path);
            if (false === $source) {
                continue;
            }
            $skills[] = [
                'id' => $id,
                'name' => $this->frontMatterValue($source, 'name') ?? $id,
                'description' => $this->frontMatterValue($source, 'description') ?? '',
            ];
        }
        usort($skills, static fn (array $a, array $b): int => strcmp($a['id'], $b['id']));

        return $skills;
    }

    public function readSkill(string $id): string
    {
        $path = $this->containedFile($id, 'SKILL.md');
        if (null === $path) {
            throw new RuntimeException('Unknown UI/UX Skill.');
        }
        $contents = file_get_contents($path);
        if (false === $contents) {
            throw new RuntimeException('Skill content could not be read.');
        }

        return $contents;
    }

    public function readReference(string $id, string $relativePath): string
    {
        if (!$this->validId($id) || str_contains($relativePath, "\0")) {
            throw new RuntimeException('Invalid Skill or reference path.');
        }
        $relativePath = str_replace('\\', '/', $relativePath);
        if (!str_starts_with($relativePath, 'references/') || !str_ends_with(strtolower($relativePath), '.md')) {
            throw new RuntimeException('Only Markdown files inside a Skill references directory can be read.');
        }
        $path = $this->containedFile($id, $relativePath);
        if (null === $path || !is_file($path)) {
            throw new RuntimeException('Unknown UI/UX reference.');
        }
        $contents = file_get_contents($path);
        if (false === $contents) {
            throw new RuntimeException('Reference content could not be read.');
        }

        return $contents;
    }

    /** @return list<array{skill_id: string, path: string, score: int, excerpt: string}> */
    public function search(string $query, ?string $skillId = null, int $limit = 5): array
    {
        $query = trim($query);
        if ('' === $query || strlen($query) > 180) {
            throw new RuntimeException('Search query must contain 1–180 characters.');
        }
        if ($limit < 1 || $limit > 10) {
            throw new RuntimeException('Search result limit must be between 1 and 10.');
        }
        if (null !== $skillId && !$this->validId($skillId)) {
            throw new RuntimeException('Unknown UI/UX Skill.');
        }

        $terms = preg_split('/\s+/u', $query, -1, PREG_SPLIT_NO_EMPTY) ?: [$query];
        $matches = [];
        foreach ($this->markdownFiles($skillId) as [$id, $relativePath, $path]) {
            $text = file_get_contents($path);
            if (false === $text) {
                continue;
            }
            $score = 0;
            $firstOffset = null;
            foreach ($terms as $term) {
                $count = substr_count(mb_strtolower($text, 'UTF-8'), mb_strtolower($term, 'UTF-8'));
                if ($count > 0) {
                    $score += min($count, 20);
                    $offset = mb_stripos($text, $term, 0, 'UTF-8');
                    if (false !== $offset && (null === $firstOffset || $offset < $firstOffset)) {
                        $firstOffset = $offset;
                    }
                }
            }
            if ($score < 1 || null === $firstOffset) {
                continue;
            }
            $snippetStart = max(0, $firstOffset - 220);
            $excerpt = trim(mb_substr($text, $snippetStart, 520, 'UTF-8'));
            $matches[] = [
                'skill_id' => $id,
                'path' => $relativePath,
                'score' => $score,
                'excerpt' => $excerpt,
            ];
        }
        usort($matches, static fn (array $a, array $b): int => ($b['score'] <=> $a['score']) ?: strcmp($a['path'], $b['path']));

        return array_slice($matches, 0, $limit);
    }

    private function root(): string
    {
        $root = realpath($this->skillsRoot);
        if (false === $root) {
            throw new RuntimeException('Skill content directory is unavailable.');
        }

        return $root;
    }

    private function validId(string $id): bool
    {
        return 1 === preg_match('/^[a-z0-9]+(?:-[a-z0-9]+)*$/D', $id);
    }

    private function containedFile(string $id, string $relativePath): ?string
    {
        if (!$this->validId($id)) {
            return null;
        }
        $root = $this->root();
        $skillRoot = realpath($root.DIRECTORY_SEPARATOR.$id);
        if (false === $skillRoot || !str_starts_with($skillRoot, $root.DIRECTORY_SEPARATOR) || !is_dir($skillRoot)) {
            return null;
        }
        $candidate = realpath($skillRoot.DIRECTORY_SEPARATOR.$relativePath);
        if (false === $candidate || !str_starts_with($candidate, $skillRoot.DIRECTORY_SEPARATOR) || !is_file($candidate)) {
            return null;
        }

        return $candidate;
    }

    /** @return iterable<array{string, string, string}> */
    private function markdownFiles(?string $skillId): iterable
    {
        $root = $this->root();
        $ids = null === $skillId ? array_column($this->list(), 'id') : [$skillId];
        foreach ($ids as $id) {
            $skillRoot = realpath($root.DIRECTORY_SEPARATOR.$id);
            if (false === $skillRoot) {
                continue;
            }
            foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($skillRoot, RecursiveDirectoryIterator::SKIP_DOTS)) as $entry) {
                if (!$entry instanceof SplFileInfo || !$entry->isFile() || $entry->isLink() || 'md' !== strtolower($entry->getExtension())) {
                    continue;
                }
                $path = realpath($entry->getPathname());
                if (false === $path || !str_starts_with($path, $skillRoot.DIRECTORY_SEPARATOR)) {
                    continue;
                }
                $relative = str_replace(DIRECTORY_SEPARATOR, '/', substr($path, strlen($skillRoot) + 1));
                yield [$id, $relative, $path];
            }
        }
    }

    private function frontMatterValue(string $source, string $key): ?string
    {
        if (!preg_match('/\A---\s*\R(.*?)\R---/s', $source, $frontMatter)) {
            return null;
        }
        if (!preg_match('/^'.preg_quote($key, '/').':\s*(.+)$/m', $frontMatter[1], $match)) {
            return null;
        }

        return trim(trim($match[1]), " \t\n\r\0\x0B\"'");
    }
}
