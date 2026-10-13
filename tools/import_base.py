"""Reassemble approved public build parts and reject any byte mismatch."""
import hashlib
import json
from pathlib import Path
import subprocess

spec = json.loads(Path('releases/android-63001.json').read_text())
assert spec['base_version'] == 'android-63001'
expected = {'auto-farm-v0.63.0-android-arm64.apk', 'android-base.zip', 'release-verification.json'}
assert {f['name'] for f in spec['files']} == expected
output = Path('build')
output.mkdir(exist_ok=True)
for item in spec['files']:
    digest = hashlib.sha256()
    size = 0
    with (output / item['name']).open('wb') as target:
        for part in item['parts']:
            assert part.startswith('https://auto-farm.liuqinh2s.chatgpt.site/downloads/android-63001/')
            block = subprocess.check_output(['curl', '--fail', '--silent', '--show-error',
                '--location', '--retry', '3', '--connect-timeout', '15', '--max-time', '120',
                '--max-filesize', str(8 * 1024 * 1024), part])
            size += len(block)
            assert size <= item['size'], 'Oversized download'
            digest.update(block)
            target.write(block)
    assert size == item['size'] and digest.hexdigest() == item['sha256'], 'Download checksum mismatch'
    print('Verified', item['name'], size)
