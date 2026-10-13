#!/usr/bin/env python3
"""Structural checks for the UI/UX Skills repository."""
import csv, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def fail(msg): errors.append(msg)
# Skill folders and frontmatter.
skills=ROOT/'.agents/skills'
found=[]
for p in sorted(skills.iterdir()):
 if not p.is_dir(): continue
 found.append(p.name); f=p/'SKILL.md'
 if not f.is_file(): fail(f'{p.name}: missing SKILL.md'); continue
 text=f.read_text(encoding='utf-8')
 if not text.startswith('---\n') or text.count('---')<2: fail(f'{p.name}: invalid frontmatter delimiters'); continue
 front=text.split('---',2)[1]
 name=re.search(r'^name:\s*(.+)$',front,re.M); desc=re.search(r'^description:\s*(.+)$',front,re.M)
 if not name or name.group(1).strip()!=p.name: fail(f'{p.name}: name must match folder')
 if not desc or len(desc.group(1))<40: fail(f'{p.name}: description must be specific')
 for ref in re.findall(r'\[[^]]+\]\(([^)]+)\)',text):
  if not ref.startswith(('http://','https://','#')) and not (p/ref).exists(): fail(f'{p.name}: broken link {ref}')
if len(found)!=8: fail(f'expected 8 Skills, found {len(found)}')
# Source registry.
with (ROOT/'docs/source-registry.csv').open(encoding='utf-8',newline='') as f: sources=list(csv.DictReader(f))
ids=[r['id'] for r in sources]
if len(sources)!=124 or len(set(ids))!=124 or set(ids)!=set(map(str,range(1,125))): fail('source registry must contain unique IDs 1..124')
if sum(r['review_status']=='partially_verified' for r in sources)!=6: fail('expected six explicitly partial sources')
source_ids=set(ids)
# Coverage mapping.
with (ROOT/'docs/domain-coverage.csv').open(encoding='utf-8',newline='') as f: domains=list(csv.DictReader(f))
if len(domains)!=14: fail(f'expected 14 domain rows, found {len(domains)}')
for row in domains:
 for sid in row['source_ids'].split(';'):
  if sid not in source_ids: fail(f"{row['domain']}: unknown source ID {sid}")
 for skill in row['primary_skills'].split(';'):
  if skill not in found: fail(f"{row['domain']}: unknown Skill {skill}")
# Evals.
with (ROOT/'evals/activation.jsonl').open(encoding='utf-8') as f: evals=[json.loads(x) for x in f if x.strip()]
for skill in found:
 cases=[x for x in evals if x['skill']==skill]
 if not any(x['case']=='positive' for x in cases) or not any(x['case']=='negative' for x in cases): fail(f'{skill}: needs positive and negative activation evals')
 if any(x.get('status')!='not_run' for x in cases): fail(f'{skill}: authoring must not mark evals run')
# Repo docs.
for path in ['README.md','AGENTS.md','LICENSE','CONTRIBUTING.md','docs/installation.md','evals/quality-scenarios.md']:
 if not (ROOT/path).is_file(): fail(f'missing {path}')
if errors:
 print('\n'.join('ERROR: '+e for e in errors));sys.exit(1)
print(f'OK: {len(found)} skills, {len(sources)} sources ({sum(r["review_status"]=="reviewed" for r in sources)} reviewed / 6 partial), {len(domains)} domains, {len(evals)} activation cases (not run)')
