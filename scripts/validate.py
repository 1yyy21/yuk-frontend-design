"""Validate distributable skill metadata, catalog, and local Markdown links."""

from pathlib import Path
import re
import sys
import json
import hashlib
from urllib.parse import unquote

import yaml


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill = root / 'skills' / 'yuk-frontend-design'
    entry = skill / 'SKILL.md'
    if not entry.is_file():
        return ['Missing skills/yuk-frontend-design/SKILL.md']
    content = entry.read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', content, re.S)
    if not match:
        errors.append('Missing YAML frontmatter')
    else:
        metadata = yaml.safe_load(match.group(1))
        if not isinstance(metadata, dict):
            errors.append('Frontmatter must be a mapping')
        else:
            if metadata.get('name') != 'yuk-frontend-design':
                errors.append('Skill name must be yuk-frontend-design')
            description = metadata.get('description')
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                errors.append('Description must be nonempty and at most 1024 characters')

    config = yaml.safe_load((skill / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))
    if config.get('policy', {}).get('allow_implicit_invocation') is not True:
        errors.append('Implicit invocation must remain enabled')
    if '$yuk-frontend-design' not in config.get('interface', {}).get('default_prompt', ''):
        errors.append('Default prompt must reference $yuk-frontend-design')

    catalog = (skill / 'references' / 'sources.md').read_text(encoding='utf-8')
    entries = re.findall(r'^\| \[', catalog, re.M)
    if len(entries) != 24:
        errors.append(f'Expected 24 source entries, found {len(entries)}; update counts together')

    for file in root.rglob('*.md'):
        if '.git' in file.parts or 'vendor' in file.parts:
            continue
        text = file.read_text(encoding='utf-8')
        if re.search(r'[A-Za-z]:[\\/](?:Users|迅雷下载|yuki)[\\/]', text):
            errors.append(f'{file.relative_to(root)} contains a machine-specific path')
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            path = unquote(target.split('#', 1)[0])
            if path and not (file.parent / path).is_file():
                errors.append(f'{file.relative_to(root)} has a missing local link: {target}')
    for required in ('README.md', 'README.zh-CN.md', 'LICENSE', 'CONTRIBUTING.md', 'THIRD_PARTY_NOTICES.md'):
        if not (root / required).is_file():
            errors.append(f'Missing {required}')
    lock = json.loads((skill / 'upstream-lock.json').read_text(encoding='utf-8'))
    for project in lock['projects']:
        for item in project['files']:
            path = skill / item['path']
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
                errors.append(f'Upstream file missing or changed: {item["path"]}')
    return errors


if __name__ == '__main__':
    try:
        problems = validate(Path(__file__).resolve().parents[1])
    except (OSError, yaml.YAMLError, AttributeError) as exc:
        print(f'Validation failed: {exc}', file=sys.stderr)
        sys.exit(1)
    if problems:
        print('\n'.join(problems), file=sys.stderr)
        sys.exit(1)
    print('Validated: skill metadata, implicit invocation, 24 sources, local links, and public repository files.')
