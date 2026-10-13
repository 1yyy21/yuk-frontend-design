"""Exercise the bundled search entry point and persistence in an isolated folder."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
entry = root / 'skills/yukiskill/scripts/design-search.py'


def run(*arguments):
    process = subprocess.run([sys.executable, '-X', 'utf8', str(entry), *arguments], capture_output=True, text=True, encoding='utf-8')
    if process.returncode:
        raise RuntimeError(process.stderr or process.stdout)
    return process.stdout


ux = json.loads(run('keyboard focus modal', '--domain', 'ux', '--json'))
assert ux['count'] > 0 and ux['domain'] == 'ux', 'UX retrieval returned no relevant records'
stack = json.loads(run('form validation', '--stack', 'react', '--json'))
assert stack['count'] > 0 and stack['stack'] == 'react', 'React guidance missing'
with tempfile.TemporaryDirectory(prefix='yukiskill-check-') as temporary:
    run('productivity dashboard', '--design-system', '-p', 'IntegrationCheck', '--persist', '--output-dir', temporary)
    masters = list(Path(temporary).rglob('MASTER.md'))
    assert len(masters) == 1, 'Expected one persisted design system'
    master = masters[0]
    master.write_text('Existing user design must survive\n', encoding='utf-8')
    run('finance dashboard', '--design-system', '-p', 'IntegrationCheck', '--persist', '--output-dir', temporary)
    assert master.read_text(encoding='utf-8') == 'Existing user design must survive\n', 'Existing design was overwritten'
print('Passed: UX retrieval, React guidance, isolated persistence, existing-design preservation.')
