"""Reassemble approved public build parts and reject any byte mismatch."""
import hashlib
import json
from pathlib import Path
import urllib.request

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
            with urllib.request.urlopen(part, timeout=60) as response:
                while block := response.read(1024 * 1024):
                    size += len(block)
                    assert size <= item['size'], 'Oversized download'
                    digest.update(block)
                    target.write(block)
    assert size == item['size'] and digest.hexdigest() == item['sha256'], 'Download checksum mismatch'
    print('Verified', item['name'], size)
