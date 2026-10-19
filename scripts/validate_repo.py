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
# The role catalog is the cross-Skill routing contract. Keep each Skill represented
# and ensure its source references stay within the maintained registry.
role_catalog=ROOT/'skills/roles.md'
if not role_catalog.is_file():
 fail('missing skills/roles.md specialist role catalog')
else:
 role_text=role_catalog.read_text(encoding='utf-8')
 for skill in found:
  if f'`{skill}`' not in role_text: fail(f'specialist role catalog does not define {skill}')
 for ref in re.findall(r'\[[^]]+\]\(([^)]+)\)',role_text):
  if not ref.startswith(('http://','https://','#')) and not (role_catalog.parent/ref).exists(): fail(f'specialist role catalog has a broken link: {ref}')
 for match in re.finditer(r'\bS(\d+)(?:[–-](\d+))?\b',role_text):
  start=int(match.group(1)); end=int(match.group(2) or start)
  if start<1 or end<start or end>124: fail(f'specialist role catalog has an invalid source range: {match.group(0)}')
# Source registry.
with (ROOT/'docs/source-registry.csv').open(encoding='utf-8',newline='') as f: sources=list(csv.DictReader(f))
ids=[r['id'] for r in sources]
if len(sources)!=124 or len(set(ids))!=124 or set(ids)!=set(map(str,range(1,125))): fail('source registry must contain unique IDs 1..124')
if any(not r.get('submitted_url') or not r.get('url') for r in sources): fail('each source needs submitted_url and reviewed/canonical url')
if len({r['submitted_url'] for r in sources})!=124: fail('submitted_url must preserve the 124 distinct source links')
allowed_source_pairs={('standard_or_specification','normative_or_consensus'),('research_or_public_service_guidance','research_or_service_guidance'),('official_platform_or_design_system','implementation_guidance'),('book_or_practitioner_publication','practitioner_method'),('practitioner_or_product_guidance','practitioner_guidance'),('commercial_or_visual_inspiration','inspiration_only')}
if any((r.get('source_class'),r.get('evidence_type')) not in allowed_source_pairs for r in sources): fail('source_class and evidence_type must use a documented matching evidence pair')
if any(not r.get(k) for r in sources for k in ('pass_1','pass_2','checkpoint_5','review_date')): fail('every source needs two review passes, a five-source checkpoint, and review date')
if sum(r['review_status']=='partially_verified' for r in sources)!=6: fail('expected six explicitly partial sources')
source_ids=set(ids)
reference_files=sorted(p for skill_dir in skills.iterdir() for p in skill_dir.glob('references/*.md'))
unlinked_sources={int(sid) for sid in source_ids}-source_ids_in_files(reference_files,{int(sid) for sid in source_ids})
if unlinked_sources: fail(f'source registry IDs lack a Skill reference method/decision link: {", ".join(map(str,sorted(unlinked_sources)))}')
# Per-source implementation trace. Keep original submitted links and Skill routing auditable.
with (ROOT/'docs/source-implementation-audit.csv').open(encoding='utf-8',newline='') as f: usage_rows=list(csv.DictReader(f))
usage_by_id={row.get('id'):row for row in usage_rows}
if len(usage_rows)!=len(sources) or len(usage_by_id)!=len(sources) or set(usage_by_id)!=set(ids): fail('source implementation audit must contain exactly one row for every source ID')
registry_by_id={row['id']:row for row in sources}
if role_catalog.is_file():
 profile_ids=re.findall(r'^### (R\d{2}) — ',role_text,re.M)
 expected_profile_ids=[f'R{i:02}' for i in range(1,14)]
 if profile_ids!=expected_profile_ids: fail('role catalog must define profiles R01 through R13 exactly once and in order')
 registry_source_ids={int(source_id) for source_id in ids}
 source_ids_by_profile={profile_id:set() for profile_id in profile_ids}
 for block in re.split(r'(?=^### R\d{2} — )',role_text,flags=re.M):
  heading=re.match(r'^### (R\d{2}) — ',block)
  if not heading: continue
  profile_id=heading.group(1)
  assigned=re.search(r'^- \*\*Assigned source IDs \(complete set\):\*\* `([^`]+)`',block,re.M)
  if not assigned:
   fail(f'role catalog profile {profile_id} is missing its complete source assignment')
   continue
  for token in assigned.group(1).split(','):
   token=token.strip(); source_range=re.fullmatch(r'(\d+)(?:[–-](\d+))?',token)
   if not source_range:
    fail(f'role catalog profile {profile_id} has an invalid source assignment: {token}')
    continue
   start=int(source_range.group(1)); end=int(source_range.group(2) or start)
   assigned_ids=set(range(start,end+1))
   if start<1 or end<start or not assigned_ids.issubset(registry_source_ids): fail(f'role catalog profile {profile_id} has an out-of-range source assignment: {token}')
   source_ids_by_profile[profile_id].update(assigned_ids)
 for match in re.finditer(r'\[S(\d+)\s+[^]]*\]\((https?://[^)]+)\)',role_text):
  source=registry_by_id.get(match.group(1))
  if not source or match.group(2) not in {source.get('url'),source.get('submitted_url')}:
   fail(f'specialist role catalog citation does not match source registry: S{match.group(1)}')
 audit_role_ids={profile_id:set() for profile_id in profile_ids}
 for row in usage_rows:
  profile_list=set(filter(None,row.get('professional_role_ids','').split(';')))
  if not profile_list: fail(f'source implementation audit has no professional role assignment for source {row.get("id")}')
  for profile_id in profile_list:
   if profile_id not in audit_role_ids: fail(f'source implementation audit uses unknown professional profile {profile_id} for source {row.get("id")}')
   else: audit_role_ids[profile_id].add(int(row['id']))
 if set(int(sid) for sid in ids)!=set().union(*audit_role_ids.values()):
  fail('professional role assignments must cover every source in the registry')
 for profile_id in profile_ids:
  if audit_role_ids.get(profile_id,set())!=source_ids_by_profile.get(profile_id,set()):
   fail(f'role catalog source assignment does not match the source audit for {profile_id}')
