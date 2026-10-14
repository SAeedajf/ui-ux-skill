#!/usr/bin/env python3
"""Structural checks for the UI/UX Skills repository."""
import csv, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.eval_harness import quality_definitions, validate_all as validate_eval_results, validate_domain_quality_refs, validate_domain_source_refs
from scripts.source_coverage import source_ids_in_files
errors=[]
def fail(msg): errors.append(msg)
# Skill folders and frontmatter.
skills=ROOT/'.agents/skills'
found=[]
for p in sorted(skills.iterdir()):
 if not p.is_dir() or p.name.startswith('.'): continue
 found.append(p.name); f=p/'SKILL.md'
 if not f.is_file(): fail(f'{p.name}: missing SKILL.md'); continue
 text=f.read_text(encoding='utf-8')
 if not text.startswith('---\n') or text.count('---')<2: fail(f'{p.name}: invalid frontmatter delimiters'); continue
 front=text.split('---',2)[1]
 name=re.search(r'^name:\s*(.+)$',front,re.M); desc=re.search(r'^description:\s*(.+)$',front,re.M)
 if not name or name.group(1).strip()!=p.name: fail(f'{p.name}: name must match folder')
 if not desc or len(desc.group(1))<40 or not desc.group(1).strip().startswith('Use when '): fail(f'{p.name}: description must start with a specific Use when trigger')
 for ref in re.findall(r'\[[^]]+\]\(([^)]+)\)',text):
  if not ref.startswith(('http://','https://','#')) and not (p/ref).exists(): fail(f'{p.name}: broken link {ref}')
if len(found)!=15: fail(f'expected 15 Skills, found {len(found)}')
# Source registry.
with (ROOT/'docs/source-registry.csv').open(encoding='utf-8',newline='') as f: sources=list(csv.DictReader(f))
ids=[r['id'] for r in sources]
if len(sources)!=124 or len(set(ids))!=124 or set(ids)!=set(map(str,range(1,125))): fail('source registry must contain unique IDs 1..124')
if any(not r.get('submitted_url') or not r.get('url') for r in sources): fail('each source needs submitted_url and reviewed/canonical url')
if len({r['submitted_url'] for r in sources})!=124: fail('submitted_url must preserve the 124 distinct source links')
if any(not r.get(k) for r in sources for k in ('pass_1','pass_2','checkpoint_5','review_date')): fail('every source needs two review passes, a five-source checkpoint, and review date')
if sum(r['review_status']=='partially_verified' for r in sources)!=6: fail('expected six explicitly partial sources')
source_ids=set(ids)
reference_files=sorted(p for skill_dir in skills.iterdir() for p in skill_dir.glob('references/*.md'))
unlinked_sources={int(sid) for sid in source_ids}-source_ids_in_files(reference_files,{int(sid) for sid in source_ids})
if unlinked_sources: fail(f'source registry IDs lack a Skill reference method/decision link: {", ".join(map(str,sorted(unlinked_sources)))}')
# Coverage mapping.
with (ROOT/'docs/domain-coverage.csv').open(encoding='utf-8',newline='') as f: domains=list(csv.DictReader(f))
if len(domains)!=14: fail(f'expected 14 domain rows, found {len(domains)}')
for row in domains:
 for sid in row['source_ids'].split(';'):
  if sid not in source_ids: fail(f"{row['domain']}: unknown source ID {sid}")
 for skill in row['primary_skills'].split(';'):
  if skill not in found: fail(f"{row['domain']}: unknown Skill {skill}")
for error in validate_domain_source_refs(domains, source_ids): fail(error)
for error in validate_domain_quality_refs(domains, quality_definitions()): fail(error)
# Evals.
with (ROOT/'evals/activation.jsonl').open(encoding='utf-8') as f: evals=[json.loads(x) for x in f if x.strip()]
for skill in found:
 cases=[x for x in evals if x['skill']==skill]
 if not any(x['case']=='positive' for x in cases) or not any(x['case']=='negative' for x in cases): fail(f'{skill}: needs positive and negative activation evals')
if len(evals)!=30: fail(f'expected 30 activation cases, found {len(evals)}')
eval_ids=[x.get('id') for x in evals]
if any(not isinstance(x,str) or not x for x in eval_ids) or len(set(eval_ids))!=len(evals): fail('activation definitions need unique stable IDs')
for error in validate_eval_results(): fail(error)
# Quality scenario count.
quality=(ROOT/'evals/quality-scenarios.md').read_text(encoding='utf-8')
quality_count=len(re.findall(r'^\d+\. \*\*',quality,re.M))
if quality_count!=len(quality_definitions()): fail(f'quality scenario count mismatch: {quality_count}')
with (ROOT/'evals/run-log.csv').open(encoding='utf-8',newline='') as f: runs=list(csv.DictReader(f))
if any(None in row for row in runs): fail('evals/run-log.csv has malformed rows or column counts')
# Repo docs.
for path in ['README.md','AGENTS.md','LICENSE','CONTRIBUTING.md','docs/installation.md','evals/quality-scenarios.md']:
 if not (ROOT/path).is_file(): fail(f'missing {path}')
if errors:
 print('\n'.join('ERROR: '+e for e in errors));sys.exit(1)
print(f'OK: {len(found)} skills, {len(sources)} sources ({sum(r["review_status"]=="reviewed" for r in sources)} reviewed / 6 partial), {len(domains)} domains, {len(evals)} activation cases, {quality_count} quality scenarios; execution states validated separately')
