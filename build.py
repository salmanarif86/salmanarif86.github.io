from base64 import b64encode
from pathlib import Path


root = Path(__file__).parent
source = (root / "index.html").read_text()
portrait = b64encode((root / "assets" / "sal-arif.png").read_bytes()).decode("ascii")
single_file = source.replace("assets/sal-arif.png", f"data:image/png;base64,{portrait}")
output = root / "dist" / "sal-arif-website.html"
output.parent.mkdir(exist_ok=True)
output.write_text(single_file)
print(output)