for sid,row in usage_by_id.items():
 if row.get('submitted_url')!=registry_by_id[sid]['submitted_url']: fail(f'source implementation audit URL does not match registry for ID {sid}')
 if not row.get('domain') or not row.get('primary_skills') or not row.get('primary_skill_reference_paths'): fail(f'source implementation audit missing Skill routing for ID {sid}')
 if row.get('skill_reference_trace') not in {'individually_linked','grouped_id_range'}: fail(f'source implementation audit has unsupported or missing trace state for ID {sid}')
 for key in ('source_role','submitted_scope_fa','role_for_ai','professional_role_ids','skill_application','review_pass_1','review_pass_2','source_review_notes','review_date','claim_ceiling'):
  if not row.get(key): fail(f'source implementation audit missing {key} for ID {sid}')
 if row.get('submitted_scope_fa') and 'scope from the original request' not in row.get('role_for_ai','').lower():
  fail(f'source implementation audit role_for_ai must distinguish supplied scope from evidence for ID {sid}')
 for key in ('review_pass_1','review_pass_2','source_review_notes','review_date'):
  registry_key={'review_pass_1':'pass_1','review_pass_2':'pass_2','source_review_notes':'notes'}.get(key,key)
  if row.get(key)!=registry_by_id[sid].get(registry_key):
   fail(f'source implementation audit {key} does not match source registry for ID {sid}')
 for key in ('primary_skill_reference_paths','trace_paths'):
  for relpath in filter(None,row.get(key,'').split(';')):
   if not (ROOT/relpath).is_file(): fail(f'source implementation audit has a broken {key} path for ID {sid}: {relpath}')
# Coverage mapping.
with (ROOT/'docs/domain-coverage.csv').open(encoding='utf-8',newline='') as f: domains=list(csv.DictReader(f))
if len(domains)!=14: fail(f'expected 14 domain rows, found {len(domains)}')
domains_by_source={}
for domain_row in domains:
 for source_id in filter(None,domain_row['source_ids'].split(';')):
  domains_by_source.setdefault(source_id,[]).append(domain_row)
for row in domains:
 for sid in row['source_ids'].split(';'):
  if sid not in source_ids: fail(f"{row['domain']}: unknown source ID {sid}")
 for skill in row['primary_skills'].split(';'):
  if skill not in found: fail(f"{row['domain']}: unknown Skill {skill}")
for sid,usage in usage_by_id.items():
 coverage=domains_by_source.get(sid,[])
 expected_domains={row['domain'] for row in coverage}
 expected_skills={skill for row in coverage for skill in row['primary_skills'].split(';')}
 if not coverage or set(filter(None,usage.get('domain','').split(';')))!=expected_domains or set(filter(None,usage.get('primary_skills','').split(';')))!=expected_skills:
  fail(f'source implementation audit routing does not match domain coverage for ID {sid}')
for error in validate_domain_source_refs(domains, source_ids): fail(error)
for error in validate_domain_quality_refs(domains, quality_definitions()): fail(error)
# Evals.
with (ROOT/'evals/activation.jsonl').open(encoding='utf-8') as f: evals=[json.loads(x) for x in f if x.strip()]
for skill in found:
 cases=[x for x in evals if x['skill']==skill]
 if not any(x['case']=='positive' for x in cases) or not any(x['case']=='negative' for x in cases): fail(f'{skill}: needs positive and negative activation evals')
if len(evals)!=32: fail(f'expected 32 activation cases, found {len(evals)}')
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
